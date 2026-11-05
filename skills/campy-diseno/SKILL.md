---
name: campy-diseno
description: Sistema de diseño del frontend de Campy (For Operators y For Providers, apps/web en campisoft y campyprov, y la Worker App Flutter en worker-app/, que debe ser un fiel reflejo de la web). Usar SIEMPRE antes de crear, rediseñar o revisar cualquier pantalla de la web o de la app móvil, tarjeta, tabla, formulario, gráfico, chip, botón, estado vacío o de carga de la web de Campy, y cuando el usuario pida «el diseño de Campy», «como el dashboard de Food», «como la planificación de Food», «como Shift», una revisión visual de UI o alinear una pantalla al patrón. Trae tipografía, colores de estado, tamaños, hover/foco/disabled, estados vacío/cargando/error, piezas de código de referencia, un checklist de revisión y una autoevaluación (scripts/autoevaluar.py + references/aprendizajes.md) para mantenerse al día con el código y con lo que decide el usuario.
---

# Diseño del frontend de Campy

Última revisión: 2026-11-04 (alineada con la Worker App de las ramas del 3 y 4/11, v1.53 a v1.62: pantallas azules
de servicio, Mi roster con Jornadas, Mi Área global, Comedor, Lavandería, Mi traslado y hotelería; el dashboard de Food
de campyprov y Shift de campisoft en `origin/main`). La actualiza «Cómo aprende esta skill», al final.

**Las referencias son tres pantallas** [D, Agustín 16/10/2026]. Marcan el lineamiento de **todo** el diseño de Campy
(web de los dos repos y Worker App). Ante cualquier conflicto (entre la maqueta móvil, otras pantallas web o esta
guía) mandan ellas:

| Origen | Pantalla | Ruta | Qué aporta |
|---|---|---|---|
| **[F]** | Dashboard de Food (campyprov) | `apps/web/src/features/food/FoodResumen.tsx` + `features/food/dashboard/` (`piezas.tsx`, `TarjetasPestana.tsx`, `arrastre.ts`, `logica.ts`) + `GraficoDemanda.tsx` | tarjetas con cabecera y número, mosaicos, gráficos y anillos, leyendas, barras con rótulo, alertas, vacío/carga/error de tarjeta, arrastre de tarjetas, KPI en celular |
| **[P]** | Planificación de Food (campyprov) | `apps/web/src/features/food/FoodPlanificacion.tsx` + `FoodModal.tsx`, `food-lib.tsx`, `components/ui/campy-ui.tsx` (`BarraFiltros`, `SolapasModulo`, `inputCls`), `components/ui/KpiCard.tsx` (`compacta`) | navegador de semana ‹ rango ›, **tira de días** (celdas de día seleccionables con total y estado), detalle del día con celdas de servicio, KPI compactos en fila de 5, sub-solapas subrayadas, barra de filtros con «Limpiar», tabla con fecha en dos líneas y «Ver más» por tandas, panel lateral de viabilidad con barras finas, franja de recomendación de IA, **modal de Food** (cabecera `campy-ink` con ícono), stepper ± y tarjetas de ajuste. **No tiene arrastre ni grilla de calendario**: el arrastre sale de [F] |
| **[S]** | Shift (campisoft) | `apps/web/src/features/shift/` (Solicitudes, Asignaciones, Calendario, Horarios, Esquemas, DAE, Colores; Cobertura e Histograma están ocultas y con estilo viejo: no son referencia) | botones, formularios, tablas con filtros adentro y acciones, pestañas de módulo en píldora (rutas con `NavLink`), lista + detalle, calendario, riel gris de Horarios, modales con `DrawerHeader`, paginación, buscador |

Las piezas de cada una están en [references/piezas.md](references/piezas.md) con su origen. **Las tres no coinciden
en todo** (título de pestaña interna, borde de chip, etiqueta e input, encabezado de tabla, sub-pestañas, rojo para deltas;
botón, cabecera de modal, chip con punto e `INFO_REQUERIDA` ya los decidió Agustín el 17/10/2026): esos choques están listados en
[references/tokens.md](references/tokens.md) › «Choques entre las tres referencias». Mientras Agustín no decida,
vale lo marcado [D] en esta guía; no se elige uno por cuenta propia.

