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
- 2026-10-23 · [incorporado] · Las barras de avance (la del ciclo en el Inicio y toda barra nueva) van del navy del fondo del botón del QR (`CampyColors.navy`), no del azul · Agustín · mobile.md › Radios › «Barra de avance (color)»
- 2026-10-23 · [incorporado] · El número del porcentaje de una barra («93%» de «Mi estadía») va del mismo navy que la barra · Agustín · mobile.md › «Barra de avance (color)»
- 2026-10-23 · [incorporado] · Mi QR (credencial): nombre, puesto, rótulos (DNI, Empresa), valores y «Se renueva en» van en MAYÚSCULAS; excepción a la mayúscula inicial · Agustín · mi_qr.dart
- 2026-10-23 · [incorporado] · Notificaciones (app): sin chevron ni «Abrir» en las filas (la fila entera abre); deslizar a la izquierda borra, salvo las urgentes; sin filtro; la campanita del aviso de acciones con borde ámbar (`IconoRecuadro(borde:)`) · Agustín · notificaciones.dart
- 2026-10-24 · [incorporado] · Shift de Providers con la visual de Shift de Operators: cabecera «Shift» con el sitio debajo y pestañas de módulo en píldora azul (Shift queda distinto al resto de Providers, que usa `SolapasModulo`) · Agustín · SKILL.md regla 18
- 2026-10-24 · [incorporado] · Choque «burbujas redondas» frente a la regla 18: en Shift (de los dos productos) mandan las formas de Shift de Operators (Combobox de filtros `rounded-input`, sub-pestañas en tarjeta con radio 9, selector del calendario rectangular, botones de ícono radio 8); la píldora queda para los demás módulos · Agustín · SKILL.md regla 18
- 2026-10-24 · [incorporado] · Cada pestaña de Shift lleva subtítulo bajo el título (una oración simple, como Operators) · Agustín · SKILL.md regla 18
- 2026-10-24 · [incorporado] · Roster del contratista: lista + detalle (como DAE/DAP y Asignaciones) en vez del panel lateral, con 4 KPIs de estado · Agustín · SKILL.md regla 18
- 2026-10-26 · [incorporado] · Worker App, cabecera del Inicio: «Hoy» en una línea y la fecha entera abajo («Lunes, 26 de Octubre»); la campana con el borde amarillo (ámbar), como la de Notificaciones · Agustín · mobile.md
- 2026-10-26 · [incorporado] · Worker App, tarjeta del turno del Inicio (Próximo turno y Mi estadía): el azul pasa al navy del botón del QR (ícono, «En N días», duración, días restantes) · Agustín · mobile.md
- 2026-10-26 · [incorporado] · La campana del Inicio va ámbar entera: el círculo y el dibujo, no solo el borde · Agustín · mobile.md
- 2026-10-26 · [incorporado] · Worker App: advertencias, urgencias, avisos sin conexión y estados pendientes en el rojo de «Cerrar sesión», no en ámbar; las campanitas siguen ámbar · Agustín · SKILL.md regla 6, mobile.md · [pendiente] si vale también para la web
- 2026-10-26 · [incorporado] · Worker App, Inicio: todas las tarjetas en el azul Campy (el de «Transporte»); la del turno deja el navy, barra incluida. Reemplaza la tarjeta del turno en navy (mismo día) y las barras en navy (23/10). El botón del QR sigue navy · Agustín · mobile.md · [pendiente] color de barras fuera del Inicio
- 2026-10-26 · [incorporado] · Worker App, Inicio: el botón del QR pasa al azul Campy (antes navy), dibujo blanco · Agustín · mobile.md
- 2026-10-26 · [incorporado] · Worker App, Inicio: «Transporte» en formato pase de embarque (maqueta A del 24/10), botón en azul Campy; el chofer con el mismo formato · Agustín · mobile.md
- 2026-10-26 · [incorporado] · Worker App, solicitudes abiertas: «Adjuntar foto» y a su derecha «Cancelar solicitud», en píldoras (`botonPildoraCampy`) · Agustín · mobile.md
