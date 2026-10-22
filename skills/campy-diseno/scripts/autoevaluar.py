#!/usr/bin/env python3
"""Autoevaluación de la skill campy-diseno: compara lo que dice la skill con el código actual.

Lee los repos desde una referencia de git (por defecto origin/main) sin tocar el árbol de trabajo
y reporta en Markdown:
  1. Rutas que cita la skill y ya no existen.
  2. Desvíos de las reglas que se pueden buscar en el código (chips con punto, botones con flecha,
     buscadores con «…», campy-blue, piezas prohibidas de Material, textos con minúscula inicial).
  3. Frescura: commits que tocaron las pantallas de referencia después de la última revisión.
  4. Aprendizajes pendientes de references/aprendizajes.md.

Uso:
  python3 scripts/autoevaluar.py                       # repos por defecto, origin/main
  python3 scripts/autoevaluar.py --campisoft-ref HEAD --campisoft /ruta/al/worktree
  python3 scripts/autoevaluar.py --sin-fetch            # no actualiza origin antes de leer

Solo informa (sale siempre con 0): las decisiones las toma quien usa la skill, con el usuario.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
HOME = Path.home()

# Pantallas de referencia y piezas compartidas: si cambian, la skill puede haber quedado vieja.
VIGILADAS = {
    "campyprov": [
        "apps/web/src/features/food/FoodResumen.tsx",
        "apps/web/src/features/food/dashboard",
        "apps/web/src/features/food/FoodPlanificacion.tsx",
        "apps/web/src/features/food/FoodModal.tsx",
        "apps/web/src/features/food/food-lib.tsx",
        "apps/web/src/components/ui",
        "apps/web/src/index.css",
    ],
    "campisoft": [
        "apps/web/src/features/shift",
        "apps/web/src/features/food/FoodResumen.tsx",
        "apps/web/src/components/ui",
        "apps/web/src/index.css",
        "worker-app/lib/theme.dart",
        "worker-app/lib/widgets",
        "worker-app/lib/screens/shell.dart",
        "worker-app/lib/screens/login.dart",
        "worker-app/lib/main.dart",
    ],
}

EXT = r"(?:tsx|ts|dart|css|json|arb|js|mjs|yaml|md)"
RUTA = re.compile(r"`((?:[\w.\-\[\]]+/)*[\w.\-\[\]]+\." + EXT + r")(?::[\d,\s\-]+)?`")
CARPETA = re.compile(r"`((?:[\w.\-]+/)+)`")


def git(repo: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    return r.stdout if r.returncode in (0, 1) else ""


def archivos(repo: Path, ref: str) -> list[str]:
    return git(repo, "ls-tree", "-r", "--name-only", ref).splitlines()


def textos_skill() -> dict[Path, str]:
    docs = [SKILL / "SKILL.md", *sorted((SKILL / "references").glob("*.md"))]
    return {p: p.read_text(encoding="utf-8") for p in docs if p.exists()}


def fecha_revision(skill_md: str) -> str | None:
    m = re.search(r"Última revisión:\s*(\d{4}-\d{2}-\d{2})", skill_md)
    return m.group(1) if m else None


def rutas_faltantes(docs: dict[Path, str], arbol: list[str]) -> list[str]:
    faltan: dict[str, list[str]] = {}
    for doc, texto in docs.items():
        if doc.name == "aprendizajes.md":
            continue
        for n, linea in enumerate(texto.splitlines(), 1):
            for m in RUTA.finditer(linea):
                ruta = m.group(1).lstrip("./")
                if "/" not in ruta and not ruta.endswith((".tsx", ".dart")):
                    continue  # nombres sueltos como `index.css` se resuelven igual abajo
                if not any(a == ruta or a.endswith("/" + ruta) for a in arbol):
                    faltan.setdefault(ruta, []).append(f"{doc.relative_to(SKILL).as_posix()}:{n}")
            for m in CARPETA.finditer(linea):
                carpeta = m.group(1).lstrip("./")
                if carpeta.count("/") < 2:
                    continue
                if not any(("/" + carpeta) in ("/" + a) for a in arbol):
                    faltan.setdefault(carpeta, []).append(f"{doc.relative_to(SKILL).as_posix()}:{n}")
    return [f"`{r}` — citada en {', '.join(sorted(set(donde))[:6])}" for r, donde in faltan.items()]


def buscar(repo: Path, ref: str, patron: str, *rutas: str, fijo: bool = False) -> list[str]:
    args = ["grep", "-n", "-I", "-F" if fijo else "-E", "-e", patron, ref, "--", *rutas]
    return [l.split(":", 1)[1] if l.startswith(ref + ":") else l for l in git(repo, *args).splitlines()]


def desvios(repos: dict[str, tuple[Path, str]]) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    i18n = ["packages/i18n/src/*/common.json"]
    arb = ["worker-app/lib/l10n/app_*.arb"]
    for nombre, (repo, ref) in repos.items():
        fuentes = ["apps/web/src", "worker-app/lib"]
        out[f"Texto con punto «●» al inicio · {nombre} (a revisar: chips no; leyendas e indicadores sueltos sí)"] = buscar(
            repo, ref, "\"● |'● |>● ", *fuentes, *i18n, *arb)
        out[f"Botón o texto que termina en flecha «→» · {nombre}"] = buscar(
            repo, ref, r"→\"|→\s*</(button|Link|a)>|→'\)", *i18n, *arb, *fuentes)
        out[f"Placeholder o hint que termina en «…» · {nombre}"] = buscar(
            repo, ref, r"\"[A-Za-z]*([Pp]laceholder|[Bb]uscar|[Ss]earch|[Hh]int)[A-Za-z]*\": \".*(…|\.\.\.)\"", *i18n, *arb)
        if nombre == "campisoft":
            out["`campy-blue` en campisoft (no existe: va `action-blue`)"] = buscar(repo, ref, "campy-blue", "apps/web/src", fijo=True)
            out["Material prohibido en pantallas nuevas o rediseñadas de la Worker App (`AlertDialog`, `SnackBar`, `Card(`, `elevation:`)"] = [
                l for l in buscar(repo, ref, r"\b(AlertDialog|SnackBar|Card)\(|elevation: [1-9]", "worker-app/lib")
                if "/l10n/" not in l
            ]
    return out


def minusculas(repo: Path, ref: str, ruta: str) -> list[str]:
    """Textos en español que empiezan con minúscula (muchos son continuaciones: revisar, no corregir a ciegas)."""
    try:
        datos = json.loads(git(repo, "show", f"{ref}:{ruta}") or "{}")
    except json.JSONDecodeError:
        return []
    res: list[str] = []

    def recorrer(nodo: object, clave: str) -> None:
        if isinstance(nodo, dict):
            for k, v in nodo.items():
                if not k.startswith("@"):
                    recorrer(v, f"{clave}.{k}" if clave else k)
        elif isinstance(nodo, str) and re.match(r"[a-záéíóúñ]", nodo):
            res.append(f"{clave} = {nodo[:50]}")

    recorrer(datos, "")
    return res


def frescura(repos: dict[str, tuple[Path, str]], desde: str | None) -> dict[str, list[str]]:
    if not desde:
        return {}
    out = {}
    for nombre, (repo, ref) in repos.items():
        out[nombre] = git(repo, "log", f"--since={desde}", "--format=%h %ad %s", "--date=short", ref, "--",
                          *VIGILADAS.get(nombre, [])).splitlines()
    return out


def pendientes() -> list[str]:
    p = SKILL / "references" / "aprendizajes.md"
    if not p.exists():
        return ["(no existe references/aprendizajes.md)"]
    return [l.strip()[2:] for l in p.read_text(encoding="utf-8").splitlines()
            if l.startswith("- ") and "· [pendiente] ·" in l.lower()]


def seccion(titulo: str, filas: list[str], vacio: str = "Nada.", tope: int = 25) -> str:
    cuerpo = "\n".join(f"- {f}" for f in filas[:tope]) if filas else f"- {vacio}"
    if len(filas) > tope:
        cuerpo += f"\n- … y {len(filas) - tope} más."
    return f"### {titulo} ({len(filas)})\n{cuerpo}\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--campisoft", type=Path, default=Path(os.environ.get("CAMPISOFT", HOME / "Escritorio/laburo/campisoft")))
    ap.add_argument("--campyprov", type=Path, default=Path(os.environ.get("CAMPYPROV", HOME / "Escritorio/laburo/campyprov")))
    ap.add_argument("--campisoft-ref", default="origin/main")
    ap.add_argument("--campyprov-ref", default="origin/main")
    ap.add_argument("--sin-fetch", action="store_true")
    a = ap.parse_args()

    repos = {"campisoft": (a.campisoft, a.campisoft_ref), "campyprov": (a.campyprov, a.campyprov_ref)}
    for repo, ref in repos.values():
        if not a.sin_fetch and ref.startswith("origin/"):
            subprocess.run(["git", "-C", str(repo), "fetch", "-q", "origin", ref.split("/", 1)[1]], capture_output=True)

    docs = textos_skill()
    arbol = [f for repo, ref in repos.values() for f in archivos(repo, ref)]
    if not arbol:
        print("No pude leer los repos: revisá --campisoft / --campyprov.", file=sys.stderr)
        return 0
    desde = fecha_revision(docs.get(SKILL / "SKILL.md", ""))

    print("# Autoevaluación de campy-diseno\n")
    print(f"Repos: campisoft `{a.campisoft_ref}`, campyprov `{a.campyprov_ref}`. Última revisión de la skill: {desde or 'sin fecha'}.\n")
    print("## 1. Rutas que cita la skill y no existen\n")
    print(seccion("Rutas", rutas_faltantes(docs, arbol)))
    print("## 2. Desvíos de reglas en el código (reportar al usuario; no se corrigen sin pedirlo)\n")
    for titulo, filas in desvios(repos).items():
        print(seccion(titulo, filas, tope=12))
    print(seccion("Worker App: textos en español con minúscula inicial (revisar: las continuaciones de frase van en minúscula)",
                  minusculas(*repos["campisoft"], "worker-app/lib/l10n/app_es.arb"), tope=20))
    web = len(minusculas(*repos["campisoft"], "packages/i18n/src/es/common.json"))
    print(f"Web (campisoft): {web} textos en español con minúscula inicial; la mayoría son pedazos de frase. Revisar solo los de la pantalla que se toca.\n")
    print("## 3. Pantallas de referencia que cambiaron desde la última revisión\n")
    for nombre, filas in frescura(repos, desde).items():
        print(seccion(f"{nombre}", filas, vacio="Sin cambios."))
    print("## 4. Aprendizajes pendientes\n")
    print(seccion("Pendientes", pendientes()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