**Lo que no se copia de [P]** aunque esté ahí, porque lo prohíbe una regla del proyecto (CLAUDE.md manda sobre el
diseño): `bloqueo(…)` de `food-lib.tsx:35` (deshabilita sin permiso; la regla 4 de abajo dice ocultar), la semana
calculada con `toISOString().slice(0, 10)` (`FoodPlanificacion.tsx:202`; usar `hoyLocalISO()`/fechas locales) y los
botones ‹ › sin `aria-label` (`FoodPlanificacion.tsx:215, 217`).

**El dashboard de Food de Operators** (campisoft `features/food/FoodResumen.tsx`) **no sigue [F]**: es el formato viejo
(sin `dashboard/`, `KpiCard` con zócalo, chips -200, gráfico verde y ámbar). No se toma como referencia; si se alinea,
se porta [F] sin las acciones operativas (Operators mira, mide y certifica).

Stack: React 18 + Tailwind 3 + lucide-react 0.408 + Recharts. Fuente Inter variable (ya cargada en
`index.css`). No es Next ni React 19.

## Worker App (móvil)

**Lo último de la app (27/10 al 4/11/2026)**, con el detalle en [references/mobile.md](references/mobile.md) › «Vigente al
4/11/2026» (manda sobre lo viejo de ese archivo): una escala de letra (`LetraCampy`) y la letra del teléfono de 0,85 a
1,5; **Inicio = tablero del trabajador** (turno con la foto, Jornada con marcar ingreso y salida, Traslado); **Servicios
en mosaicos blancos con un solo azul Campy**; cada servicio abre una **pantalla azul** (azul arriba con el dibujo y la luz
de la hora, hoja blanca abajo, credencial tipo Wallet al pie) armada con `PantallaServicioAzul`; **Mi Área con un diseño
global** (secciones con título y carrusel de tarjetas, igual para todos los roles); Mi roster con «Mi ciclo», «Jornadas» y
«Solicitudes»; avisos como **pop-up** (`avisoCampy`), nunca banner; un solo escáner de QR; volver en dos formas según el
fondo. Antes (19–21/10): barra inferior navy con corte en U bajo Cori, `CoriVivo`, `ArranqueCampy`, `BotonAlAro`, «en
camino» centrado.

**Contenedores de la app: blanco y secciones** [D, Agustín 17/10/2026]: la app NO copia el panel gris con
tarjetas blancas de la web (se veía «app vieja»). Fondo blanco; los bloques son secciones sin caja separadas por
una línea fina (`CampyCard` sin color); solo lo destacado (servicios, «Para vos», avisos, emergencia) va en
superficies tintadas de radio 16–20 sin borde ni sombra; pestañas en riel gris claro. Lo demás (tipografía, colores,
chips, botones, textos) sigue igual a la web.
**La Worker App es un fiel reflejo de la web** [D, 16/10/2026]: misma tipografía (Inter), mismos colores, mismos
bordes redondeados y sombras, mismos chips, y los mismos estilos y textos en avisos, popups, estados vacíos
(«Sin datos todavía»), errores y cargas. Un solo diseño para todos los roles y fases. Equivalencias Flutter, piezas
propias (`widgets/ui.dart`), prohibidos de Material, checklist y la auditoría de Move/Shift (16/10) en
[references/mobile.md](references/mobile.md). En la app la maqueta decide la composición (qué bloques y en qué orden)
solo donde las tres referencias no dicen nada; en los valores mandan las tres referencias.

## Cómo usar esta skill

- **Construir UI:** leé las reglas de abajo y copiá la pieza que corresponda de
  [references/piezas.md](references/piezas.md). Los valores exactos están en
  [references/tokens.md](references/tokens.md); los estados en [references/estados.md](references/estados.md);
  los gráficos en [references/graficos.md](references/graficos.md).
- **Revisar un cambio de UI:** recorré [references/checklist.md](references/checklist.md) sobre el diff y
  reportá cada desvío con `archivo:línea`, la regla y la clase correcta.
- **Algo que no está acá** (un patrón nuevo, o dos estilos que no cubre la guía): preguntale al usuario antes
  de inventar uno y, si lo decide, agregalo a esta skill (ver «Cómo aprende esta skill»).

