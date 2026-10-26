# Worker App (Flutter): el mismo diseño que la web

**Regla [D, 16/10/2026]: la Worker App es un fiel reflejo de la web.** Misma tipografía, mismos colores, mismos
radios, mismas sombras, mismas piezas, y los mismos estilos y textos en alertas, popups, toasts, confirmaciones,
estados vacíos, cargas y errores. Si una pantalla de la app se ve distinta de su equivalente web, está mal la app.
Vale para todos los roles y todas las fases (en sitio, llegada, descanso, sin roster): **una sola app, un solo
diseño**.

Código: `worker-app/lib/theme.dart` (`CampyColors`, `campyTheme()`, `CampyCard`, `EstadoChip`),
`worker-app/lib/widgets/ui.dart` (piezas propias), `worker-app/lib/widgets/proximamente.dart`,
`worker-app/lib/widgets/cori_vivo.dart` (Cori con vida), `worker-app/lib/widgets/mi_qr.dart` y
`worker-app/lib/screens/shell.dart` (barra inferior y vuelo de Cori). Maquetas:
`/home/agustin/Escritorio/laburo/visual-app-mobile-campy/` (20 pantallas: Inicio en sitio y en descanso, Próximo
traslado, Indicaciones, Pase, Servicios, Perfil, Notificaciones, Login, Check In ×3, Bienestar ×4, Lavandería,
Preferencias, Nueva solicitud, Asistente).

**Quién manda cuando chocan** [D, Agustín 16/10/2026]: **las tres pantallas de referencia** (dashboard de Food [F],
planificación de Food [P] y Shift [S], ver SKILL.md) mandan sobre la maqueta y sobre cualquier otra pantalla web.
En la **composición** (qué bloques hay, en qué orden, cómo se reparten) la maqueta decide solo donde esas tres no
dicen nada; en los **valores** (color, tamaño y peso de letra, radio, sombra, alto, borde, textos de estado) mandan
ellas. Donde las tres no coinciden entre sí, vale lo que fija tokens.md › «Choques entre las tres referencias». Las medidas de este documento están en píxeles lógicos y son las de la web **en ancho de celular**
(< 640 px, sin el prefijo `sm:` de Tailwind).

**Nada de textos que informan lo obvio** [D, Agustín 17/10/2026]: no se agregan aclaraciones que repiten lo que la
pantalla ya muestra («Es tu usuario para ingresar a la app», «Mi credencial» bajo el QR, «Tu solicitud será revisada…»,
descripciones de una opción que se explica sola). Se dejan solo los que avisan algo que no se ve: una consecuencia
(«Se cierra la sesión en tus otros teléfonos»), una regla (contraseña), un estado (sin conexión) o seguridad
(emergencia, Cori). Botones con la acción corta: «Ver credencial», no «Ver credencial completa».

## Tipografía

**Meses con mayúscula inicial** [D, Agustín 17/10/2026]: en español «17 Oct», «Octubre 2026», «viernes 17 de Octubre»
(`fmtFecha` y `Idioma.diaCorto/diaLargo/diaAnio/mesAnio`). El día de la semana no cambia.

| Web | Flutter | Hoy en la app (16/10) |
|---|---|---|
| Inter variable, `index.css:8-21` | **El mismo archivo de la web** [D, 17/10/2026]: `apps/web/public/fonts/InterVariable.woff2` instanciado a opsz 14 y con cv02/cv03/cv04/cv11/ss01 congelados (se ven siempre, sin `fontFeatures`); receta en `worker-app/tool/fuentes_inter.md`. Cuatro TTF estáticos (Regular 400, Medium 500, SemiBold 600, Bold 700) declarados en `pubspec.yaml` con su `weight`; `fontFamily: 'Inter'`, `fontFamilyFallback: ['NotoSansSC', 'NotoSansKR']`. Con el TTF variable, según la versión de Flutter, el peso solo cambia con `fontVariations: [FontVariation('wght', 700)]`: los estáticos evitan la duda | `fontFamily: 'Roboto'` (`theme.dart:53`) y sin Inter en `pubspec.yaml:86-92` ✗ |
| `font-feature-settings: 'cv02','cv03','cv04','cv11','ss01'` (`index.css:52`) | ya congelados en los TTF (no hace falta `fontFeatures`) | — ✗ |
| `font-bold` | `FontWeight.w700` | `w800`/`w900` en ~180 lugares ✗ |
| `font-semibold` / `font-medium` | `w600` / `w500` | |
| `tabular`, `table`, `.kpi` | `fontFeatures: [FontFeature.tabularFigures()]` en todo número | — ✗ |
| h1–h3 `letter-spacing: -0.02em` | `letterSpacing: -0.02 × tamaño` (24 → -0.48, 28 → -0.56) | -0.5 fijo o nada |
| `leading-none` / `leading-tight` / `leading-snug` | `height: 1.0` / `1.25` / `1.375` | |

El logo es una imagen, no texto: `apps/web/public/logo-white.png` (sobre navy) como asset de la app, alto 28.
Hoy se escribe «campy» en Roboto w800 (`ui.dart:74`, `home.dart:234`, `login.dart:218-227`) ✗.

**Escala global de la letra [D, Agustín 20/10/2026]:** toda la letra se dibuja un 13 % más chica que el `fontSize` escrito (`escalaLetraCampy = 0.87` en `worker-app/lib/main.dart`, por el `textScaler` del `builder`). En el código se siguen escribiendo los tamaños de esta tabla; en pantalla, 15 se ve como 13. No achicar estilos a mano para compensar.

**Letra de app móvil [D, Agustín 17/10/2026]:** el cuerpo y los detalles van más grandes que en la web para leerse en el
teléfono: 12,5 → 14, 13 → 14,5, 13,5 → 15 (rótulos y chips de 11–12 y los títulos no cambian).

Tamaños por rol: lo que se escribe en el código de la app, ya con el agrandado del 17/10 (la web en ancho de celular, más
13,5 → 15 y 13 → 14,5). En pantalla se ven un 13 % más chicos por la escala global:

| Rol | Flutter |
|---|---|
| Título de pantalla | 24 w700 `ink`, `height 1.25`, `letterSpacing -0.48` (30 en tablet ≥ 640) |
| Subtítulo de pantalla | 15 w400 `gris` |
| Título de pestaña interna | 27 w700 `ink`, `height 1.0`, `letterSpacing -0.54`; sub 14 `gris` a 8 [D, Agustín 21/10/2026] |
| Título de sección fuera de tarjeta («Paso a paso», «Novedades») | 16 w700 `ink`, con la acción (si hay) a la derecha [P `FoodPlanificacion.tsx:474-477`, «Escenarios»] |
| Título de tarjeta | 16 w700 `ink`, `height 1.375`; en las tarjetas «Para vos» de la maqueta, 20 w700 |
| Subtítulo / contexto | 14.5 `gris` (detalle de `VacioCampy`, mensaje de `ErrorReintentar`, descripción de `CabeceraHoja`, tooltip) |
| Línea secundaria, pie | 12 `grisClaro` |
| Rótulo en mayúscula | 12 w700 `gris`, `letterSpacing 1.2`, `toUpperCase()` |
| Número KPI / de cabecera | 30 w700 `ink` tabular `height 1.0` (24 si pasa 6 caracteres, 22 si pasa 9) |
| Número mediano (mini KPI, hora, asiento) | 24 w700 tabular `height 1.0`; sufijo «Hs» 12 w700 desde el ARB |
| Etiqueta de formulario | 15 w600 `gris`, asterisco `#EF4444` |
| Input, select | 15 `ink`; buscador 14 |
| Botón primario / secundario | 15 / 14 w600 |
| Chip de estado / de leyenda | 12 w600 / 13.5 w500 `grisTexto` |
| Enlace | 14.5 w600 `azul` |

## Colores

Nada de colores de Material (`Colors.blue`, `Colors.black`…) y **nada de colores derivados del `seedColor`**: con
`ColorScheme.fromSeed(seedColor: azul)` (`theme.dart:51`) todo lo que toma el `colorScheme` (spinners,
`RefreshIndicator`, `TextButton`, `ChoiceChip`, `Checkbox`, `Divider`, `showDatePicker`, foco de `TextField`
sin `focusedBorder`) sale en un azul lavado distinto de `#2563EB`. Hay que fijar en `campyTheme()`:
`colorScheme: ColorScheme.fromSeed(seedColor: azul).copyWith(primary: azul, onPrimary: Colors.white, secondary: azul,
surface: Colors.white, surfaceTint: Colors.transparent, outline: bordeControl, outlineVariant: borde, error: rojo)`,
más `dividerTheme: DividerThemeData(color: borde, thickness: 1, space: 1)`.

| Web | `CampyColors` | Valor (web = objetivo) | Hoy en la app (16/10) |
|---|---|---|---|
| `campy-ink` | `ink` | `#061333` | `#0F172A` ✗ (`theme.dart:27`) |
| `campy-navy` | `navy` | `#061333` | `#0F1E3C` ✗ (`theme.dart:26`) |
| `campy-navy-soft` (degradé de modal) | — crear `navySuave` | `#0C1F4A` | — |
| fondo del contenido (`bg-slate-100` en la web) | `fondo` | **en la app, blanco** `#FFFFFF` [D, Agustín 17/10/2026: blanco y secciones, la app no copia el panel gris de la web]; el gris `#F1F5F9` queda en `grisFondo` (rieles, campos, esqueletos) | `theme.dart:55` ✓ |
| `action-blue` | `azul` | `#2563EB` | igual ✓ |
| `hover:bg-blue-700` | `azulOscuro` | `#1D4ED8` (la web también usa `#1d4fd8` en `campy-ui.tsx:21`) | `#1D4FD8` ✓ |
| `bg-blue-50` / `border-blue-100` / `border-blue-200` | `azulFondo` / — crear `azulBordeSuave` / `azulBorde` | `#EFF6FF` / `#DBEAFE` / `#BFDBFE` | ✓ / — / ✓ |
| `text-slate-500` | `gris` | `#64748B` | igual ✓ |
| `text-slate-400` | `grisClaro` | `#94A3B8` | igual ✓ |
| `text-slate-600` (celdas, texto del secundario) | — crear `grisTexto` | `#475569` | — (se usa `gris`) |
| `text-slate-300` (ícono de vacío) | — crear `grisIcono` | `#CBD5E1` | — |
| borde de tarjeta `border-slate-200/80` | `borde` | `#E2E8F0` al 80 % → `Color(0xCCE2E8F0)` | `#E2E8F0` opaco (casi igual) |
| borde de input y de secundario `border-slate-200` (el CSS global lo pinta slate-300, `index.css:245`) | — crear `bordeControl` | `#CBD5E1` | `#E2E8F0` ✗ (`ui.dart:399`) |
| separador `divide-slate-100` (el CSS global lo pinta slate-200, `index.css:255`) | `borde` | `#E2E8F0` | `Divider` sin color: sale del seed ✗ |
| `bg-slate-100` (riel, esqueleto, chip cerrado) / `bg-slate-50` | — crear `grisFondo` / `grisFondoSuave` | `#F1F5F9` / `#F8FAFC` | hex suelto `0xFFF1F5F9` ×9, `0xFFF8FAFC` ×3 |
| emerald-700 / -50 (ok) | `verde` / `verdeFondo` | `#047857` / `#ECFDF5` | `#16A34A` ✗ / ✓ |
| amber-700 / -50 / -200 (pendiente) | `ambar` / crear `ambarFondo` / crear `ambarBorde` | `#B45309` / `#FFFBEB` / `#FDE68A` | `ambar #F59E0B` ✗; se usa `naranja #EA580C` + `naranjaFondo #FFF7ED` + `naranjaBorde #FED7AA` (orange) ✗ |
| red-600 / -50 / -200 (crítico) | `rojo` / `rojoFondo` / `rojoBorde` | `#DC2626` / `#FEF2F2` / `#FECACA` | igual ✓ |
| slate (cerrado, cancelado, «Próximamente») | `gris` / `grisFondo` | `#64748B` / `#F1F5F9` | `fondo` o `0xFFF1F5F9` |
| violet-600 / -50 (IA, `INFO_REQUERIDA` y Bienestar [D, 17/10/2026]) | — crear si hace falta | `#7C3AED` / `#F5F3FF` | — |
| `bg-slate-900/40` (fondo detrás del modal) | — | `Color(0x660F172A)` | `barrierColor` por defecto |
| Toast `status-*-soft` + texto -900 | — | ver «Toast» | — |

