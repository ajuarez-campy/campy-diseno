# campy-diseno

Skill de Claude Code con el **sistema de diseño de Campy**: la web de For Operators y For Providers (`apps/web` en
campisoft y campyprov) y la Worker App en Flutter. Trae las tres pantallas de referencia (dashboard de Food,
planificación de Food y Shift), tipografía, colores, piezas de código, estados vacío/cargando/error, gráficos, la guía
de la app móvil, un checklist de revisión y las reglas que fue decidiendo el equipo.

Es una skill que **se autoevalúa y aprende**:

- `scripts/autoevaluar.py` compara la skill con el código actual (`origin/main` de los dos repos, sin tocar las copias
  de trabajo) y reporta rutas que ya no existen, desvíos de las reglas en el código, pantallas de referencia que
  cambiaron desde la última revisión y aprendizajes pendientes.
- `references/aprendizajes.md` guarda cada corrección o decisión de diseño con fecha y origen; la skill la lleva a la
  regla que corresponde en el mismo momento.

## Para el equipo

Esta skill es el **lineamiento de diseño de Campy**: lo que tiene que cumplir toda pantalla nueva o que se toque, en la
web y en la Worker App, la haga quien la haga. Lo define Agustín (líder de frontend).

- **Antes de diseñar o revisar una pantalla**, Claude la carga sola; si trabajás sin Claude, leé las «Reglas que no se
  negocian» de `skills/campy-diseno/SKILL.md` y, para la app, «Vigente al 4/11/2026» en `references/mobile.md`.
- **Revisar un PR de UI:** `references/checklist.md` (y el de la app en `mobile.md`).
- **Lo que no está, se acuerda antes de codificar.** Una vez acordado, quien lo trabajó lo suma a la skill: la regla
  o la pieza donde corresponde, y una línea en `references/aprendizajes.md` con la fecha y su nombre
  (`[D, nombre dd/mm/aaaa]`).
- **Para sumar un cambio a la skill:** con acceso de escritura, commit en español («Aprendizaje: …») y push; sin acceso,
  un fork y un PR.

## Instalación

El repo es público: para instalarla no hace falta cuenta ni acceso.

### Modo editable (recomendado: así la skill puede aprender)

```bash
git clone https://github.com/ajuarez-campy/campy-diseno.git ~/.claude/campy-diseno && ~/.claude/campy-diseno/install.sh
```

Deja el clon en `~/.claude/campy-diseno` y enlaza `~/.claude/skills/campy-diseno` a la skill (si había una copia
suelta, la guarda como respaldo fuera de `~/.claude/skills`). Para actualizar: `git -C ~/.claude/campy-diseno pull`.
Los aprendizajes quedan en ese clon; para subirlos hace falta acceso de escritura al repo (o un fork y un PR).

### Como plugin (solo usar)

En una sesión de Claude Code:

```
/plugin marketplace add ajuarez-campy/campy-diseno
/plugin install campy-diseno@campy-skills
```

Instalada así la skill queda en `~/.claude/plugins/cache/` y no se edita (se pisa en cada actualización): propone los
aprendizajes para que los subas al repo. Para recibir cambios: `/plugin` › Marketplaces › actualizar (o activar
la actualización automática).

## Uso

Claude Code la usa sola al crear, rediseñar o revisar pantallas de Campy, o cuando se pide «el diseño de Campy»,
«como el dashboard de Food», «como Shift». La autoevaluación se puede correr a mano:

```bash
cd ~/.claude/skills/campy-diseno
python3 scripts/autoevaluar.py                  # busca los clones en ~/Escritorio/laburo, ~, ~/code, ~/projects
CAMPISOFT=/ruta/campisoft CAMPYPROV=/ruta/campyprov python3 scripts/autoevaluar.py
python3 scripts/autoevaluar.py --campisoft /ruta/al/worktree --campisoft-ref HEAD   # mirar una rama
```

Necesita `python3` y `git`, y los dos repos de Campy clonados (son privados: el script solo los lee en tu máquina).

## Estructura

```
.claude-plugin/        manifiesto del plugin y marketplace (campy-skills)
skills/campy-diseno/
  SKILL.md             reglas, referencias y cómo aprende
  references/          tokens, piezas, estados, gráficos, app móvil, checklist, aprendizajes
  scripts/autoevaluar.py
install.sh             instalación en modo editable
```