**Cómo se decide el diseño en Campy** (para todo el equipo):
- **El lineamiento lo define Agustín** (líder de frontend). Las reglas marcadas `[D, Agustín dd/mm/aaaa]` ya están
  decididas y valen para todos: no se discuten en un PR ni se cambian por gusto. Si una regla te traba, se le plantea a él.
- **Lo que no está en la skill se pregunta antes de codificar**, no se inventa ni se copia de otra pantalla que «se ve
  parecida». Lo que él decide se suma a la skill (ver «Cómo aprende esta skill»).
- **Maqueta antes de código** cuando cambia la composición de una pantalla (qué bloques, en qué orden): dos o tres
  variantes en HTML para que Agustín elija; recién después se pasa a React o a Flutter. Los ajustes chicos (un color,
  un texto, un margen) van directo.
- **Referencias visuales de afuera** (otras apps, GIF o videos de animaciones): se adaptan a Campy (sus colores, su
  letra y estas reglas) y se traducen a código propio (`CustomPainter`/`AnimationController` en la app); nunca se copian
  ni se embeben. Rive se probó y se descartó (3/11/2026). Los dibujos de los servicios son los de
  `worker-app/assets/ilustraciones/`: no se dibujan vectores nuevos sin pedirlo.
- **Una captura con algo encerrado en rojo y sin texto** quiere decir «sacar esto» (con sus claves de idioma, que quedan
  huérfanas); si la marca viene con un texto, manda el texto.

## Reglas que no se negocian

1. **Nada inventado.** Sin dato → «Sin datos» o «—». En gráficos, un día sin registro es `null`, nunca `0`.
2. **Todo texto con `t()`** en es, en, ko y zh-CN, incluidos `title`, `aria-label` y textos de estado vacío.
3. **Sin aclaraciones entre paréntesis en la UI:** título + descripción aparte. La descripción es **una sola oración
   simple**, sin incisos entre comas («, por ejemplo …,»): «Un escenario simula un cambio en la demanda sin modificar
   la planificación.» [D, 16/10/2026]
4. **No se muestra lo que la API rechaza** (permisos): no se deshabilita, se oculta.
5. **Tokens donde existan:** `text-campy-ink`, `bg-action-blue`, `rounded-card`, `rounded-input`,
   `rounded-pill`, `shadow-card-hover`, `bg-status-*`. Hex arbitrario solo si no hay token (ver tabla en
   tokens.md). **`campy-blue` no existe en campisoft: usar `action-blue`.**
6. **Colores con significado** (cinco tonos, ver abajo). **En la Worker App, advertencias, urgencias, avisos sin conexión y estados pendientes van en rojo** (el de «Cerrar sesión»), no en ámbar [D, Agustín 26/10/2026]; ver mobile.md. Nunca rojo para algo que no sea crítico/riesgo, **salvo un
   número que baja** (delta negativo, egresos), que sí va en rojo [D, Agustín 21/10/2026]. Los íconos de los KPI pueden llevar un tono
   propio decorativo (como los de [F]: ámbar, sky, violeta, teal, rojo, esmeralda) [D, Agustín 21/10/2026].
   **El violeta ya no es exclusivo de IA** [D, Agustín 17/10/2026]: lo usan Campy AI, el estado `INFO_REQUERIDA` de
   solicitudes de Shift, el color de servicio de Bienestar y la «versión» de un esquema de Shift [D, Agustín 21/10/2026].
   **En la Worker App lo que va en progreso usa una escala de azules** (lo hecho en blue-200/300, lo de ahora en el
   azul Campy, lo que viene en gris claro; `azulEscala1..3`) y los servicios **no tienen color propio**: todo en el azul
   Campy [D, Agustín 28 y 30/10/2026].
7. **Anillos y arcos con puntas redondeadas y separación entre tramos.**
8. **Ningún placeholder termina en «…» ni «...»:** ni el de un buscador («Buscar servicio», no «Buscar servicio…») ni
   el de ningún otro campo para escribir («Escribí tu pregunta», no «Escribí tu pregunta…»), en la web y en la app y en
   los cuatro idiomas [D, 15 y 19/10/2026].
9. **Alertas con mensaje corto:** título + una línea breve (`truncate`), p. ej. «2 insumos bajo stock de
   seguridad»; el detalle largo va al `title` o a la pantalla destino. Si las alertas no entran (más de
   4 en una tarjeta), se muestran 3 y una fila «Ver todas las alertas» con triángulo y contador que abre
   la lista completa en un popup.
