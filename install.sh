#!/usr/bin/env bash
# Instala la skill campy-diseno en modo editable: un clon de este repo enlazado en
# ~/.claude/skills/campy-diseno. Así la skill puede anotar lo que aprende y esos cambios
# se commitean al repo. (Instalada como plugin queda en una caché de solo lectura.)
#
#   git clone https://github.com/ajuarez-campy/campy-diseno.git ~/.claude/campy-diseno && ~/.claude/campy-diseno/install.sh
#   ./install.sh                      # desde un clon ya hecho (usa ese clon)
#   CAMPY_DISENO_DIR=~/otra/ruta ./install.sh
set -euo pipefail

REPO="${CAMPY_DISENO_REPO:-https://github.com/ajuarez-campy/campy-diseno.git}"
DIR="${CAMPY_DISENO_DIR:-$HOME/.claude/campy-diseno}"
DESTINO="$HOME/.claude/skills/campy-diseno"

# Si se corre desde un clon, se usa ese clon.
AQUI="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd || true)"
if [ -n "$AQUI" ] && [ -f "$AQUI/skills/campy-diseno/SKILL.md" ]; then
  DIR="$AQUI"
elif [ -d "$DIR/.git" ]; then
  git -C "$DIR" pull --ff-only
else
  git clone "$REPO" "$DIR"
fi

mkdir -p "$HOME/.claude/skills"
if [ -L "$DESTINO" ]; then
  rm "$DESTINO"
elif [ -e "$DESTINO" ]; then
  # El respaldo va fuera de ~/.claude/skills: si no, Claude Code lo cargaría como otra skill.
  RESPALDO="$HOME/.claude/campy-diseno.respaldo-$(date +%Y%m%d%H%M%S)"
  mv "$DESTINO" "$RESPALDO"
  echo "Había una copia suelta de la skill: quedó en $RESPALDO"
fi
ln -s "$DIR/skills/campy-diseno" "$DESTINO"
echo "Listo: $DESTINO → $DIR/skills/campy-diseno"
echo "Abrí una sesión nueva de Claude Code (o /reload-plugins) para que la tome."
