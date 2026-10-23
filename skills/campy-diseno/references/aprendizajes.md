# Registro de aprendizajes

La memoria de la skill: cada corrección o decisión de diseño del usuario y cada desvío que encontró la
autoevaluación queda acá **en el momento**, con fecha y origen, y se lleva a la regla o pieza que corresponde en el
mismo turno. Lo que todavía no se decidió queda `[pendiente]` y lo lista `scripts/autoevaluar.py` cada vez que corre.

Formato: `AAAA-MM-DD · [estado] · qué se aprendió · origen · dónde quedó`.
Estados: `[incorporado]` (ya está en la skill), `[pendiente]` (falta que el usuario decida o falta incorporarlo),
`[descartado]` (se probó y no va, con el porqué).

## Entradas

- 2026-10-21 · [incorporado] · ¿Los pedazos que van después de « · » empiezan con mayúscula? («4/6 · faltan ítems», «Tablet · calibración vencida»). Las continuaciones de frase («3 de 4 personas», «Actualizado hace 5 min») siguen en minúscula · pregunta abierta a Agustín · SKILL.md › Reglas › mayúscula inicial → decidido por Agustín 21/10: Sí: lo que va después de « · » empieza con mayúscula · SKILL.md regla 15
- 2026-10-21 · [incorporado] · Revisión completa contra el código: Worker App (PR #217), dashboard de Food (campyprov `origin/main`) y Shift (campisoft `origin/main`) · pedido de Agustín · SKILL.md, mobile.md, piezas.md, tokens.md, estados.md, graficos.md, checklist.md
- 2026-10-21 · [incorporado] · Servicios, Mi Área y Cori sin cabecera; regla 14 corregida · decisiones de Agustín del 21/10 · SKILL.md regla 14, mobile.md › Composición
- 2026-10-21 · [incorporado] · Mayúscula inicial en todo texto; códigos de idioma enteros en mayúscula («ES») · Agustín · SKILL.md regla 15
- 2026-10-21 · [incorporado] · Barra inferior que se contrae con Cori arriba, vuelo de Cori, CoriVivo, arranque con el aro, BotonAlAro, ingreso sin QR ni servidor · Agustín · mobile.md › Composición
- 2026-10-21 · [incorporado] · Animaciones: respetan «reducir movimiento» y nunca traban la navegación (la barra quedó trabada por una recarga en caliente) · hallazgo del 21/10 · SKILL.md regla 17
- 2026-10-21 · [incorporado] · El dashboard de Food de Operators (campisoft) no sigue [F]: no es referencia · revisión · SKILL.md › referencias
- 2026-10-21 · [incorporado] · Cobertura e Histograma de Shift están ocultas y con estilo viejo: no son referencia; Convenios salió de las pestañas y entró Horarios · revisión · piezas.md › Pestañas de módulo
- 2026-10-21 · [incorporado] · Título de pestaña interna: Shift usa 28 px (Solicitudes, Calendario, DAE, Colores) y 26 px (Asignaciones, Esquemas, Horarios) · revisión · tokens.md › Choques → decidido por Agustín 21/10: 27 px para el título de pestaña interna · SKILL.md, tokens.md
- 2026-10-21 · [incorporado] · Encabezado de tabla: [D] y [F] 12 px; Shift 11 px · revisión · tokens.md › Choques → decidido por Agustín 21/10: 12 px; los 11 px de Shift son desvío · tokens.md
- 2026-10-21 · [incorporado] · Sub-pestañas de segundo nivel: tres formas en Shift (tarjeta con `bg-blue-50`, riel gris de Horarios, subrayado de [P]) · revisión · tokens.md › Choques → decidido por Agustín 21/10: Depende del módulo en que se trabaja · SKILL.md regla 18
- 2026-10-21 · [incorporado] · Selector de vista: píldora de [F] o rectangular con la activa azul de Calendario · revisión · tokens.md › Choques → decidido por Agustín 21/10: Depende del módulo · SKILL.md regla 18
- 2026-10-21 · [incorporado] · Violeta para la «versión» de un esquema de Shift (¿cuarto uso permitido?) · revisión · tokens.md › Choques → decidido por Agustín 21/10: Sí · SKILL.md regla 6
- 2026-10-21 · [incorporado] · Íconos de los KPI de [F] en tonos decorativos (violeta, teal, sky) frente a la regla 6 · revisión · tokens.md › Choques → decidido por Agustín 21/10: Sí, se permiten · SKILL.md regla 6
- 2026-10-21 · [incorporado] · ¿Una fila entera que navega (alertas, «Ver todas») puede llevar chevron? La regla 11 es para botones · revisión · tokens.md › Choques → decidido por Agustín 21/10: Sí, lleva chevron · SKILL.md regla 11
- 2026-10-21 · [incorporado] · Mes en minúscula en fechas largas de la web («15 de octubre») frente a la mayúscula inicial · revisión · tokens.md › Choques → decidido por Agustín 21/10: Mes con mayúscula también en la web · SKILL.md regla 15
- 2026-10-21 · [incorporado] · Rojo para un número que baja en [P] (sigue abierto desde el 17/10) · revisión · tokens.md › Choques → decidido por Agustín 21/10: Sí, va en rojo · SKILL.md regla 6
- 2026-10-21 · [descartado] · Desvíos que el script encontró en el código (chips con «●», ~230 botones con «→», ~80 placeholders con «…», `AlertDialog`/`SnackBar` en la app): ¿se corrigen en un PR aparte? · autoevaluar.py · — → Agustín 21/10: no se corrigen; solo se reportan

- 2026-10-23 · [incorporado] · Con «Mi Área en camino» no se muestra nada más en la pestaña (quedaba el chip «Mucama» suelto arriba: «está horrible») · Agustín · mobile.md › Composición › «En camino»