10. **Ninguna bala (chip) de estado lleva punto al inicio** [D, Agustín 17/10/2026]: solo texto con fondo del tono y
    borde del color del texto («A confirmar», no «● A confirmar»). Vale para todo chip nuevo en la web y en la app; un
    chip con punto que ya exista en la web es un desvío y se corrige cuando se toca esa pantalla. No confundir con
    los indicadores sueltos que no son chips (no leído, «En vivo», «Grabando») ni con la leyenda de un gráfico.
11. **Los botones van solo con el texto** [D, Agustín 19/10/2026]: sin flecha («Ver traslado», no «Ver traslado →») ni ícono a
    los costados, en la web y en la app. Quedan afuera los botones que son solo un ícono (sin texto), el chevron de un
    selector que despliega opciones y **una fila entera que navega** (fila de alerta, «Ver todas»), que sí lleva su
    chevron a la derecha [D, Agustín 21/10/2026].
    **En la Worker App las tarjetas sueltas no llevan botón, chevron ni texto-enlace para navegar** («Ver alojamiento»,
    «Solicitar ayuda», «Reportar en Connect», «Reservar →»): se tocan enteras. **En un listado, las filas que se pueden
    tocar y llevan a algún lado sí llevan `>`** (Perfil «Más», Configuración, teléfonos, actividades) [D, Agustín 26/10/2026].
    Quedan las acciones reales, los botones de pantalla y los ‹ › de mes.
    **Toda fila que hay que distinguir como tocable entre filas que solo informan lleva el `>` gris** («Punto de
    encuentro» de Mi traslado, solicitudes de Mi roster, incidencias de Lavandería); se probaron y se descartaron una
    miniatura del mapa, una pastilla, un círculo y un fondo [D, Agustín 2/11/2026]. `FilaServicio` lo pone solo cuando hay
    `onTap`. **Las opciones de un pop-up que llevan al paso siguiente no llevan nada a la derecha** (ni `>`, ni flecha,
    ni círculo de elegir); el círculo con tilde queda para elegir de una lista [D, Agustín 30/10/2026].
    **Sin «+» delante del texto** tampoco en Shift ni Turnos («Nueva asignación»); el «+ Nueva asignación» de Operators es
    un desvío [D, Agustín 26/10/2026].
12. **Íconos en recuadro con un solo formato** [D, Agustín 19/10/2026] (Worker App): cuadrado redondeado (radio 24 % del
    lado), fondo blanco, borde de 1,25 y dibujo del color (`IconoRecuadro` en `ui.dart`, el de «Próximamente»). Nada de
    recuadros o círculos tintados con el ícono adentro.
13. **Soporte = auriculares** [D, Agustín 19/10/2026]: todo acceso a soporte o asistencia (escribir a soporte, pedir
    ayuda, mesa de ayuda) usa el ícono de auriculares (`headset` de lucide), nunca el sobre ni el signo de pregunta.
    El signo de pregunta queda para «informar un problema» de un servicio.
    También va como **ayuda**: un «?» chico junto a un dato abre un pop-up con su regla (Lavandería › «Mi cupo»)
    [D, Agustín 3/11/2026].
14. **Cabeceras de la Worker App** [D, Agustín 19 y 21/10/2026; 30/10 y 1/11]: la campana va **solo en Inicio** (con
    el avatar, **el nombre arriba grande y el saludo según la hora debajo, chico y gris** [D, 1/11], y a la izquierda de la
    campana el círculo rojo de ayuda urgente [D, 30/10]). Servicios, Mi Área y Cori van **sin cabecera**: el contenido arranca bajo la barra de estado y el título
    queda solo para el lector de pantalla. Perfil lleva una franja navy con la identidad y la tarjeta de accesos
    montada. Pantallas a las que se entra: volver y el título centrado, nada a la derecha salvo una acción propia. **Volver tiene dos
    formas según el fondo** (`BotonVolver`) [D, Agustín 1/11/2026]: sobre blanco o gris, círculo blanco de 44 con sombra
    suave e ícono en tinta; sobre azul o navy, solo la flecha blanca. Chevron en iPhone, flecha en Android.