`verdeBorde` (`#BBF7D0`) y `naranjaBorde` no tienen uso en la norma: **el borde del chip es del color de su texto**.
Las filas con ✗ son deuda de `theme.dart`: cambiar la constante alinea toda la app de una vez; en código nuevo se
usa la constante (no un hex suelto) para que el ajuste sea en un solo lugar.

Los **cinco tonos con significado** de la web valen igual (SKILL.md). En Move: confirmado/programado → emerald
(aprobado) · a confirmar → amber · en embarque, en viaje → **blue** (en curso) · finalizado, cancelado → **slate** ·
contingencia → amber. Rojo solo para crítico o riesgo; el SOS es rojo porque es una emergencia.

Colores de servicio (íconos y títulos en Servicios): Alojamiento `azul`, Comedor naranja `#EA580C`, Lavandería
`#0891B2`, Bienestar `#7C3AED`, Conectividad `#0EA5E9`.

**Sin modo oscuro [D, Agustín 19/10/2026]:** la app es siempre clara; se quitaron Apariencia y lib/apariencia.dart (ya no existe). La paleta oscura de `CampyColors` quedó en el código (getters con `ModoColor.oscuro`, que vale siempre `false`) pero no se usa. Lo que sigue es histórico. **Antes (17/10):** sigue al teléfono por defecto y se elige en Configuración › Apariencia
(Como el teléfono / Claro / Oscuro; lib/apariencia.dart, guardado en SharedPreferences). Los colores que dependen del
modo son getters de `CampyColors` que leen `ModoColor.oscuro` (por eso **no van en expresiones `const`**); los de
relleno y marca son fijos (`azul`, `rojo`, `navy`, `violeta`, servicios). Paleta oscura (slate): fondo #0B1220,
superficie #111A2E, superficie elevada #17223A, borde #24324D, borde de control #334466, ink #E6EDF7, gris #9AA8BF,
grisTexto #C3CDDC, grisClaro #7385A3; tonos con texto más claro (verde #34D399, ámbar #FBBF24) sobre fondos oscuros
tintados. Fondos de superficie: `CampyColors.superficie` (nunca `Colors.white`); **QR siempre sobre blanco con módulos
navy** (`CampyColors.blanco`, `QrImageView(backgroundColor: Colors.white)`). Barra de estado: `estiloBarraEstado`.
**Tamaño de letra del teléfono:** se respeta acotado a 1,0–1,1 (`builder` de `MaterialApp`); con 1,3 se veía gigante en Android [D, Agustín 20/10/2026].

## Formas, bordes y sombras

**[D, Agustín 17/10/2026] manda sobre esta tabla para los contenedores:** fondo de pantalla blanco (`CampyColors.fondo`
= blanco); `CampyCard` sin color = sección sin caja (padding vertical, contenido alineado al margen de 16, línea
`borde` abajo, apretada `grisFondoSuave`); `CampyCard` con color = superficie tintada radio 16 sin borde ni sombra;
tarjetas de servicio y «Para vos» tintadas radio 20 sin borde; `PestanasCampy` en riel `grisFondo` sin borde.
Sombra solo en lo que flota (recuadro de Mi QR, toast, hojas). El Inicio pone los datos debajo de la foto, sin
tarjeta encima. Las medidas de sombra/borde de abajo quedan para esos casos.

