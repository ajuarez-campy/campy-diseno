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
- **Lo que no está, se pregunta** a Agustín antes de codificar. Lo que decide otra persona queda anotado como
  `[pendiente: confirmar con Agustín]` hasta que él lo confirme.
- **Para proponer un cambio a la skill:** rama propia y PR a este repo, con la decisión y su fecha en
  `references/aprendizajes.md`.

## Instalación

### Modo editable (recomendado: así la skill puede aprender)

```bash
gh repo clone ajuarez-campy/campy-diseno ~/.claude/campy-diseno && ~/.claude/campy-diseno/install.sh
```

Deja el clon en `~/.claude/campy-diseno` y enlaza `~/.claude/skills/campy-diseno` a la skill (si había una copia
suelta, la guarda como respaldo fuera de `~/.claude/skills`). Los aprendizajes
quedan en ese clon y se suben con `git commit` + `git push`. Para actualizar: `git -C ~/.claude/campy-diseno pull`. Como
el repo es privado, hace falta acceso a GitHub (`gh auth login` y `gh auth setup-git`, o SSH) y que el dueño te sume
como colaborador.

### Como plugin (solo usar)

En una sesión de Claude Code:

```
/plugin marketplace add ajuarez-campy/campy-diseno
/plugin install campy-diseno@campy-skills
```

Instalada así la skill queda en `~/.claude/plugins/cache/` y no se edita (se pisa en cada actualización): propone los
aprendizajes para que alguien los suba al repo. Para recibir cambios: `/plugin` › Marketplaces › actualizar (o activar
la actualización automática).

## Uso

Claude Code la usa sola al crear, rediseñar o revisar pantallas de Campy, o cuando se pide «el diseño de Campy»,
«como el dashboard de Food», «como Shift». La autoevaluación se puede correr a mano:

```bash
cd ~/.claude/skills/campy-diseno
python3 scripts/autoevaluar.py                  # por defecto busca ~/Escritorio/laburo/{campisoft,campyprov}
CAMPISOFT=/ruta/campisoft CAMPYPROV=/ruta/campyprov python3 scripts/autoevaluar.py
python3 scripts/autoevaluar.py --campisoft /ruta/al/worktree --campisoft-ref HEAD   # mirar una rama
```

Necesita `python3` y `git`, y los dos repos de Campy clonados.

## Estructura

```
.claude-plugin/        manifiesto del plugin y marketplace (campy-skills)
skills/campy-diseno/
  SKILL.md             reglas, referencias y cómo aprende
  references/          tokens, piezas, estados, gráficos, app móvil, checklist, aprendizajes
  scripts/autoevaluar.py
install.sh             instalación en modo editable
```