15. **Mayúscula inicial** [D, Agustín 21/10/2026]: todo texto de pantalla empieza con mayúscula, en la web y en la app.
    Los códigos cortos van enteros en mayúscula («ES», «EN», «KO», «ZH»). Lo que va después de « · » también empieza
    con mayúscula («4/6 · Faltan ítems») y el mes de una fecha va con mayúscula también en la web («15 de Octubre»)
    [D, Agustín 21/10/2026]. Solo las continuaciones de una misma frase siguen en minúscula («3 de 4 personas», «Actualizado hace 5 min»).
18. **Sub-pestañas y selector de vista: los del módulo** [D, Agustín 21/10/2026]: cada módulo conserva su forma (Shift: tarjeta con
    `bg-blue-50` o el riel gris de Horarios, calendario con selector rectangular; Food: subrayado de [P] y `Segmentado`
    de [F]). Al trabajar en un módulo se usa la que ya tiene ese módulo; en uno nuevo, se pregunta.
    **En Shift (Operators y Providers) mandan las formas de Shift de Operators** sobre la regla de «burbujas en
    píldora» [D, Agustín 24/10/2026]: pestañas de módulo en píldora azul (`ShiftHubPage`), título «Shift» con el sitio
    debajo, `Combobox` de filtros `rounded-input`, sub-pestañas en tarjeta con radio 9, selector del calendario
    rectangular, botones de ícono `rounded-[8px]` y un subtítulo de una oración bajo el título de cada pestaña.
    **Planificación en dos ítems de menú, en los dos productos** [D, Agustín 26/10/2026]: «Rosters» (el Shift de
    siempre: esquemas, asignaciones, solicitudes, calendario, DAE/DAP, colores) y «Turnos» (horarios de entrada y
    salida, ruta propia: `/turnos` en Operators, `/providers/turnos` en Providers), con la cabecera y la barra de
    secciones de Rosters. En Providers, Turnos conserva la sección **Excepciones** (Operators la sacó): es la única
    forma de cargar un cambio de horario de un día puntual. También conserva lo que Operators sacó y Providers ya tenía: esquemas rotativos y fijos, reglas
    por dotación o puesto, editar vigencia y contraturno, y reactivar esquemas [D, Agustín 26/10/2026].
16. **Letra de la Worker App** [D, Agustín 20/10 y 30/10/2026]: se dibuja un 13 % más chica que lo escrito
    (`escalaLetraCampy = 0.87`) y **una sola escala para toda la app menos el login** (`LetraCampy` en `theme.dart`:
    número grande 42, número 24, saludo 20, sección 17, título 14, texto 13, chico 11,5). El tamaño de letra del teléfono
    se respeta **entre 0,85 y 1,5×** (antes 1,0–1,1). No se compensa a mano: si algo no entra, el componente crece.
17. **Animaciones** [D, Agustín 21/10/2026]: respetan «reducir movimiento» del teléfono (quietas o un fundido) y
    **nunca traban la navegación ni impiden entrar**: si una animación falla, la acción sigue sin ella.
19. **Nada de anotaciones de relleno** [D, Agustín 26/10/2026]: no se muestra de dónde sale un dato ni quién lo
    cargó («Cargada por tu empresa», «Recepción a cargo de la minera según…»), ni aclaraciones de alcance o del sistema
    («Solo por tipo», «Solo el cocinero declara»), ni el mismo dato dos veces (chip «Vencida hace 3 días» y además
    «Venció el 23 de Octubre»). Cada pantalla muestra solo lo que la persona necesita para actuar; ante la duda, se saca.
20. **Texto completo: sin «...», sin paréntesis, nada cortado** [D, Agustín 28/10/2026]. Ningún texto de pantalla
    termina en puntos suspensivos (en la app, nunca `TextOverflow.ellipsis`; en la web, nada de `truncate` en un dato
    que la persona necesita leer), ninguno lleva palabras entre paréntesis (se reescribe con « · » o en otra frase) y
    nada se corta: si no entra, baja de línea y el componente crece (o se achica un poco la letra antes de cortar).
    Meses y días enteros («Noviembre», no «Nov»). Un carrusel que deja asomar la tarjeta siguiente no es un corte. Las
    tarjetas de una misma fila, del mismo alto (manda la más alta).