| Web | Flutter |
|---|---|
| `rounded-card` 16 | `BorderRadius.circular(16)`: tarjeta, modal, hoja inferior (arriba), toast, popover; 20–24 solo en las tarjetas grandes de la maqueta (hero del Inicio, «Para vos», ticket del pase) |
| `rounded-card-sm` 12 | `circular(12)`: subtarjeta, aviso en línea, recuadro de ícono, tooltip |
| `rounded-input` 10 | `circular(10)`: input, select, buscador, botón de ícono, botón fantasma, menú |
| `rounded-pill` | `circular(999)`: chips, barras de avance, pestañas (nunca inputs ni botones: ver «Login») |
| Barra de avance (color) | en el Inicio, relleno **`CampyColors.azul`** como el resto de la tarjeta, riel `grisFondo` [D, Agustín 26/10/2026; antes navy, 23/10]. Fuera del Inicio: preguntar. Ej.: `_BarraAvance` `home.dart` |
| Advertencias, urgencias, avisos sin conexión y estados pendientes | **`CampyColors.rojo`** (#DC2626, el de «Cerrar sesión»), texto, ícono, borde y fondo `rojoFondo`/`rojoBorde`; ya no ámbar. «Pendiente», «A confirmar», toasts de espera, «Datos guardados…», «Falta…», bajada vencida: todo rojo. Ámbar solo para las campanitas y lo que no es aviso (micrófono hablando, niveles, categorías) [D, Agustín 26/10/2026] | `theme.dart`, `colorTono` |
| Acciones de una fila, de a pares | botones en **píldora** chicos (`botonPildoraCampy`: alto 36, `StadiumBorder`, 13.5 w600, fondo blanco y contorno del tono; apretado, fondo del tono): azul con borde `azulBorde` para la acción (Adjuntar foto / Ver respaldo), rojo con `rojoBorde` para cancelar. Van debajo de la fila con todo su ancho, de izquierda a derecha [D, Agustín 26/10/2026] | `roster.dart` `_solicitudFila` |
| «Transporte» del Inicio | formato **pase de embarque** (maqueta A del 24/10): título azul + fecha larga + chip; salida y llegada 30 w700 con origen y destino del tramo, línea punteada `azulBordeSuave` con el bus y la duración; corte con medias muescas de 10; abajo 3 datos (Vehículo · Asiento · Sube en, flex 10/7/13, valor hasta 2 renglones). Sin botón desde el 26/10: se toca la tarjeta entera. Sin llegada «—» y sin duración. Chofer: Vehículo · Pasajeros. Columna angosta y sin traslado: `_ParaVos` [D, Agustín 26/10/2026] | `_BoletoTransporte` `home.dart` |
| Fechas | **mes y día enteros** en toda la app: «8 de Noviembre», «26 de Octubre de 2026», «Miércoles» (`fmtFecha`, `Idioma.diaCorto`, `diaAnio`, `diaSemana`). Cortos solo los encabezados de calendario (Lun…Dom) y la tarjeta del turno del Inicio (`fmtFecha(…, corta: true)`) [D, Agustín 26/10/2026] | `theme.dart`, `idioma.dart` |
| Tarjeta del turno del Inicio | **inmersiva**: la foto del campamento (`perfil.fotoCampamento`; sin ella `campamento-noche.jpg`) ocupa toda la tarjeta, radio 24, sombra `#081024` de 0 a 92 % desde arriba (0 · 5 % · 62 % · 92 %) para leer en blanco; arriba chip vidrio oscuro (rojo si es aviso) y Mi QR azul 56; abajo rótulo 13.5, número grande 40 w700 blanco, línea del turno y **línea de tiempo** Hoy · Ingreso · Salida (pista blanca 28 %, hecho en blanco, punteado del ingreso a la salida, ingreso relleno azul, hoy con halo) con la fecha en negrita y la hora debajo [D, Agustín 26/10/2026] | `_Hero`, `_LineaDelTurno` `home.dart` |
| Tarjetas del Inicio | todas en el **azul Campy** (`CampyColors.azul`, el de «Transporte»): la del turno (Próximo turno, Mi estadía) lleva ícono, días, duración, días restantes, porcentaje y barra en azul; el botón del QR también, con el dibujo blanco [D, Agustín 26/10/2026, reemplaza el navy del 19, 23 y 26/10] | `home.dart` |
| Servicios (pestaña) | **widgets de estado** a la manera de Apple Home: bloque de color lleno radio 24, padding 16, letra blanca; el dato del momento en 24 w700 (30 a lo ancho), nombre 14 w600 blanco 85 %, línea 13 blanco 85 %, chip vidrio (blanco 18 % con borde blanco 45 %). Fondo en el tono 700 del color de servicio (`CampyColors.serv*Fuerte`: Comedor `#C2410C`, Lavandería `#0E7490`, Conectividad `#0369A1`; Alojamiento azul y Bienestar violeta). Pictograma blanco sin recuadro (30 en la grilla; a lo ancho, 190 al 16 % de fondo). Sin botón: se toca el bloque entero (0,98 al apretar). Comedor primero; con cantidad impar, el primero a todo el ancho; sin buscador ni contador [D, Agustín 26/10/2026] | `_WidgetServicio` `servicios.dart` |
| «Para vos» del Inicio | **Transporte fijo arriba** + dos filas deslizables «Hoy» y «Tu estadía» [D, Agustín 26/10/2026]: cada servicio aparece solo cuando tiene algo (Comedor abierto o próximo; vianda de hoy; reserva de hoy; orden de lavandería; caso abierto; Conectividad solo si la señal es mala) y con su módulo. Todas **vivas** como «Mi alojamiento» (`_Viva`): llenas en el tono fuerte de su servicio (`CampyColors.serv*Fuerte`: Comedor `#C2410C`, Lavandería `#0E7490`, Alojamiento azul marino `#1E3A8A`, Bienestar violeta, Transporte `azul`, Ayuda fucsia `ayudaFuerte` `#BE185D`, Conectividad `rojo`; cada una distinta) y **una sola tarjeta de comida** (el comedor con la vianda de hoy en una franja abajo; sin comedor, la vianda sola), radio 24, padding 18, rótulo 14 w600 blanco 85 %, chip vidrio, dato grande w700 blanco (27; Comedor 30, vianda 46), dibujo del servicio 160 al 16 % abajo a la derecha, avances en blanco (segmentos de 6 o nodos de 24 con halo). Filas: tarjetas de `ancho - 32 - 46` (asoma la siguiente), imán por tarjeta (`_ImanPorTarjeta`), puntitos 6/18; una sola tarjeta a todo el ancho; la fila con aviso sube. Reemplaza «todas las tarjetas del Inicio en azul» | `_ParaVosSeccion`, `_Fila`, `_Viva`, `_Nodos` `home.dart` |
| Cabecera del Inicio | saludo y debajo la fecha entera «Lunes, 26 de Octubre», sin «Hoy» (`Idioma.diaSemanaLargo`); campana **ámbar entera** (borde de 1,25 y dibujo; `BotonRedondo(borde: CampyColors.ambar)`), como la de Notificaciones [D, Agustín 26/10/2026] | `barraCampy` `ui.dart`, `hoyCabecera` |
| botón `rounded-[20px]` | `circular(20)` |
| Sombra de tarjeta | `[BoxShadow(color: Color(0x0A0F1E3C), blurRadius: 2, offset: Offset(0, 1)), BoxShadow(color: Color(0x240F1E3C), blurRadius: 28, spreadRadius: -18, offset: Offset(0, 10))]` |
| Sombra de tarjeta en hover | `0x0F0F1E3C` 2/(0,1) + `0x380F1E3C` blur 32, spread -16, (0,14) → en móvil, mientras se aprieta |
| Sombra de tarjetita de mosaico | `0x0D0F1E3C` 2/(0,1) + `0x380F1E3C` blur 20, spread -10, (0,8) |
| Sombra de popover / calendario | `BoxShadow(color: Color(0x2E0F1E3C), blurRadius: 44, offset: Offset(0, 16))` |
| `shadow-2xl` (modal) | `BoxShadow(color: Color(0x40000000), blurRadius: 50, spreadRadius: -12, offset: Offset(0, 25))` |
| Sombra del primario en hover | `BoxShadow(color: Color(0x592563EB), blurRadius: 20, offset: Offset(0, 8))` → en móvil, mientras se aprieta |
| Halo de foco de input | `BoxShadow(color: Color(0x1F2563EB), spreadRadius: 3)` alrededor del campo |

Prohibido en pantallas nuevas o rediseñadas: `elevation` de Material, `Card`, `AlertDialog`, `SnackBar`,
`showDialog`, `SegmentedButton`, `ChoiceChip`, `ListTile`/`CheckboxListTile`, `LinearProgressIndicator`,
`showDatePicker`, `TextField` sin `inputCampy`, `ElevatedButton`/`FilledButton`/`OutlinedButton` con el estilo del
tema (hasta corregir el tema, siempre con `botonPrimarioCampy` y sus hermanos).

## Íconos

**[D, Agustín 17/10/2026]**
- **Íconos de interfaz** (barra, botones, filas, avisos): lucide, como la web, con `lucide_icons_flutter`; mismo
  nombre que en la pantalla web equivalente. Nunca rellenos de Material.
- **Pictogramas de servicio** (Alojamiento, Comedor, Lavandería, Bienestar, Conectividad, Move, Shift): `IconoServicio`
  de `widgets/ui.dart`, SVG en `assets/iconos/` (trazos de Lucide ISC / Tabler MIT combinados) con `flutter_svg`.
  Estilo de la referencia: recuadro blanco con radio 24 % del lado y borde 1,5 del color del servicio (1,25 por debajo de 56 de lado), glifo de
  línea fina (1.5) del mismo color con puntas redondeadas, insignia opcional abajo a la derecha (círculo blanco con
  borde del color: ✓ Alojamiento, ✦ Lavandería). Tamaños 72 (tarjeta de Servicios), 40 (listas), 32 (filas).
- **«Mi QR» del Inicio** [D, Agustín 19/10/2026, reemplaza lo del 17/10]: cuadrado **azul Campy** (`CampyColors.azul`; navy hasta el 26/10/2026) de 72 con radio 16 y el
  dibujo del QR en blanco (44), sin rótulo («Mi QR» solo para lectores de pantalla). Al tocarlo abre la credencial
  (`home.dart`, `mi_qr.dart`).

## Interacción en móvil

La web tiene hover; el teléfono no. Equivalencias **[propuesta, confirmar con Agustín]**:

| Web | Móvil |
|---|---|
| `hover:` de tarjeta clickeable (borde slate-300 + sombra hover) | mientras se aprieta: borde `bordeControl` + sombra hover, 150 ms; sin `InkWell` con onda (la onda de Material no existe en la web) |
| `hover:bg-blue-700` + sombra del primario | mientras se aprieta: `azulOscuro` + sombra del primario + escala 0.98 (`active:scale-[0.98]`) |
| `hover:bg-slate-50` (secundario), `hover:bg-slate-100` (ícono, fila) | mientras se aprieta, ese mismo fondo |
| foco (`outline` 2 px azul 80 %) | solo con teclado/lector: `FocusableActionDetector` con borde azul 2; los inputs, con borde azul + halo |
| `disabled:opacity-50` | `Opacity(0.5)` y `onPressed: null`; **sin permiso no se deshabilita: no se muestra** |
| `active:scale-[0.98]` | `AnimatedScale(scale: 0.98)` al apretar |

## Piezas: web → Flutter

Cada fila: valores Flutter exactos y qué pieza existe hoy. «Crear» = no existe; va en `widgets/ui.dart` con ese
nombre y se agrega a esta tabla.

### Estructura

| Pieza (web) | Flutter | Hoy en la app |
|---|---|---|
| Cabecera de pestaña | ver «Composición › Cabeceras» (la cabecera navy de 56 con logo y campana es historia) | `barraCampy` `ui.dart:64-85` ✓ (logo como texto ✗); Inicio la arma aparte `home.dart:221-254`; Mi Área usa otra `mi_area.dart:276-288` ✗ |
| Título de pantalla (piezas.md › Encabezado) | `barraCampy(context, titulo: …, atras: true)`: volver y título 17 w700 centrado. `TituloPagina` ya no se usa en ninguna pantalla | `TituloPagina` `ui.dart:144-172`: 30 w800, sub 14 ✗ |
| Título de pestaña interna (h2) | 27 w700 `height 1.0`, sub 14 `gris` a 8 | no existe; cada pantalla usa 24–26 w800 suelto (`roster.dart:484`, ciclo.dart:55, `nueva_solicitud.dart:119`) ✗ |
| Tarjeta (piezas.md › Tarjeta) | `CampyCard`: radio 16, borde `borde` 1, fondo blanco, **sombra de tarjeta**, padding 16; al apretar, «Interacción en móvil» | `CampyCard` `theme.dart:139-162`: sin sombra y con onda de `InkWell` ✗; copias con radio 18–20: `perfil.dart:243-254`, `servicios.dart:333-341`, `notificaciones.dart:206-217` ✗ |
| Título + contexto de tarjeta | 16 w700 + 13 `gris` a 4; del título al contenido, 20 (`mt-5`) | suelto, 14.5–17 w800 |
| Rótulo en mayúscula | 12 w700 `gris` `letterSpacing 1.2` | no se usa |
| Dato en columna (maqueta: Ingreso · Salida) | rótulo 13 `gris`, valor 15 w700 `ink` tabular, pie 12 `gris`; separador vertical 1 × 38 `borde` | `DatoColumna` `ui.dart:43-61` (w800 ✗) y copia `_Dato` `home.dart:344-360` ✗ |

### Chips, badges y avatar

| Pieza (web) | Flutter | Hoy en la app |
|---|---|---|
| Chip de estado (piezas.md › Chip) | `Container(padding: h10 v4, radio 999, fondo tono-50, Border.all(color: texto, width: 1))`, texto 12 w600 `height 1.33`; **sin punto al inicio** [D, Agustín 17/10/2026]: `ChipPunto` ya no dibuja el punto | `EstadoChip` `theme.dart:165-209` (padding 12/4, 12.5 w700, borde claro u opcional ✗); `chipTono` `ui.dart:366-367` ✓ borde; `ChipPunto` `ui.dart:13-40` y `_chip` `home.dart:364-372` sin borde, punto 7 ✗ (con borde [D, 17/10/2026]) |
| Tonos | ok `verde`/`verdeFondo` · espera `ambar`/`ambarFondo` · crítico `rojo`/`rojoFondo` · info `azul`/`azulFondo` · cerrado `gris`/`grisFondo` · IA `#7C3AED`/`#F5F3FF`; borde = texto | `Tono` `ui.dart:347-363`: espera → `naranja` ✗, sin IA (falta también para `INFO_REQUERIDA`) |
| Chip de leyenda (graficos.md) | radio 999, fondo `grisFondo`, padding h14 v6, 13.5 w500 `grisTexto`, punto 10 | `_Leyenda` `roster.dart:631-641`, `_Dot` ciclo.dart:269-279 (12 `gris`, sin fondo) ✗ |
| Contador en pestaña | radio 999, padding h6, alto 18, 11 w700; activa fondo `azul` texto blanco | `CircleAvatar` 10/9 con 11.5 w800 (`roster.dart:107`, `mi_area.dart:1122`) ✗ |
| Avatar (`connect-ui.tsx:119-126`, colores `connect-lib.ts:101-107`) | círculo; iniciales w700; color por nombre: `h = (h * 31 + rune) % 997`, `paleta[h % 6]` con (fondo, texto) = (`#DBEAFE`,`#2563EB`) (`#FFE4E6`,`#BE123C`) (`#D1FAE5`,`#047857`) (`#FEF3C7`,`#B45309`) (`#EDE9FE`,`#6D28D9`) (`#CCFBF1`,`#0F766E`); sin nombre `grisFondo`/`gris`. Tamaños web 28 (10.5) y 40 (12); en la app, 56–64 con iniciales 20 (maqueta) | no existe: crear `AvatarCampy`. Hoy `CircleAvatar` azul fijo w800: `home.dart:265-268`, `perfil.dart:82-86`, `emergencia.dart:161-164`, `mi_area.dart:302-304` ✗ |

### Botones (piezas.md › Botones)

**Nada de emojis en toda la app** [D, Agustín 17/10/2026] (textos, saludos, chips, listas: ni 👋 ni 📍 ni ● ni ✗; si el símbolo
dice algo, va un ícono lucide o un punto dibujado; `tool/chequeo_arb.dart` lo controla en los ARB). Ningún botón lleva emojis ni símbolos en el texto («✓», «📍», etc.) ni el
avioncito de «Enviar». **Los botones van solo con el texto** [D, Agustín 19/10/2026]: sin flecha («Ver traslado», no «Ver traslado →»), sin ícono a la izquierda («Reportar algo», no «⊕ Reportar algo») y sin ícono a la derecha. Quedan afuera los botones que son solo un ícono (sin texto: micrófono, enviar, volver) y el chevron ▾ de un selector que despliega opciones.

| Pieza | Flutter | Hoy en la app |
|---|---|---|
| Primario | [D, 17/10/2026] alto 44, padding h20, radio 20, fondo `azul`, texto 15 w600 blanco; apretado `azulOscuro` + sombra del primario + escala 0.98; deshabilitado opacidad 0.5; solo texto, también si navega (regla 11). Uno solo por vista | `botonPrimarioCampy` `ui.dart:376-387` (alto 48, radio 24, w700 ✗); tema `theme.dart:68-86` (52/14/w700) ✗ |
| Secundario | **gris, nunca azul** **[resuelto]** (`ShiftDAEPage.tsx:148`, `ConveniosPage.tsx:198`; `BTN_SEC` `food-lib.tsx:428` en `FoodPlanificacion.tsx:222, 576`; el contorno azul de la maqueta no va): alto 44, padding h20, radio 20, fondo blanco, borde `bordeControl` 1, texto 14 w600 `grisTexto`; apretado fondo `grisFondoSuave` | no existe: crear `botonSecundarioCampy`. Tema `theme.dart:87-95` (borde `azulBorde`, texto azul, 52/14) ✗ |
| Peligro | como el secundario con borde `rojoBorde`, texto `rojo`; apretado fondo `rojoFondo`. **Es también el botón de confirmar de una confirmación destructiva** **[resuelto]**: contorno rojo, nunca relleno (`ShiftSolicitudesPage.tsx:975`, `ShiftAssignmentsPage.tsx:1302`, `BTN_ROJO` `food-lib.tsx:430`) | no existe: crear `botonPeligroCampy`. `perfil.dart:217-226` ✓ colores, ✗ medidas |
| IA | como el primario con fondo `#7C3AED`, sin ícono de brillito | no existe (no hace falta en Move/Shift) |
| Fantasma | alto 44, padding h16, radio 10, 14 w600 `grisTexto`; apretado `grisFondo` al 70 % | `TextButton` del tema (color del seed) ✗ |
| Enlace | 14.5 w600 `azul`, solo texto (regla 11) | suelto, 13–14.5 w700 ✓ casi |
| De ícono | 32 × 32 visible dentro de 44 tocables, radio 10, ícono 16–18 `grisClaro`; apretado fondo `grisFondo` + `grisTexto`; `tooltip` y `Semantics(label)` traducidos | `IconButton` de Material (`roster.dart:378,387`, `emergencia.dart:797-809` relleno 52) ✗ |
| Botón que guarda | `disabled` mientras dura + spinner 16 blanco `strokeWidth 2` + texto en gerundio del ARB («Enviando…») | spinner 22 solo, sin texto: `nueva_solicitud.dart:240-245`, `login.dart:460-468` ✗ |
| Bloqueado / «Próximamente» | sin botón (un botón deshabilitado no va): chip «Próximamente» y «Muy pronto en Campy» (`TarjetaProximamente`, `EnCamino`) | `TarjetaProximamente` `proximamente.dart:98-114` ✓ (w700) |
| Pie de pantalla (maqueta) | primario a todo el ancho y debajo el secundario a todo el ancho, 10 de separación | suelto |
| Pie de hoja o modal (web) | `Row` con secundario (Cancelar) y primario, cada uno `Expanded`, 12 de separación, línea `grisFondo` arriba y 20 de aire | `confirmarCampy` `ui.dart:110-135` ✓ orden |

### Formularios (piezas.md › Formulario)

| Pieza | Flutter | Hoy en la app |
|---|---|---|
| Etiqueta | 13.5 w600 `gris`, 6 hasta el campo, `*` `#EF4444` | suelta, 16 w800 `ink` (`nueva_solicitud.dart:122`) ✗ |
| Input | alto 44, radio 10, borde `bordeControl` 1, fondo blanco, padding h14, 15 `ink`, pista 15 `grisClaro`; foco borde `azul` 1 + halo; deshabilitado fondo `grisFondoSuave`, texto `gris`; error borde `#EF4444` al 60 %, fondo `#FEE2E2` al 20 %, mensaje 12 w500 `#EF4444` con ícono | `inputCampy` `ui.dart:390-404` (borde `borde`, foco 1.5 sin halo, sin estado de error) ✗ casi; crear `CampoCampy` (envuelve el `TextField` y pinta el halo con `Focus`) |
| Textarea (`ChoferesPage.tsx:460-462`) | `inputCampy` + `maxLines 3`, padding h14 v12, 15, sin redimensionar; contador 11.5 `grisClaro` | `hojaTextoCampy` ✓; sueltos con `OutlineInputBorder()` de Material: `chofer.dart:415-416`, `equipo.dart:108-111`, `emergencia.dart:788-791`, `mi_area.dart:229-232`; con radio 14 y foco del seed: `nueva_solicitud.dart:214-224` ✗ |
| Buscador (piezas.md › Buscador) | alto 44, radio 10 (no píldora), borde `bordeControl`, lupa 15 `grisClaro` a 14, texto a 36, 14 `ink`, foco borde azul **sin halo**; pista sin «…» | `servicios.dart:110-122`: radio 24 ✗ (la maqueta lo dibuja píldora; manda la web) |
| Select (`Combobox.tsx:95-125`) | campo como el input con `keyboard_arrow_down` 15 `grisClaro` a la derecha; abre `elegirCampy` (hoja con opciones 14.5 `ink`, padding h14 v10, elegida con `check` 15 `azul`, tocada `azulFondo`; vacío «Sin coincidencias» 13.5 `grisClaro`) **[propuesta: en móvil el desplegable es una hoja inferior, confirmar con Agustín]** | no existe: crear `elegirCampy`. Hoy hojas con `ListTile` y radio: `notificaciones.dart:111-131`, `mi_area.dart:179-205`, `login.dart:104-150` ✗ |
| Fecha (`DateField.tsx:108-160`) | campo alto 44, radio 10, borde `bordeControl` (abierto `azul`), `calendar_today_outlined` 15 `grisClaro`, fecha 14 centrada; calendario en hoja: barra del mes radio 12 fondo `grisFondo` con botones redondos blancos 32, días de la semana 11 w600 `grisClaro`, día círculo 36 13 tabular, elegido `azul` blanco w700, hoy `azulFondo` `azul` w600, fuera de rango opacidad 0.3, pie «Hoy» 12.5 w600 `azul` y «Cerrar» 12.5 w600 `gris` **[propuesta: hoja inferior en vez de popover]** | no existe: crear `fechaCampy`. Hoy `showDatePicker` de Material `nueva_solicitud.dart:84-91` y campo propio radio 14 w800 `nueva_solicitud.dart:257-276` ✗ |
| Checkbox (`ShiftSolicitudesPage.tsx:1755-1760`) | 16 × 16 visible (20 en móvil **[propuesta]**) dentro de 44 tocables, radio 5, borde `bordeControl` 1, fondo blanco; marcado fondo `azulBordeSuave`, borde `azulBorde`, `check` 11 `azul`; texto 13 `grisTexto` a 10 | no existe: crear `CasillaCampy`. `CheckboxListTile` de Material: `chofer.dart:417-421`, `equipo.dart:112-119` ✗; el login usa una propia rellena (`login.dart:398-443`) |
| Interruptor (`AiConfigPage.tsx:34`) | pista 44 × 24 radio 999, encendido `azul`, apagado `bordeControl`; perilla 20 blanca con sombra, corrimiento 22, 150 ms; chico 36 × 20 / 16 | no existe: crear `InterruptorCampy` (no hay `Switch` en Move/Shift hoy) |
| Login (`login.dart`) | **[resuelto]** el mismo formulario que el resto: input alto 44, radio 10, fondo **blanco**, borde `bordeControl`; botón = primario general (hoy alto 44, radio 20; [D, 17/10/2026]). Ni píldora ni relleno `#F8FAFC`: las tres referencias usan inputs blancos de 44 y radio 10 (`campy-ui.tsx:227`, `ShiftSchemesPage.tsx:374`, `ConveniosPage.tsx:155`) y ningún botón en píldora | `login.dart:160` relleno `#F8FAFC`; botones `login.dart:455-457` (60, radio 10), `:522-524` (58, radio 10) ✗ |
| Tarjeta de opción (estados.md › Seleccionado) | borde 2 `azul` + fondo `azulFondo` al 50 %; no elegida borde 2 `borde`; radio 12 | `nueva_solicitud.dart:126-145` (radio 14, borde 1.6/1) ✗ casi; `emergencia.dart:730-752` ✗ casi |

### Navegación dentro de la pantalla

| Pieza (web) | Flutter | Hoy en la app |
|---|---|---|
| Pestañas (piezas.md › Pestañas de módulo; maquetas Notificaciones y Mis reservas) | `PestanasCampy` [D, Agustín 17/10/2026]: riel `grisFondo` radio 30 sin borde ni sombra, padding 4; pestaña 15 w600; activa fondo `azul` texto blanco, inactiva `gris`; contador opcional en píldora chica | `_Pestanas` `notificaciones.dart:482-511` ✓ casi (13 en vez de 13.5, padding 3) → moverla a `ui.dart` como `PestanasCampy`. Distintas: `roster.dart:74-113`, `chofer.dart:146-163`, `mi_area.dart:1105-1129` ✗ |
| Sub-pestañas | contenedor radio 12 borde `bordeControl` padding 4; pestaña radio 9, padding h16 v8, 13 w600; activa `azulFondo` + `azul`, inactiva `gris` | no se usa |
| Selector de vista (piezas.md › Selector de vista) | píldora fondo `grisFondoSuave` borde `bordeControl` padding 2; opción alto 32 radio 999 padding h14 12.5 w600; elegida blanca, texto `azul`, sombra chica | `roster.dart:253-260, 343-354` (gris `#EDF1F7` radio 14, elegida azul rellena) ✗ |
| Filtros en fila | **[propuesta, confirmar con Agustín; las referencias no lo resuelven: P filtra con `Combobox` en la barra (`FoodPlanificacion.tsx:264-274`), F prende/apaga series con la leyenda]** chips de leyenda que filtran: inactivo fondo `grisFondo` texto `grisTexto` 13.5 w500; activo fondo `azul` texto blanco w600; radio 999, padding h14 v6, `Semantics(selected:)` | `ChoiceChip` de Material `chofer.dart:171`, `emergencia.dart:707-714, 762-768`; propios distintos `roster.dart:551-569`, `mi_area.dart:1131-1149` ✗ |
| Tabla → lista en móvil | **[propuesta, confirmar con Agustín]** sin encabezados: `CampyCard(padding: 0)` con filas padding h16 v14 separadas por línea `borde`; principal 14 w700 `ink`, secundaria 12 `grisClaro`, valor a la derecha 13 `grisTexto`, `chevron_right` 16 `grisClaro`; apretada `grisFondo`; elegida `azulFondo` al 70 %. Sin cebra | `ListTile` sueltos (`roster.dart:441-458`, ciclo.dart:251-266, `chofer.dart:261-300`) ✗; bien encaminadas: filas de `pase.dart:150-173`, `notificaciones.dart:292-357` |
| Paginación → «Ver más» | **[resuelto, P `FoodPlanificacion.tsx:462-466`]** se muestra la primera tanda; al pie, línea `borde` arriba, padding v12 y el enlace «Ver más» 13 w600 `azul` centrado; cada toque suma una tanda sobre lo filtrado y al cambiar un filtro se vuelve a la primera. Sin contador «Mostrando…» (P no lo tiene). Alertas: regla 9 de SKILL.md (3 + «Ver todas las alertas») | `.take(n)` que esconde el resto sin avisar: `equipo.dart:37, 182`, `mi_area.dart:506` ✗ |
| Menú de tres puntos (`MenuAcciones.tsx:44`) | **[propuesta]** hoja inferior con las acciones: 13.5 `ink` padding h14 v10, peligro `rojo` | no se usa |

### Popups y avisos

| Pieza (web) | Flutter | Hoy en la app |
|---|---|---|
| Modal / drawer (piezas.md › Modal; `FormSection.tsx:34-60`, `ShiftColorConfigPage.tsx:499-524`) | en móvil, **hoja inferior** [D, slice E]: radio 16 arriba, fondo blanco, `barrierColor 0x660F172A`, sombra `shadow-2xl`. **Cabecera navy en degradé** (`LinearGradient(topLeft → bottomRight, [navySuave, navy])`, padding 24/24/24/20): título 18 w700 blanco `letterSpacing -0.36`, descripción 13 blanco 60 % `height 1.375`, X 32 × 32 radio 8 con ícono 18 blanco 60 % (apretada blanco 10 %). Cuerpo padding 20, bloques a 20. Pie: «Pie de hoja o modal». Esta cabecera vale para toda hoja y modal [D, 17/10/2026]; la sólida de `FoodModal.tsx:46-54` es un desvío | no existe: crear `hojaCampy(titulo, descripcion, cuerpo, pie)`. Hojas blancas sin cabecera: `ui.dart:98-139, 480-492`, `equipo.dart:71-143`, `mi_area.dart:179-205`, `notificaciones.dart:112-129`, `ui.dart:302-340` (fondo `#EFF4FF`) ✗ |
| Confirmación (estados.md › Avisos) | `hojaCampy` con título «¿…?», una oración en la descripción y pie Cancelar + confirmar. Destructiva: el confirmar es `botonPeligroCampy` (contorno rojo) **[resuelto]**, ver «Botones» | `confirmarCampy` `ui.dart:90-141` (sin cabecera navy, radio 24, título 18 w800) ✗; `AlertDialog` de Material: `shell.dart:136-149`, `mi_area.dart:222-241` ✗ |
| Formulario corto | `hojaCampy` con un `inputCampy` multilínea y el pie | `hojaTextoCampy` `ui.dart:469-559` (sin cabecera navy, título 17 w800, «Volver» como enlace debajo) ✗ casi |
| Toast (`Toast.tsx:44-90`) | fondo y texto por tipo: éxito `#D1FAE5`/`#064E3B`, error `#FEE2E2`/`#7F1D1D`, advertencia `#FEF3C7`/`#78350F`, info `#E0E7FF`/`#312E81`; borde 1 del color del estado al 30 % (`0x4D10B981`, `0x4DEF4444`, `0x4DF59E0B`, `0x4D6366F1`); radio 16, padding h16 v12, sombra `shadow-lg`; ícono 18 (`check_circle_outline`, `error_outline`, `warning_amber_rounded`, `info_outline`), título 14 w600, detalle 12 al 90 %, X 16 al 60 %; dura 5 s; se apilan con 8 de separación. Lugar: arriba, a la altura de la barra de estado + 64, márgenes 16; un toast nuevo reemplaza al anterior, entra con un fundido de 180 ms, vibra según el tono y el texto va en 14 w600 (`avisoCampy`) | `avisoCampy` `ui.dart:406-462`: fondo sólido `ink` o del tono con texto blanco 13 w600, radio 12, sin ícono ni X, 3 s, abajo ✗ |
| Banner de alerta de sitio | franja a todo el ancho, fondo `rojo` (crítico) o `ambar` (pendiente), ícono 20 blanco, texto 12.5 w600 blanco en una línea | `shell.dart:179-224, 322-357` ✓ forma; `naranja` en vez de `ambar` (`shell.dart:200`) y w800 ✗ |
| Aviso informativo en línea (estados.md) | radio 12, fondo `azulFondo` al 70 %, borde `azulBordeSuave`, padding h16 v10, ícono `info_outline` 15 `azul`, texto 13 `grisTexto` | `traslado.dart:183-198` (radio 10, 11.5 `ink`, sin borde) ✗; `indicaciones.dart:228-236` (sin borde, `ink`) ✗ casi; avisos grises `0xFFF8FAFC`: `roster.dart:532-539`, `nueva_solicitud.dart:228-238` ✗ |
| Advertencia en línea | radio 12, fondo `ambarFondo`, borde `ambarBorde`, padding 16, texto 13 `ink` | `CampyCard` `naranjaFondo` (`mi_area.dart:377-391`, `emergencia.dart:287-294`, `nueva_solicitud.dart:197-210`) ✗ tono; `AvisoCaja` `acceso.dart:38-51` |
| Sin conexión / datos guardados | advertencia en línea compacta (padding h16 v6, 12 `ambar`) **[propuesta]** | franja `naranja` `home.dart:82-89`; textos naranjas sueltos `traslado.dart:122-127`, `chofer.dart:254` ✗ |
| Ítem que requiere atención | radio 12, borde `rojoBorde`, fondo `rojoFondo` al 60 %, padding h12 v10; ícono en recuadro 36 radio 8 `#FEE2E2` `#B91C1C` | `EquipoAlertasBloque` `equipo.dart:183-195` (tarjeta blanca con ícono suelto) ✗ |
| Sin alertas | círculo 40 `verdeFondo` con `verified_user_outlined` 20 `#059669` + texto | `equipo.dart:180` (texto suelto) ✗ |
| Aviso grande con ícono (maqueta: «Ya podés hacer tu Check In», «Disponible sin conexión») | tarjeta radio 16 del tono (fondo -50, borde -200), ícono 40 del tono, título 16 w700 `ink`, detalle 13 `grisTexto` | `TarjetaAviso` `ui.dart:175-208` (radio 20, ícono 46, 17 w800, fondo `#EFFAF3`) ✗ casi |
| Tooltip (graficos.md › Tooltip) | **[propuesta]** sin hover no hay tooltip: solo en los botones de ícono, al mantener apretado. `TooltipThemeData(decoration: blanco + borde `borde` + radio 12 + sombra `card-hover`, padding h12 v8, textStyle 13 `ink`)` en `campyTheme()` | `tooltip:` con el estilo gris oscuro de Material (`emergencia.dart:801, 808`, `notificaciones.dart:161`, `login.dart:381`, `shell.dart:241`) |
| Nueva versión (`ActualizacionFlotante.tsx:54`) | botón flotante `azul` radio 14, padding 16/14/20/14, sombra `0x732563EB` blur 36 (0,12); círculo 36 blanco 15 % con ícono 17; título 14 w700 blanco, sub 12 blanco 80 % | `_BarraActualizar` `shell.dart:359-382`: franja `navy` con `TextButton` celeste ✗ |

### Estados de datos (estados.md)

| Estado | Flutter | Hoy en la app |
|---|---|---|
| Vacío | `VacioCampy(icono, titulo, detalle, accion)`: columna centrada, padding vertical 48, ícono 32 `grisIcono` (variante `_outlined`), título 14.5 w600 `gris` a 12, explicación 13 `grisClaro` a 4, acción secundaria a 16 (solo con permiso). En tarjeta chica: ícono + una línea 13 `grisClaro` con el mismo alto del contenido. Dice **qué** falta («Sin traslados asignados»), no «Sin datos» genérico | no existe: crear `VacioCampy`. Hoy texto gris suelto, sin ícono ni título: `traslado.dart:101-108`, `indicaciones.dart:73`, `roster.dart:128, 443, 526`, ciclo.dart:70, `chofer.dart:177`, `equipo.dart:35, 180`, `notificaciones.dart:238-239`, `servicios.dart:128-132`, `mi_area.dart:504` ✗ |
| «—» | valor puntual sin dato | ✓ en general |
| Cargando: tarjeta, KPI, lista | `EsqueletoCampy(alto, ancho, radio)`: bloque `grisFondo` con la forma de lo que viene (título 24 × 96 radio 6; cuerpo radio 10 del alto real), latido de opacidad 1 ↔ 0.5 cada 1 s | no existe: crear `EsqueletoCampy` |
| Cargando: pantalla o lista sin forma conocida | `CargandoCampy` [D, Agustín 19/10/2026]: `AroGirando` de 40, el aro de Campy da una vuelta cada 1,4 s con un pulso de escala 0,92 ↔ 1, centrado con padding vertical 56; con «reducir movimiento» solo late | no existe: crear `CargandoCampy`. Hoy `CircularProgressIndicator()` con el color del seed: `traslado.dart:98`, `indicaciones.dart:70`, ciclo.dart:68, `chofer.dart:73, 250`, `notificaciones.dart:166`, `perfil.dart:118`, `emergencia.dart:406`; `LinearProgressIndicator` `home.dart:834`, `servicios.dart:233` ✗ |
| Error al cargar | `ErrorReintentar`: tarjeta blanca normal, mensaje 13 w600 `gris` (`mensajeError(e)`, nunca `'$e'`), botón «Reintentar» chico (radio 10, borde `bordeControl`, padding h12 v6, 12 w600 `azul`). 403: el mensaje, sin «Reintentar». **No es rojo**: rojo es crítico | `ErrorReintentar` `ui.dart:212-234`: tarjeta roja, texto rojo w700, `OutlinedButton` del tema a todo el ancho ✗; `chofer.dart:71` rojo y sin reintentar ✗ |
| Error al guardar | toast de error con el mensaje del servidor | `avisoCampy(tono: Tono.critico)` ✓ uso, ✗ forma |
| Nunca vacío mientras carga | | ✓ |

### Datos y avance

| Pieza (web) | Flutter | Hoy en la app |
|---|---|---|
| KPI (piezas.md › KPI) | `CampyCard` padding 16; etiqueta 14 `gris` arriba (truncada), número 30 w700 `ink` tabular a 6; el círculo de ícono (56, fondo -50, borde -100, ícono 24) **no va en celular** (`max-sm:hidden`) | no existe: crear `KpiCampy` |
| Mini KPI en fila de 3 | **[resuelto]** el KPI compacto de [P] (`KpiCard compacta`, `FoodPlanificacion.tsx:241-247`; `KpiCard.tsx:56, 60, 64-67`): padding 16, etiqueta 12.5 `gris` arriba truncada, número 24 w700 `ink` tabular a 4 («—» sin dato), sub 11 `grisClaro`; **sin ícono en celular** (F `FoodResumen.tsx:65`). La fila de 3 es composición de la maqueta | `kpi` `chofer.dart:79-89`, `_jornadaCard` `mi_area.dart:1089-1103` (ícono arriba, 22 w800, etiqueta 11.5 abajo), `stat` `home.dart:858-863` (número del color del tono) ✗ |
| Barra de avance (graficos.md › Barras HTML) | **[resuelto]** riel alto 14 radio 999 `grisFondo` `#F1F5F9`, relleno `azul`; rótulo 14 w600 `ink` arriba a 6, valor 14 w600 tabular a la derecha; sin dato, riel vacío y «—» (F `piezas.tsx:421-435`). Variante fina en fila (rótulo a la izquierda, P `food-lib.tsx:415-421`): riel 6 `grisFondo`. El riel `#E5E7EB` de 12 de la maqueta no va: las dos referencias usan slate-100 | `_BarraAvance` `home.dart:447-467` (alto 12, `#E5E7EB`) ✗ casi; `LinearProgressIndicator` `mi_area.dart:594-600` ✗ |
| Anillo / arco (graficos.md) | `CustomPainter`: aro de fondo `grisFondo`, tramos con `StrokeCap.round` y separación (cada tramo se acorta `ancho + 0.6` y se corre `ancho/2 + 0.3` sobre perímetro 100); centro 23 w700 tabular; sin dato, aro gris y «—» | `emergencia.dart:189-197` (cuenta de 3 s: `CircularProgressIndicator` sin `strokeCap: StrokeCap.round`, pista `#FAD3D3`) ✗ detalle |
| Línea de tiempo / pasos | número en círculo 28 `azul` con texto 13 w700 blanco, hilo 2 `azulBorde` | `_Paso` `indicaciones.dart:331-378` ✓ (w800) |
| Calendario de roster | días radio 9 → 10, hoy borde `azul` 2 + w700; colores de fase desde constantes | `roster.dart:405-423` ✓ forma |

## Composición (manda la maqueta donde las tres referencias no dicen nada)

**Emergencia** [D, Agustín 17/10/2026]: todo lo que sea enviar o confirmar (Enviar, Confirmar, Reintentar ahora) y la
opción elegida (ubicación, gravedad) va en **rojo** relleno; los botones de ícono (audio, foto) van sin color (blanco
con borde), salvo el micrófono mientras graba. Alto común 48.

**Formato de app moderna [D, Agustín 17, 19, 20 y 21/10/2026] — manda sobre lo que sigue en esta sección:**
- **Cabeceras** (`barraCampy`):
  - **Inicio:** blanca, alto 72, avatar (44) a la izquierda, «Hola, …» y «Hoy, Lun 19 de Oct» al centro y la campana en
    un `BotonRedondo` (44, borde fino) a la derecha. La campana va **solo** en Inicio.
  - **Servicios, Mi Área y «Servicios en camino»** [D, Agustín 21/10/2026]: **sin cabecera**. Queda solo el alto de la
    barra de estado sobre el fondo de la pantalla; el título lo anuncia el lector de pantalla (`barraCampy(context,
    titulo: …)`). Nada de banda navy.
  - **Perfil:** franja navy con la identidad (avatar 60, nombre 22 w700 blanco) y la tarjeta de accesos montada.
  - **Cori:** sin cabecera (ver «Pantalla de Cori»).
  - **Pantallas a las que se entra:** `barraCampy(context, titulo: …, atras: true)`: `BotonVolver` (chevron «‹» en iOS,
    flecha «←» en Android, sin círculo) y el título centrado, nada a la derecha salvo una acción propia. Sobre navy
    (`sobreNavy: true`) cuando la pantalla es navy: el pase y el respaldo.
  - Siguen navy: el ingreso (cabecera), la puerta de huella o rostro, Mi QR a pantalla completa, el pase, la
    emergencia, la franja de Perfil y el arranque.
- **Barra inferior** [D, Agustín 17, 20 y 21/10/2026] (`shell.dart`): píldora navy flotante de alto 68 con márgenes de
  16 y un **corte en U bajo Cori** (`_BarraCorte`: radio 36, entrada curva 18, franja de 10 debajo; sombra `0x33061333`
  desenfoque 12 corrida 10 hacia abajo). Solo íconos lucide de 22 (Inicio `house`, Servicios `layoutGrid`, Mi Área
  `wrench`, Perfil `user`), los inactivos en blanco al 75 %; la activa en un círculo blanco de 44 a 60 (se achica en
  teléfonos angostos) con el ícono navy, 180 ms. Los nombres van en `Semantics`/`Tooltip`. Entre pestañas, el aire del
  reparto parejo de cada mitad.
  - **Con Cori en su pantalla la barra se contrae** [D, Agustín 21/10/2026]: el corte se achica hasta desaparecer y
    las dos mitades se juntan en el centro con el mismo aire que hay entre pestañas, sin hueco; al volver Cori se
    expande y el corte se abre para recibirlo. Deslizando entre pestañas, 250 ms.
  - **Vuelo de Cori** (`_VueloCori`, 1000 ms): al tocar Cori, una hoja blanca (radio 24 → 0) sube desde la barra
    (0–0,55), Cori viaja y crece hasta su lugar en el chat (0,08–0,8) con un rebote del 6 % al llegar, con los ojos
    abiertos que cierra al llegar; la página cambia cuando la hoja la tapa (0,55). Al ir a otra pestaña, todo al revés
    (el blanco tapa la conversación, la página cambia en 0,3, la hoja baja y Cori vuelve a la barra). Deslizando o con
    «reducir movimiento», sin vuelo. **El vuelo es solo visual y nunca traba la barra**: si falla, la pestaña se
    desliza como antes.
  - El SOS sigue flotando aparte.
- **Cori vivo** (`CoriVivo` + `OjosCori` en `widgets/cori_vivo.dart`) [D, Agustín 20 y 21/10/2026]: imagen
  `cori.png` (82 en la barra, aro de ~62) con ojos dibujados encima. Gestos: **toque** (1,1 s: abre los ojos y los
  cierra contento, escala 1 → 1,08 y rebote de 1,05), **entrada** (2,4 s: abre, mira a la izquierda y a la derecha y
  cierra) y **parpadeo** (1 s: abre, parpadea una vez y cierra). En la barra: entrada al terminar cada arranque
  (`ArranqueCampy.terminadas`) y un parpadeo cada 5 minutos con la app en pantalla (el conteo se frena en segundo
  plano). En el chat: flota (ciclo de 3,2 s, ±3 % del tamaño) y cada 7 s alterna parpadeo y mirada. Con «reducir
  movimiento», quieto.
- **Pantalla de Cori** [D, Agustín 19 y 21/10/2026]: **toda blanca y sin cabecera** (la barra queda en alto 0 solo
  por la barra de estado). Cori de 112 arriba del saludo con la conversación vacía; con mensajes, de 56 arriba de la
  conversación. Sugerencias en píldora (`azulFondo`, borde `azulBorde`, 14,5 w600 azul). Caja de escritura como
  WhatsApp: campo en píldora `grisFondo` de radio 23 y alto mínimo 46; micrófono redondo de 46 en `azulFondo` (rojo
  mientras escucha); enviar redondo de 46 en azul con flecha hacia arriba, nunca el avión de papel. Debajo, el aviso
  «Cori puede equivocarse…» en 11,5 y «Cómo te cuidamos» en el renglón de abajo.
- **Arranque** (`ArranqueCampy` + `AroDesplegado` en `ui.dart`) [D, Agustín 19 y 21/10/2026]: navy con el aro del logo
  de 76 pintado con sus cinco tramos y sus puntitos (no la imagen). Cada vuelta dura 2,1 s: el aro se recoge en sentido
  horario hasta un punto arriba, el punto da una vuelta antihoraria y el aro se despliega en sentido horario. Al estar
  lista la app (mínimo 1,3 s al abrir, 0,6 s al ingresar, máximo 4 s) el aro se completa, toma impulso (1 → 1,1) y se
  aleja girando, y el navy se abre en un círculo (950 ms). `claro: true` lo hace sobre blanco (después del ingreso y del
  desbloqueo). Con «reducir movimiento», quieto y solo se desvanece. Las cargas de pantalla usan `AroGirando`.
- **Ingreso y desbloqueo** (`BotonAlAro` en `ui.dart`) [D, Agustín 21/10/2026]: si el ingreso o el desbloqueo (rostro,
  huella o contraseña) salen bien, el botón se angosta hasta ser un círculo azul (0–0,35), viaja al centro (0,3–0,62)
  y en su lugar se despliega el aro (0,55–0,95), mientras una hoja blanca sube (desde la hoja del ingreso o desde el
  borde de abajo en el desbloqueo); sigue el arranque claro. 1,1 s. La animación nunca impide entrar.
- **Pantalla de ingreso** [D, Agustín 21/10/2026]: cabecera navy con el logo y el selector de idioma (píldora blanco al
  8 % con borde al 18 %, radio 12, bandera 24×18 y el código en mayúsculas «ES», «EN», «KO», «ZH», 15 w600, sin
  flecha; el lector de pantalla dice el nombre completo); hoja blanca de radio 24 con los campos, «¿Olvidaste tu
  contraseña?» a la derecha de la etiqueta Contraseña, el botón y debajo «¿Necesitás ayuda?» y «Contactar a Soporte»
  en dos renglones. Sin «Acceso con QR» ni «Configurar servidor» (en desarrollo el servidor se elige con
  `--dart-define=CAMPY_API_URL`).
- **«En camino»** (`EnCamino` en `proximamente.dart`) [D, Agustín 19 y 21/10/2026]: mosaicos escalonados
  (desplazamientos 14 / 0 / −8 / 0 / 14, separación 8), el chip «Próximamente», un título de 24 w700 y una oración de 15
  `gris`, **centrado de arriba a abajo** en el alto disponible. **Mientras un módulo está «en camino», en esa pestaña no
  se muestra nada más** (ni el rol, ni «Cambiar función», ni otros bloques) [D, Agustín 23/10/2026].
- **El contenido NO cambia con el formato** [D, Agustín 17/10/2026]: el formato de app moderna es solo cabecera, barra
  inferior y estilo; las tarjetas y bloques de cada pantalla (p. ej. «Mi estadía» con la foto, el QR montado y los
  datos debajo; «Para vos») siguen como estaban. No agregar ni rearmar bloques por imitar una referencia.

- Margen lateral 16; entre tarjetas 12; entre secciones 20–22.
- Sin espacios vacíos: el contenido termina pegado a la barra inferior (`SliverFillRemaining(hasScrollBody: false)`);
  las hojas (login) llegan al borde.
- Una tarjeta nunca se estira para llenar la pantalla (`mainAxisSize: MainAxisSize.min`).
- Las tarjetas de una misma sección comparten diseño en todos los roles y fases («Transporte» es la misma para la
  subida y el regreso).
- Textos: **siempre** con las claves de `lib/l10n/app_{es,en,ko,zh}.arb` (+ `flutter gen-l10n`), incluidos sufijos
  como «Hs» y los textos de vacío, carga y error. Faltan claves comunes: `comunSinDatos`, `comunCargando`,
  `comunVerMas` (hoy solo existe `comunReintentar`).

## Modo por módulos (`CAMPY_MODULOS`)

Lo que no está activo se oculta o se muestra como «Próximamente»; nunca se muestran datos de un módulo apagado
(vianda o dieta son de Food; check-in de Stay; tickets e «Informar…» de Connect). Ver `lib/modulos.dart`.

## Checklist de revisión de una pantalla de la app

1. Fuente Inter con sus 4 pesos; nada de `w800`/`w900`; números tabulares.
2. Colores desde `CampyColors` con los valores de la web; nada del `seedColor`; tonos con significado (en curso azul,
   cancelado gris); chip con borde del color del texto.
3. Radios 10/12/16/20/999; fondo blanco y bloques como secciones sin caja (sin sombra de tarjeta); nada de `elevation`, `Card` ni onda de `InkWell`.
4. Sin las piezas de Material prohibidas («Formas, bordes y sombras»).
5. Botones: primario 44/20/15 w600, secundario con borde `bordeControl` y texto `grisTexto`, uno solo primario.
6. Hojas y confirmaciones con cabecera navy en degradé; confirmar destructivo con contorno
   rojo; toast con fondo suave, ícono y 5 s.
7. Vacío (`VacioCampy`), cargando (`EsqueletoCampy`/`CargandoCampy`) y error (`ErrorReintentar` gris) con textos
   en los 4 ARB.
8. Nada inventado, ni de módulos apagados, ni recortado sin «Ver más».
9. Comparada con las tres referencias (dashboard de Food, planificación de Food, Shift) en los valores, con su
   pantalla web equivalente y, en la composición, con su maqueta.
10. Íconos lucide; fondo blanco; barras de avance sobre `grisFondo` (`#F1F5F9`).
11. Textos con mayúscula inicial; códigos cortos enteros en mayúscula («ES»).
12. Animaciones: respetan «reducir movimiento» y nunca traban la navegación ni impiden entrar.

## Rediseño 17/10/2026 (rama `agustin/worker-app-rediseno`)

Ya existen en `widgets/ui.dart` / `theme.dart`: `hojaCampy` + `CabeceraHoja`, `VacioCampy`, `CargandoCampy`,
`EsqueletoCampy`/`EsqueletoTarjetas`, `PestanasCampy<T>` (con contador), `AvatarCampy`, `LogoCampy`,
`IconoServicio`/`estiloServicio` (pictogramas en `assets/iconos/`), `botonSecundarioCampy`, `botonPeligroCampy`,
`Tono.ia`, `CampySombras`, `CampyColors` con los valores de la web (`naranja*` = ámbar; `serv*` = colores de
servicio), `letraCampy`/`respaldoCampy`. Las tablas de arriba con «Hoy en la app (16/10)» quedan como historia: (ciclo.dart se unió a `roster.dart` el 17/10)
Inicio, Servicios y las pantallas de Move/Shift ya están alineadas; falta la etapa 5 (emergencia, chofer, equipo y
módulos ocultos).

**Piezas que se sumaron después (19–21/10/2026)** en `widgets/ui.dart` salvo que se diga: `AroGirando` (carga),
`ArranqueCampy` + `AroDesplegado` (arranque), `BotonAlAro` (ingreso y desbloqueo), `CoriVivo` + `OjosCori`
(`cori_vivo.dart`), `EnCamino` / `MiAreaEnCamino` (`proximamente.dart`), `BotonRedondo` (44 con borde fino),
`BotonVolver`, `MosaicoDato`, `BloqueDestacado` / `FilaDestacada` (superficie tintada radio 20/16, sin ícono),
`AceptoCampy`, `BotonFijoAbajo` (acción principal fija abajo, en la zona del pulgar), `BrilloAlMaximo` (pantallas con
QR), `BanderaIdioma`, `LineaHorarioHoy`, `UnidadGrande`, `BotonSos`, `tinteServicio` (color del servicio al 6 % sobre
blanco). Antes de crear una pieza nueva, buscar si ya existe acá.

**Desvíos conocidos (no copiar):** `AlertDialog` en `bloqueo.dart` («Usar contraseña», con `e.toString()`),
`seguridad.dart` y `senales_riesgo_medico.dart`; el rótulo «BIENVENIDO» del ingreso con el hex suelto `#5B8DEF`; el
rótulo de sección de Perfil en 13 w700 (la norma es 12 w700 con espaciado 1,2); `campyAppBar` navy en
`comunicados.dart` y `lavanderia.dart`.

**Trampa:** el `textStyle` de un `ButtonStyle` **reemplaza** al del tema (no se mezcla): todo `textStyle` de botón
nombra `fontFamily: letraCampy, fontFamilyFallback: respaldoCampy`, o el botón sale con la fuente del sistema.

## Auditoría 16/10/2026 — diferencias en Move/Shift

Pantallas revisadas: `home`, `traslado`, `indicaciones`, `pase`, `roster`, `ciclo`, `nueva_solicitud`, `chofer`,
`equipo`, `emergencia`, `notificaciones`, `servicios`, `perfil`, `login`, `shell`, `mi_area` y `widgets/ui.dart`
(más `theme.dart` y `widgets/proximamente.dart`, que las alimentan). Rama `agustin/worker-app-pulido-2` con cambios
sin commitear: los números de línea pueden correrse. Formato: `archivo:línea` — regla — hoy → debería.

### Rompe reglas del proyecto

- `mi_area.dart:590, 595` — regla 1 (nada inventado) — total de pasos `?? 4` → sin dato, «—» y barra vacía.
- `indicaciones.dart:316`, `notificaciones.dart:423` — regla 7 (textos en los 4 idiomas) — `' Hs'` fijo → clave ARB.
- `equipo.dart:182` — regla 9 (alertas cortas) — `alertas.take(20)` → 3 alertas + fila «Ver todas las alertas» con
  triángulo y contador que abre la lista en una hoja.
- `equipo.dart:37`, `mi_area.dart:506` — nada escondido sin avisar — `.take(10)` / `.take(6)` → «Ver más».
- `equipo.dart:110` (`eqObservacionHint`), `chofer.dart:416` (`chSalvedadHint`) — regla 3 (sin aclaraciones entre
  paréntesis) → título + descripción aparte.
- `traslado.dart:55`, `indicaciones.dart:54`, `roster.dart:58`, ciclo.dart:38, `equipo.dart:90`,
  `chofer.dart:400` — error con el nombre de la excepción en pantalla (`'$e'`, `e.toString()`) → `mensajeError(e)`.

### Se ve distinto a simple vista

1. `theme.dart:53` (+ `pubspec.yaml:86-92`) — tipografía — Roboto → Inter en 4 TTF estáticos con los `cv`/`ss01` de
   la web. Afecta todas las pantallas.
2. `theme.dart:60-67` — cabecera — `AppBar` blanco, raya azul de 3 px y título centrado 18 w800 en
   `traslado.dart:96`, `roster.dart:67`, ciclo.dart:51, `nueva_solicitud.dart:115`, `chofer.dart:248, 410` →
   `barraCampy` + `TituloPagina(atras: true)` como en la maqueta (Próximo traslado, Nueva solicitud).
3. `theme.dart:68-95` — botones — radio 14, alto 52, w700 en todo `ElevatedButton`/`FilledButton`/`OutlinedButton`
   sin estilo propio (`roster.dart:208, 488`, `traslado.dart:270`, `nueva_solicitud.dart:240`,
   `chofer.dart:104, 114, 304, 306, 438`, `equipo.dart:125, 133`, `emergencia.dart:414, 772, 795`,
   `mi_area.dart:469, 613, 618, 680, 691`, `pase.dart:190`, `perfil.dart:217`, `servicios.dart:305`) → primario
   44/20/15 w600; secundario con borde `bordeControl` y texto `grisTexto`. Lo más rápido: corregir el tema.
4. `theme.dart:51` — colores derivados — `ColorScheme.fromSeed` sin `copyWith`: spinners, `RefreshIndicator`,
   `TextButton` (`roster.dart:244, 316`, `chofer.dart:299, 435`, ciclo.dart:261), `ChoiceChip`, `Divider` y foco
   de `TextField` salen en el azul lavado del seed → `copyWith(primary: azul, …)` y `dividerTheme`.
5. `theme.dart:26-28, 33, 39` — colores — `ink #0F172A`, `navy #0F1E3C`, `fondo #F4F6FB`, `verde #16A34A`,
   `naranja #EA580C` como pendiente → `#061333`, `#061333`, `#F1F5F9`, `#047857`, `ambar #B45309`.
6. `theme.dart:149-157` — tarjeta — `CampyCard` sin sombra (toda la app se ve plana) → sombra de tarjeta; además
   copias con radio 18–20: `perfil.dart:243-254`, `servicios.dart:333-341`, `notificaciones.dart:206-217` → `CampyCard`.
7. `ui.dart:412-462` — toast — banda sólida oscura o del tono, texto blanco, 3 s, sin ícono → fondo suave + texto
   -900 + ícono + X, radio 16, 5 s (todas las llamadas a `avisoCampy`).
8. `ui.dart:90-141, 469-559` — hojas — blancas, radio 24, título 17–18 w800 → `hojaCampy` con cabecera navy en
   degradé, radio 16. `shell.dart:136-149` y `mi_area.dart:222-241` usan `AlertDialog` de Material → `confirmarCampy` /
   `hojaTextoCampy`.
9. `theme.dart:165-209`, `ui.dart:13-40`, `home.dart:364-372` — chips — borde claro (`verdeBorde`, `naranjaBorde`) o
   sin borde, 12.5 w700 → borde del color del texto, 12 w600, padding 10/4; también los de punto (`ChipPunto`, `_chip`)
   [D, 17/10/2026]. Llamadas sin borde: `indicaciones.dart:126-127`,
   `chofer.dart:185`, `equipo.dart:51-53`, `mi_area.dart:561-565`; borde claro: `traslado.dart:265-266, 302`,
   ciclo.dart:227, `mi_area.dart:319-324`.
10. `viaje_estado.dart:41-45`, `theme.dart:180-182` — tonos — «En embarque» y «En viaje» en verde, «Cancelado» en
    rojo, `EN_CURSO` de solicitud en verde → en curso `azul`, cancelado `gris`; `INFO_REQUERIDA` en gris → **violeta**
    (`#7C3AED` sobre `#F5F3FF`, borde del color del texto) [D, 17/10/2026].
11. Estados vacíos (ver tabla «Vacío»: 13 lugares) — texto gris suelto → `VacioCampy` con ícono, título y explicación.
12. `ui.dart:212-234`, `chofer.dart:71` — error — tarjeta roja con botón ancho → tarjeta normal gris con «Reintentar»
    chico.
13. `roster.dart:74-113`, `chofer.dart:146-163`, `mi_area.dart:1105-1129` — pestañas — gris `#EDF1F7` con la activa
    blanca y subrayado o borde azul → píldora azul rellena (`_Pestanas` de `notificaciones.dart:482-511` a `ui.dart`).
14. `chofer.dart:283-289` `SegmentedButton`; `chofer.dart:171`, `emergencia.dart:707, 762` `ChoiceChip`;
    `chofer.dart:261, 277, 295`, `roster.dart:449`, ciclo.dart:253, `emergencia.dart:302`, `notificaciones.dart:121`,
    `perfil.dart:327`, `mi_area.dart:193` `ListTile`; `chofer.dart:417`, `equipo.dart:112` `CheckboxListTile` —
    piezas de Material → piezas propias de esta guía.
15. `nueva_solicitud.dart:84` — fecha — `showDatePicker` de Material → `fechaCampy`.
16. Inputs con `OutlineInputBorder()` de Material o sin foco azul: `chofer.dart:415-416`, `equipo.dart:108-111`,
    `emergencia.dart:788-791`, `mi_area.dart:229-232`, `nueva_solicitud.dart:214-224`, `servicios.dart:110-122` →
    `inputCampy` (buscador radio 10, alto 44).
17. `pase.dart:81-103` — composición — cabecera azul rellena en el ticket → la maqueta la muestra blanca, con
    «Base Salta → Campamento Norte» en `ink` y el tipo de ingreso en `gris`.
18. `servicios.dart:318-368` — composición — tarjeta activa con ícono en círculo chico, título `ink` y acción como
    enlace → como la maqueta y como `TarjetaProximamente`: recuadro de ícono grande, título del color del servicio,
    chip y botón primario «Ver …» (sin flecha desde el 19/10).
19. `mi_area.dart:276-288` — cabecera — aro + título + campana de Material → `barraCampy` + `TituloPagina`.
20. `traslado.dart:98`, `indicaciones.dart:70`, ciclo.dart:68, `chofer.dart:73, 250`, `notificaciones.dart:166`,
    `perfil.dart:118`, `emergencia.dart:406`; `home.dart:834`, `servicios.dart:233`, `mi_area.dart:594` — cargando —
    spinner del seed o barra de Material → `EsqueletoCampy` / `CargandoCampy`.
21. `shell.dart:359-382` — nueva versión — franja navy → botón flotante azul de la web.
22. `equipo.dart:125-128` — peligro — «Rechazar» con texto rojo y borde azul claro del tema → `botonPeligroCampy`.
23. `ui.dart:74`, `home.dart:234`, `login.dart:218-227` — logo — «campy» escrito en Roboto w800 → `logo-white.png`.

### Detalle fino

- **Pesos** — `w800`/`w900` → `w700`. Conteo: `emergencia` 20, `mi_area` 19, `home` 17, `traslado` 16, `roster` 14,
  `ciclo` 12, `chofer` 12, `ui.dart` 9, `indicaciones` 8, `nueva_solicitud` 8, `notificaciones` 8, `equipo` 5,
  `shell` 5, `login` 4, `perfil` 4, `pase` 3, `theme.dart` 3, `servicios` 2, `proximamente` 2.
- **Títulos de pantalla** — 24 w700: `ui.dart:161` (30), `home.dart:100` (27), ciclo.dart:55 (26),
  `emergencia.dart:151` (26), `emergencia.dart:684` (28), `notificaciones.dart:174` (30); sub 13.5: `ui.dart:165` (14).
- **Títulos de tarjeta** — 16 w700: `traslado.dart:175, 207, 261, 295, 317, 336, 359`, `roster.dart:132, 195, 314, 523`,
  ciclo.dart:98, 106, 225, `chofer.dart:92, 135, 144, 258, 275, 293`, `equipo.dart:30, 175`,
  `indicaciones.dart:200, 242, 252`, `perfil.dart:264`, `mi_area.dart:452, 481, 514` (hoy 14.5–18 w800).
- **Números** — 30 w700 `ink` tabular: `home.dart:412` (30 azul), `home.dart:503` (34 azul), `traslado.dart:240`;
  24 w700: `traslado.dart:383`, `indicaciones.dart:315` (22), `home.dart:860` (del color del tono → `ink`),
  `roster.dart:546` (20 del tono).
- **Hex sueltos** → constantes: `home.dart:457` `#E5E7EB`, `home.dart:579` `#EFF4FF`, `home.dart:831` `#ECFAFD`,
  `home.dart:840` `#F59E0B`/`#FFF7E6`; `indicaciones.dart:249` `#F1FAF4`; `roster.dart:76, 255` `#EDF1F7`,
  `roster.dart:326, 585` y `notificaciones.dart:278` `#F1F5F9`; `roster.dart:533`, `nueva_solicitud.dart:229`
  `#F8FAFC`; ciclo.dart:87, 205, 241 `#86EFAC`, ciclo.dart:158 `#DCE9FB`, ciclo.dart:169 `#E8F7EE`,
  ciclo.dart:233 `#93B8ED`; `emergencia.dart:194, 678` `#FAD3D3`, `emergencia.dart:665` `#7DA2E8`;
  `notificaciones.dart:432` `#FBBF24`, `notificaciones.dart:521` `#EFFAF3`, `notificaciones.dart:530` `#D1FAE5`;
  `pase.dart:77` `Colors.black`; `login.dart:160, 280, 301`; `ui.dart:184, 305`.
- **Input** — `ui.dart:399-401` — borde `borde` y foco 1.5 sin halo → `bordeControl`, foco 1 + halo.
- **Duplicados** — `home.dart:344-360` `_Dato` = `DatoColumna`; `home.dart:364-372` `_chip` = `ChipPunto`;
  `perfil.dart:243-254` `_Tarjeta` = `CampyCard`.
- **Botón primario de la app** — `ui.dart:376-387` (48/24/w700) y CTAs sueltos `indicaciones.dart:273-285` (50/25),
  `home.dart:615-627` (48/24) → 44/20/15 w600.
- **Botones de contorno azul** — `indicaciones.dart:133-141, 288-301, 388-399`, `traslado.dart` (tema) → secundario
  **gris** (`botonSecundarioCampy`, resuelto 17/10).
- **Barra de avance** — `home.dart:455-462` — alto 12, `#E5E7EB` → 14, `grisFondo` `#F1F5F9` (resuelto 17/10).
- **Login** — `login.dart:160` relleno `#F8FAFC` → fondo blanco y borde `bordeControl`; botones `login.dart:455-457`
  (60, radio 10) y `:522-524` (58, radio 10) → primario general 44 / radio 20 (resuelto 17/10: ni píldora ni 56–60).
- **Confirmación destructiva** — `confirmarCampy` con relleno `#DC2626` → confirmar con `botonPeligroCampy` (contorno
  rojo, resuelto 17/10).
- **Avatares** — `home.dart:265-268`, `perfil.dart:82-86`, `emergencia.dart:161-164`, `mi_area.dart:302-304` →
  `AvatarCampy` (color por nombre, w700).
- **Contadores** — `roster.dart:107`, `mi_area.dart:1122` — `CircleAvatar` → píldora 11 w700.
- **Hero del Inicio** — `home.dart:312` sombra navy 10 % blur 24 → sombra de tarjeta; `home.dart:322-325` «Mi QR» con
  `elevation: 4` → sombra.
- **Separadores** — `Divider`/`VerticalDivider` sin color (`traslado.dart:149, 219`, `roster.dart:169`,
  ciclo.dart:113, 231, `emergencia.dart:235, 237`, `perfil.dart:195-208`, `pase.dart:136-142, 159`,
  `home.dart:666, 668`) → `dividerTheme` con `borde`.
- **Avisos en línea** — `traslado.dart:183-198` (11.5 `ink`, radio 10, padding 8) → 13 `grisTexto`, radio 12,
  padding h16 v10, borde `azulBordeSuave`; `indicaciones.dart:228-236` sin borde.
- **Franja sin conexión** — `home.dart:82-89` naranja 12 → advertencia `ambar`.
- **Banners** — `shell.dart:191, 206, 221, 351` w800 → w600–w700; `shell.dart:200` `naranja` → `ambar`.
- **Hojas** — radio 18–24 → 16: `equipo.dart:74`, `mi_area.dart:181`, `notificaciones.dart:115`, `login.dart:108`,
  `ui.dart:101, 306, 484`.
- **Botón que guarda** — `nueva_solicitud.dart:241-244`, `login.dart:460-468` — spinner sin texto → spinner 16 +
  gerundio.
- **«Próximamente»** — `proximamente.dart:50` chip con fondo `fondo` y borde `borde` → slate con borde `gris`;
  `proximamente.dart:44, 94` w800; `proximamente.dart:82, 89` radio 22.
- **`TarjetaAviso`** — `ui.dart:191-200` — radio 20, ícono 46, 17 w800, detalle `ink` → radio 16, ícono 40, 16 w700,
  detalle `grisTexto`.
- **`mostrarAlojamiento`** — `ui.dart:305-311` — fondo `#EFF4FF`, radio 24, título 20 w800 → `hojaCampy`.
- **Emergencia** — `emergencia.dart:140, 387, 668` título w800, `emergencia.dart:397` w900 → w700;
  `emergencia.dart:191-196` anillo sin puntas redondeadas.
- **Íconos** — mezcla de rellenos y de contorno (`traslado.dart:210` `directions_bus`, `chofer.dart:263`
  `check_circle`, `roster.dart:138` `business`) → lucide como la web (resuelto 17/10, ver «Íconos»); mientras no
  esté el paquete, `_outlined`.
- **Textos fijos menores** — `perfil.dart:232` «Campy Worker App» (nombre propio, probablemente legítimo),
  `login.dart:598` URL de ejemplo como pista.
- **SOS** — `shell.dart:238-244` `FloatingActionButton` de Material 3 (cuadrado redondeado con `elevation`) → ver Dudas.

### Dudas para confirmar con Agustín

Resueltas el 17/10/2026 mirando las tres referencias (quedan como regla en su tabla): botón secundario (gris),
login (input 44 blanco radio 10, primario general), fondo (`#F1F5F9`), barra de avance (14, `#F1F5F9`),
confirmación destructiva (contorno rojo), íconos (lucide). Decididas por Agustín el 17/10/2026 [D]: cabecera de
modal y hoja (degradé navy de Shift), botón (44 / radio 20), chip con punto (con borde del color del texto) e
`INFO_REQUERIDA` (violeta). Sigue abierta:

- ~~**SOS flotante.**~~ Resuelto [D, Agustín 26/10/2026]: **redondo** (círculo rojo de 60, borde blanco 2, sombra `0x59DC2626` blur 18 (0,8), ícono blanco 30, 0,94 al apretar; `BotonSos` `ui.dart`). **No va en el Inicio**: sin el cartel «¿Necesitás ayuda urgente?»; flota en las otras pestañas y en Cori.
