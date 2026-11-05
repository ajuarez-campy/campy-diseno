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
- 2026-10-26 · [incorporado] · Worker App: fechas con el mes y el día enteros (no «Oct», «Lun»); cortos solo los encabezados de calendario y la tarjeta del turno del Inicio · Agustín · mobile.md
- 2026-10-26 · [incorporado] · Worker App, cabecera del Inicio sin «Hoy»: saludo y fecha entera · Agustín · mobile.md
- 2026-10-26 · [incorporado] · Worker App, Inicio: tarjeta del turno inmersiva con la foto del campamento y línea de tiempo Hoy · Ingreso · Salida (hora debajo de la fecha) · Agustín · mobile.md
- 2026-10-26 · [incorporado] · Worker App, Servicios: widgets de estado (Apple Home) en bloques de color lleno, tono 700 del color de servicio y pictograma blanco sin recuadro; se toca el bloque entero; sin buscador · Agustín · mobile.md
- 2026-10-26 · [incorporado] · Worker App, Inicio «Para vos»: a todo el ancho; Mi alojamiento como llave (azul lleno, número grande), Lavandería como seguimiento de 4 pasos en azul, Transporte y viaje del chofer sin botón (se toca la tarjeta) · Agustín · mobile.md
- 2026-10-26 · [incorporado] · Worker App, «Para vos»: Transporte fijo + filas deslizables «Hoy» y «Tu estadía», tarjetas vivas en el color fuerte de cada servicio (reemplaza todas en azul) · Agustín · mobile.md
- 2026-10-26 · [incorporado] · Worker App, «Para vos»: un color distinto por tarjeta (Alojamiento azul marino, Ayuda fucsia) y una sola tarjeta de comida con la vianda adentro · Agustín · mobile.md
- 2026-10-26 · [incorporado] · Worker App, SOS: fuera del Inicio y redondo en las otras pestañas y en Cori · Agustín · mobile.md
- 2026-10-26 · [incorporado] · Worker App, Inicio: «¿Necesitás ayuda urgente?» al pie sin la burbuja del SOS; la tarjeta entera abre la emergencia · Agustín · mobile.md
- 2026-10-26 · [incorporado] · Worker App, Inicio: ninguna tarjeta con botón ni flecha; se toca la tarjeta (sale «Ver alojamiento» de la llave y la flecha de ayuda urgente) · Agustín · mobile.md
- 2026-10-26 · [incorporado] · Worker App: ninguna tarjeta con botón ni flecha para navegar, en toda la app · Agustín · SKILL.md regla 11
- 2026-10-26 · [incorporado] · Worker App: sin chevrons ni textos-enlace en filas y tarjetas (reemplaza el chevron de fila que navega del 21/10 en la app) · Agustín · SKILL.md regla 11
- 2026-10-26 · [incorporado] · Worker App: «>» solo en filas de un listado que navegan; tarjetas sueltas sin flecha ni botón · Agustín · SKILL.md regla 11
- 2026-10-26 · [incorporado] · Rediseño de Mateo en Operators (PR #237): chip de esquema en una sola píldora pastel azul, avatares «cremita» por persona, paginación sin selector de filas y esquemas de roster sin «vN»; en Shift manda Operators, así que vale para Providers · Agustín · piezas.md (Shift)
- 2026-10-26 · [incorporado] · Providers separa el menú en «Rosters» y «Turnos» como Operators, y Turnos conserva Excepciones · Agustín · SKILL.md regla 18
- 2026-10-26 · [incorporado] · Worker App: tarjetas de color en pastel (`pastelDe`), dato en tinta y acento en el tono fuerte; reemplaza el lleno con letra blanca en Servicios, «Para vos» y Mi Área · Agustín · mobile.md (Servicios, «Para vos»)
- 2026-10-26 · [incorporado] · Nada de anotaciones de relleno ni datos repetidos (quién cargó, a cargo de quién, aclaraciones del sistema): se sacan · Agustín · SKILL.md regla 19
- 2026-10-26 · [incorporado] · Botones sin «+» también en Shift y Turnos: «Nueva asignación», no «+ Nueva asignación»; el «+» de Operators es un desvío a corregir cuando se toque · Agustín · SKILL.md regla 11
- 2026-10-26 · [incorporado] · Turnos de Providers conserva sus funciones nativas aunque Operators las sacó (esquemas rotativos y fijos, reglas por dotación o puesto, editar vigencia y contraturno, reactivar esquemas), con el diseño nuevo · Agustín · SKILL.md regla 18
- 2026-10-26 · [incorporado] · Tarjetas de servicio en los colores de Cori (aro del logo): Transporte cielo, Comedor amarillo, Alojamiento coral, Lavandería lima, Bienestar y Ayuda lavanda; acento = el tono oscurecido. Conectividad sale de Servicios · Agustín · mobile.md
- 2026-10-26 · [incorporado] · Worker App: el SOS está solo en el Inicio («¿Necesitás ayuda urgente?»); sale la burbuja flotante del resto de las pantallas · Agustín · mobile.md (Dudas › SOS)
- 2026-10-28 · [incorporado] · Worker App: el azul de las pantallas de servicio es un cielo que sigue la hora (noche con estrellas y luna, amanecer y atardecer con resplandor cálido, mañana más clara, mediodía el azul Campy), como luz sobre la escena y no como fondo (los PNG tienen partes semitransparentes); la franja del mosaico Comedor avanza con la hora dentro de la comida de ahora · Agustín · `worker-app/lib/widgets/cielo.dart`, `FranjaDia` en `mosaicos.dart`; mobile.md › Vigente al 4/11 › Pantallas azules
- 2026-11-02 · [incorporado] · Worker App: toda fila que hay que distinguir como tocable entre lo que solo informa lleva el «>» gris («Punto de encuentro» de Mi traslado, solicitudes de Mi roster). Se probó y se descartó reemplazarlo por una miniatura del mapa, una pastilla, un círculo o un fondo · Agustín · `FilaServicio` en `servicio_azul.dart`; SKILL.md regla 11
- 2026-11-03 · [incorporado] · Worker App, hojas de servicio: el dato principal va en el azul bajo el título («Habitación 12», «6 prendas listas») y la hoja va sin ícono ni encabezado; dentro, los datos se ordenan por importancia con `DosDatos` (dos datos lado a lado con línea fina, grande 28 para lo que se busca primero y 17 para lo de lectura) y bloques con título de 15 en negrita («Estadía», «Incidencias», «Mi cupo»); el estado de una fila va a la derecha en su color. Ninguna fila destacada lleva rótulo «Ahora» ni «Sigue» · Agustín · `servicio_azul.dart` (`DosDatos`), `hospedaje.dart`, `lavanderia.dart`, `comedor.dart`; mobile.md › Vigente al 4/11 › Pantallas azules
- 2026-11-03 · [incorporado] · Worker App: negrita solo para los títulos importantes (título de bloque, el dato grande que se busca primero); rótulos, valores de lectura, filas y estados van sin negrita (w400/w500) · Agustín · `DosDatos` en `servicio_azul.dart`, `lavanderia.dart`; SKILL.md regla 26

- 2026-11-04 · [incorporado] · Puesta al día con todo lo decidido del 27/10 al 4/11 (vault y memoria): sección nueva «Vigente al 4/11/2026» en mobile.md y reglas 20 a 30 en SKILL.md; filas viejas de mobile.md marcadas como reemplazadas; se sacaron los párrafos repetidos de las reglas 3 y 8 y del checklist · pedido de Agustín · SKILL.md, mobile.md, checklist.md
- 2026-10-27 · [descartado] · Equilibrio visual de la app: direcciones A (calma), B (color) y C (un protagonista) · Agustín: «busquemos nueva inspiración» · vault › Hallazgo - Desequilibrio visual; se eligió D (pases) para el Inicio y S2 (mosaicos) para Servicios
- 2026-10-28 · [incorporado] · Servicios en mosaicos blancos con el ícono en un cuadrado azul Campy y su dato grande; un solo color, nada de multicolor (reemplaza el pastel y los colores de Cori del 26/10 y los de KPI del 27/10) · Agustín · mobile.md › Vigente › Servicios, SKILL.md regla 6
- 2026-10-28 · [incorporado] · Texto completo: sin «...», sin paréntesis, nada cortado; lo que no entra baja de línea · Agustín · SKILL.md regla 20
- 2026-10-28 · [incorporado] · Pop-ups con título corto y una oración de ~60 caracteres, para todo pop-up nuevo · Agustín · SKILL.md regla 21
- 2026-10-28 · [incorporado] · Pantallas azules: el arco con dos pines y la línea punteada del piso solo en Transporte; parábola solo para el avión; mismo alto de azul y de hoja en las seis (`ComposicionAzul`) · Agustín · mobile.md › Pantallas azules
- 2026-10-28 · [incorporado] · Un QR por persona: la credencial sirve para todo; nunca QR por orden, viaje o reserva · Agustín · SKILL.md regla 30
- 2026-10-28 · [incorporado] · La app marca y mira; la gestión y los procesos administrativos son de la web · Agustín · SKILL.md regla 28
- 2026-10-29 · [incorporado] · Nunca flechas de ruta («→») entre origen y destino: «A a B» o `Recorrido` · Agustín · SKILL.md regla 23
- 2026-10-29 · [incorporado] · Horas con «hs» («14:00hs») y fecha entera («Viernes 6 de Noviembre») en Mi traslado · Agustín · SKILL.md regla 24 → decidido por Agustín 4/11: es regla de toda la Worker App
- 2026-10-29 · [incorporado] · La barra de abajo de la app no se cambia aunque una maqueta dibuje otra · Agustín · SKILL.md regla 29
- 2026-10-29 · [incorporado] · Lo encerrado en rojo en una captura sin texto es para sacar; con texto, manda el texto · Agustín · SKILL.md › Cómo se decide el diseño en Campy
- 2026-10-29 · [incorporado] · Check In sin «Validación» y confirmación deslizando; Check Out con el mismo formato de hoja · Agustín · mobile.md › Por servicio
- 2026-10-29 · [incorporado] · Arranque en navy con el logo (iOS y Android) y brillo de los colores del aro al abrir · Agustín · mobile.md › Escáner, login y arranque
- 2026-10-30 · [incorporado] · Una escala de letra (`LetraCampy`) para toda la app menos el login; letra del teléfono de 0,85 a 1,5 (reemplaza 1,0–1,1) · Agustín · SKILL.md regla 16
- 2026-10-30 · [incorporado] · Inicio = tablero del trabajador (roster, Jornada, Traslado); lo de cada servicio va a Servicios · Agustín · mobile.md › Inicio
- 2026-10-30 · [incorporado] · Tarjetas Jornada y Traslado del Inicio con el mismo esqueleto «Rótulo · estado», dos columnas y sin círculos ni «Registrada»/«Pendiente» · Agustín · mobile.md › Inicio
- 2026-10-30 · [incorporado] · Ayuda urgente en la cabecera del Inicio, a la izquierda de la campana · Agustín · SKILL.md regla 14
- 2026-10-30 · [incorporado] · Escala de azules para lo que avanza (`azulEscala1..3`) · Agustín · SKILL.md regla 6, mobile.md › Color
- 2026-10-30 · [incorporado] · Calendario de Mi roster: en sitio azul Campy, descanso gris, hoy con círculo, avión que sube o baja · Agustín · mobile.md › Color
- 2026-10-30 · [incorporado] · Un solo escáner de QR con velo navy, ventana con esquinas y brillo azul · Agustín · mobile.md › Escáner
- 2026-10-30 · [incorporado] · Login: título más grande con textura topográfica y una sola entrada «¿No podés ingresar?»; sin «Mantener mi sesión» ni «Contactar a Soporte» · Agustín · mobile.md › Login
- 2026-10-30 · [incorporado] · Opciones de un pop-up que llevan al paso siguiente sin nada a la derecha · Agustín · SKILL.md regla 11
- 2026-10-30 · [incorporado] · Mis solicitudes: lista simple con la palabra del estado en su color, no chat · Agustín · mobile.md › Mi roster
- 2026-10-31 · [incorporado] · Sin zócalos (barra de color en el borde izquierdo) en ninguna tarjeta; reemplaza la barra de la crítica de impeccable del 30/10 · Agustín · SKILL.md regla 25
- 2026-10-31 · [incorporado] · Mi traslado: grilla de dos columnas sin recuadros de color ni nombre del pasajero; pastilla amarilla en pastel con la patente sola · Agustín · mobile.md › Por servicio
- 2026-11-01 · [incorporado] · Volver en dos formas según el fondo (círculo blanco sobre claro, flecha blanca sobre azul o navy) · Agustín · SKILL.md regla 14
- 2026-11-01 · [incorporado] · Cabecera del Inicio: nombre arriba grande y saludo debajo chico · Agustín · SKILL.md regla 14
- 2026-11-01 · [incorporado] · Credencial de servicio tipo Wallet con cara de credencial (no de pase), sin lo que repite la hoja · Agustín · mobile.md › Pantallas azules
- 2026-11-01 · [incorporado] · La hoja de las pantallas azules no sube sola ni más allá de 111 px bajo el título · Agustín · mobile.md › Pantallas azules
- 2026-11-01 · [incorporado] · Cori: un solo botón micrófono/enviar como WhatsApp; sube sin salto final · Agustín · mobile.md › Barra de abajo y Cori
- 2026-11-02 · [incorporado] · Todo mensaje emergente es un pop-up de Campy (`avisoCampy`), nunca banner ni `SnackBar` · Agustín · SKILL.md regla 22
- 2026-11-02 · [incorporado] · Mismo formato de pantalla de servicio en todos los perfiles (el chofer con el `ArcoRuta` del pasajero); reusar, no copiar · Agustín · SKILL.md regla 27
- 2026-11-02 · [incorporado] · Mi Área con un diseño global: secciones con título y carrusel de `TarjetaCarrusel`; urgente rojo y primero · Agustín · mobile.md › Mi Área
- 2026-11-02 · [incorporado] · Notificaciones como buzón de hechos; hora sin píldora, chica y gris · Agustín · mobile.md › Notificaciones
- 2026-11-02 · [incorporado] · Comedor rediseñado: plato en el azul, Mi vianda y Mis preferencias en pop-up, una sola puerta para pedir un cambio · Agustín · mobile.md › Por servicio
- 2026-11-02 · [pendiente] · Rediseñar la OT entera (`ot.dart`) con maqueta antes de Flutter · Agustín · mobile.md › Mi Área
- 2026-11-03 · [incorporado] · Jornadas en lista de a 7 días (sin calendario propio, sin paginación «‹ 1 2 3 ›», sin «Sin marca») · Agustín · mobile.md › Mi roster
- 2026-11-03 · [incorporado] · Lavandería: «Mi cupo» sin barra, «?» de ayuda con pop-up de una oración, incidencias con `>` y detalle en pop-up · Agustín · mobile.md › Por servicio, SKILL.md regla 13
- 2026-11-03 · [incorporado] · Check In: fechas de la estadía como línea de tiempo (`LineaEstadia`); sin la pastilla «Alojamiento activo» · Agustín · mobile.md › Por servicio
- 2026-11-03 · [incorporado] · Animaciones de referencia (carpeta campy-animations) traducidas a código: QR escaneado y partida del viaje; Rive descartado · Agustín · SKILL.md › Cómo se decide el diseño en Campy, mobile.md
- 2026-11-04 · [incorporado] · El supervisor sí resuelve y gestiona desde la app (cambia la regla del 2/11) · Agustín · SKILL.md regla 28
- 2026-11-04 · [incorporado] · Lo que falló y sigue abierto sale en un pop-up al entrar a la pantalla, no en un recuadro rojo en la hoja · Agustín · SKILL.md regla 22
- 2026-11-04 · [incorporado] · «hs» en toda hora y fecha entera en toda la Worker App (antes solo en Mi traslado); la tarjeta del turno ya no usa la fecha corta · Agustín · SKILL.md regla 24 · [pendiente] si la web también lleva «hs»
- 2026-11-04 · [incorporado] · La skill es también para el equipo: sin rutas ni enlaces personales; «Cómo se decide el diseño en Campy»; lo que decide otra persona queda `[pendiente: confirmar con Agustín]` · Agustín · SKILL.md, mobile.md, README.md