21. **Pop-ups cortos** [D, Agustín 28/10/2026]: título corto y como mucho **un detalle de una oración, ~60 caracteres**
    (dos líneas en un cuadro de 342). Lo que no hace falta para decidir, afuera; las instrucciones largas van en la
    pantalla. Vale para todo pop-up nuevo, en la app y en la web; uno viejo con un párrafo se acorta en los cuatro
    idiomas cuando se toca. Un pop-up de ayuda («?») es solo el título y una oración, sin ícono ni mosaicos [D, 3/11].
22. **Todo mensaje emergente es un pop-up de Campy, nunca un banner ni una barra** [D, Agustín 2/11/2026] (Worker App:
    `avisoCampy(context, texto, tono:)` en `widgets/ui.dart`; nada de `SnackBar` ni `ScaffoldMessenger`). Única excepción:
    el «Guardado» de 1 s del autoguardado de la OT. **Lo que falló y sigue abierto** (una incidencia, un rechazo del
    encargado) tampoco va en un recuadro rojo en la hoja: sale en un pop-up al entrar a la pantalla, se va al cerrarlo
    y vuelve a salir en cada entrada mientras siga abierto [D, Agustín 4/11/2026]. Una confirmación continua (el pase del
    embarque por QR) va dentro de la pantalla, no en pop-up.
23. **Nunca flechas de ruta** [D, Agustín 29/10/2026]: ningún «→», «->», «>» ni «➜» entre origen y destino en un texto de
    pantalla. En una línea, «ALFA Norte a Salta» (clave `comunRuta`, «{origen} a {destino}»); con lugar, el widget
    `Recorrido` (círculo vacío, línea de puntos, círculo lleno). Tampoco en caminos de navegación («Servicios →
    Alojamiento» se escribe con palabras) ni en las maquetas.
24. **Horas con «hs» y fecha entera, en toda la Worker App** [D, Agustín 29/10 y 4/11/2026]. Toda hora lleva «hs»
    pegado: «14:00hs» (`comunHoraHs`; solo el español lleva el sufijo, los otros idiomas muestran la hora sola); toda
    duración, «4hs», «1hs 20 min» (`duracionTextoHs`, no `duracionTexto`). Toda fecha va con el día y el mes enteros:
    «Viernes 6 de Noviembre», «6 de Noviembre» (`fechaConDia` o `fmtFecha` sin `corta`); nunca «Nov», «Vie» ni
    `fmtFecha(…, corta: true)`. Si la fecha entera no entra, se reubica en otra línea (regla 20), no se abrevia. Solo
    quedan cortos los encabezados de columna de un calendario (Lun…Dom). En la web: `[pendiente]` confirmar con
    Agustín si también lleva «hs».
25. **Sin zócalos** [D, Agustín 31/10/2026]: ninguna tarjeta ni fila lleva una barra de color pegada al borde izquierdo.
    Se distingue con el fondo (celeste lo destacado, blanco con borde fino lo demás), con el color del texto o con la
    palabra del estado. En la app, en el lienzo y en la web nueva.
26. **Negrita solo para los títulos importantes** [D, Agustín 3/11/2026]: el título de un bloque («Mi cupo»,
    «Incidencias») y el dato grande que se busca primero («6 prendas listas», «Módulo B»). Rótulos, valores de lectura
    (fechas, números de orden, cupo), el texto de las filas y los estados van sin negrita (400/500). El valor de toda
    grilla de datos (`DatosServicio.valorDato`) es regular. Se ajusta cada pantalla cuando se toca.
27. **Una pieza igual se ve igual en todos los perfiles** [D, Agustín 17/10 y 2/11/2026]: chofer, pasajero, supervisor,
    mucama o técnico ven la misma pantalla de servicio con el mismo componente (`ArcoRuta`, `PuntaRuta`,
    `PantallaServicioAzul`, `EncabezadoChapa`, `FilaServicio`, `TarjetaCarrusel`); si a un rol le falta algo, se agrega un
    parámetro al componente común, nunca una copia parecida. Y todo cambio de la app vale para todas las fases (en sitio,
    llegada, descanso, sin roster), roles y categorías, propios y contratistas.
28. **La app del trabajador marca y mira; la gestión es de la web** [D, Agustín 28/10 y 2/11/2026]. Marcar ingreso y
    salida, ejecutar (una OT, un viaje, una limpieza), escanear y mirar su ciclo, servicios y solicitudes. Cerrar o
    reabrir ciclos, DAE/DAP, ajustes del campamento, crear OT o planificar: web. No se diseñan pantallas de procesos
    administrativos en la app. **Excepción desde el 4/11/2026: el supervisor sí resuelve y gestiona desde la app** lo de su
    equipo (solicitudes, aprobar o rechazar una limpieza).
29. **La barra de abajo de la app no se cambia** [D, Agustín 29/10/2026]: la de `screens/shell.dart` (cinco íconos, la
    elegida en un círculo sin texto, Cori al medio) queda como está. Si una maqueta dibuja otra barra (con el nombre de
    la pestaña elegida, con difuminado), es de la maqueta y no pasa al código sin que Agustín lo pida.
30. **Un QR por persona** [D, Agustín 28/10/2026]: la credencial de la app (la que rota y muestra «Mi QR») sirve para
    todo: embarcar, hospedaje, lavandería, comedor, vianda, actividades. Nunca se diseña un QR por orden, viaje o reserva;
    las «credenciales» de cada servicio (Lavandería, Comedor) muestran ese mismo QR con los datos de ese servicio. El
    código de barras Code 128 del ticket de equipaje no es una credencial y sí va.

## Lo esencial de un vistazo

| Qué | Clases |
|---|---|
| Título de pantalla | `text-[24px] sm:text-[30px] font-bold text-campy-ink leading-tight` + sub `text-[13.5px] text-slate-500` |
| Título de pestaña interna | `text-[27px] font-bold text-campy-ink tracking-tight leading-none` + sub `mt-2 text-[14px] text-slate-500` [D, Agustín 21/10/2026] |
| Tarjeta | `rounded-card bg-white border border-slate-200/80 shadow-[0_1px_2px_rgba(15,30,60,0.04),0_10px_28px_-18px_rgba(15,30,60,0.14)] p-4 sm:p-5` |
| Título de tarjeta | `text-[16px] font-bold text-campy-ink leading-snug` + sub `text-[13px] text-slate-500` |
| Rótulo en mayúscula | `text-[12px] font-bold uppercase tracking-[0.1em] text-slate-500` |
| Número grande / KPI | `text-[30px] font-bold tabular leading-none text-campy-ink` |
| Encabezado de tabla | `text-[12px] font-bold uppercase tracking-[0.06em] text-slate-400` [D, Agustín 21/10/2026]: los `th` de 11 px de Shift son desvío |
| Celda | `text-[13px] text-slate-600`; nombre principal `text-[14px] font-bold text-campy-ink` |
| Chip de estado | `inline-flex items-center rounded-pill border px-2.5 py-1 text-[12px] font-semibold` + tono |
| Botón primario | `h-11 px-5 rounded-[20px] text-[15px] font-semibold text-white bg-action-blue hover:bg-blue-700 hover:shadow-[0_8px_20px_rgba(37,99,235,0.35)] active:scale-[0.98] transition-all disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:shadow-none` |
| Input | `h-11 w-full rounded-input border border-slate-200 bg-white px-3.5 text-[15px] text-campy-ink placeholder:text-slate-400 focus:border-action-blue focus:outline-none focus:shadow-[0_0_0_3px_rgba(37,99,235,0.12)] transition-all` |
| Página | `space-y-5`; grilla de tarjetas `grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4` |

## Colores de estado (cinco tonos + IA)

| Tono | Significa | Chip |
|---|---|---|
| emerald | bien, activo, aprobado, sin alertas | `bg-emerald-50 text-emerald-700 border-emerald-700` |
| amber | pendiente, pausado, por vencer | `bg-amber-50 text-amber-700 border-amber-700` |
| red | vencido, rechazado, crítico, riesgo de vida, faltante | `bg-red-50 text-red-600 border-red-600` |
| blue | en curso, programado, informativo | `bg-blue-50 text-action-blue border-action-blue` |
| slate | finalizado, cancelado, cerrado, inactivo | `bg-slate-100 text-slate-500 border-slate-500` |
| violet | funciones de IA, `INFO_REQUERIDA` de solicitudes de Shift y Bienestar (ya no es exclusivo de IA [D, 17/10/2026]) | `bg-violet-50 text-violet-600 border-violet-600` |

**El borde de todo chip es del mismo color que su texto** [D] (no un tono más claro).

Los gráficos van en **azules** (ver graficos.md); el rojo entra solo para lo que hay que resolver.

## Trampas del CSS global (`apps/web/src/index.css`, en los dos repos)

- `.border-slate-200` y `.border-slate-200/70` se pintan como **slate-300** (`!important`); `border-slate-200/80`
  no. Por eso la tarjeta usa `/80`.
- `divide-slate-100` se ve slate-200 (`index.css:244-257`).
- `tbody tr:hover` es **slate-100 con `!important`**: el `hover:bg-…` de una fila de tabla no tiene efecto.
- `table`, `.tabular` y `.kpi` ya son `tabular-nums`; h1–h3 ya tienen `letter-spacing: -0.02em`.
- Foco global: `outline 2px rgba(37,99,235,0.8)` con offset 2. Si un elemento lo saca con `outline-none`,
  tiene que poner `focus-visible:ring-2 focus-visible:ring-action-blue/40`.

## Cómo aprende esta skill

La skill se autoevalúa y se corrige sola, en tres momentos. No es opcional: es parte de usarla.

1. **Al empezar** una tarea de diseño o una revisión, correr la autoevaluación desde la carpeta de esta skill:
   `python3 scripts/autoevaluar.py` (lee `origin/main` de los dos repos sin tocar las copias de trabajo; los repos se
   buscan en `$CAMPISOFT` y `$CAMPYPROV`, por defecto `~/Escritorio/laburo/campisoft` y `~/Escritorio/laburo/campyprov`: si tus clones están en otro
   lado, exportá esas dos variables;
   para mirar una rama: `--campisoft /ruta --campisoft-ref HEAD`). Reporta rutas que la skill cita y
   ya no existen, desvíos de las reglas en el código (chips con punto, botones con flecha, placeholders con «…»,
   `campy-blue`, Material prohibido, minúsculas, y en la app textos cortados con «...», `ScaffoldMessenger`, paréntesis
   y flechas de ruta), pantallas de referencia que cambiaron después de «Última revisión» y
   aprendizajes pendientes. Leer el informe antes de diseñar: si una referencia cambió, mirar el cambio y actualizar la
   skill antes de copiar de ella.
2. **Durante:** cada corrección o decisión de diseño del usuario («así no», «va con mayúscula», «sacá el hueco») se
   anota **en el momento** en [references/aprendizajes.md](references/aprendizajes.md) (fecha, qué, origen, dónde
   quedó) y se lleva a la regla, pieza o token que corresponde en el mismo turno, con `[D, usuario dd/mm/aaaa]`.
   Lo que el usuario no decidió queda `[pendiente]` y se le pregunta; nunca se elige por cuenta propia. **Si quien usa la
   skill no es Agustín**, su decisión se anota `[pendiente: confirmar con Agustín]`, salvo que diga que ya lo acordó con
   él (entonces `[D, Agustín dd/mm/aaaa]` y de dónde salió). Si tenés el vault de producto de Campy, la decisión va
   también a `02 - Decisiones/Registro de decisiones.md`.
3. **Al terminar:** revisar lo hecho contra la skill. Si se usó un valor, una pieza o un patrón que la skill no tenía,
   o si la skill dijo algo que el código o el usuario desmintieron, corregir la skill, sumar la entrada en
   aprendizajes.md y actualizar «Última revisión». Si la autoevaluación mostró desvíos en el código, reportarlos al
   usuario (no se corrigen sin que lo pida).

**Dónde se guarda lo aprendido.** Esta skill vive en el repo `ajuarez-campy/campy-diseno`. Si está instalada en modo
editable (`install.sh`: `~/.claude/skills/campy-diseno` es un enlace a un clon del repo), los cambios se hacen ahí y
se commitean en ese repo con un mensaje en español («Aprendizaje: …»); el push se le propone al usuario. Si está
instalada como plugin (la carpeta está dentro de `~/.claude/plugins/cache/`), **no se edita**: esa copia se pisa en
cada actualización. En ese caso se le muestra al usuario el cambio propuesto (texto y archivo) para que lo suba al repo.

El script solo informa: las decisiones las toma el usuario. Si una búsqueda del script da falsos positivos, se mejora
el script (y se anota en aprendizajes.md), no se ignora el informe.

