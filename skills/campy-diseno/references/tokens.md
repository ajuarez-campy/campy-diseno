# Tokens y valores

Origen de cada valor entre corchetes: **[F]** dashboard de Food (campyprov), **[P]** planificación de Food
(campyprov, `features/food/FoodPlanificacion.tsx` y lo que importa), **[S]** Shift (campisoft), **[D]** decidido
con el usuario al armar la skill.

## Tokens de Tailwind que existen en los dos repos

| Token | Valor | Uso |
|---|---|---|
| `campy-ink` | `#061333` | todo texto principal |
| `campy-navy`, `-navy-soft`, `-navy-deep`, `-navy-mid` | `#061333` `#0C1F4A` `#040E26` `#112657` | encabezado de modal (degradado), menú |
| `campy-paper` / `campy-paper-alt` | `#FAFAFC` / `#F4F5F9` | fondo del body |
| `campy-muted` | `#64748B` (= slate-500) | equivale a `text-slate-500` |
| `action-blue` | `#2563EB` (= blue-600) | **el azul de Campy**: primario, hoy, enlaces, foco |
| `action-purple` | `#8B5CF6` | IA |
| `status-ok/warn/crit/info` (+ `-soft`) | `#10B981` `#F59E0B` `#EF4444` `#6366F1` | toasts |
| `rounded-card` | 16px | tarjetas, popovers, modales |
| `rounded-card-sm` | 12px | subtarjetas, tooltips, avisos en línea, tarjetitas de mosaico |
| `rounded-input` | 10px | inputs, selects, botones de ícono, contenedores de tabla en panel |
| `rounded-pill` | 999px | chips, píldoras, leyendas |
| `shadow-card-hover` | `0 8px 30px -4px rgba(0,0,0,.12), 0 3px 8px -3px rgba(0,0,0,.06)` | tooltips y globos |

**No usar:** `campy-blue` (no existe en campisoft), `rounded-action`/`rounded-dialog`,
`shadow-premium-*` (el CSS global los redefine distinto del config), `bg-gradient-cta` (primario navy viejo).

Valores **sin token** (se escriben literales; en pantallas nuevas, en minúscula: [F] los escribe en mayúscula, da igual para el color):

| Qué | Valor |
|---|---|
| Sombra de tarjeta | `shadow-[0_1px_2px_rgba(15,30,60,0.04),0_10px_28px_-18px_rgba(15,30,60,0.14)]` |
| Sombra de tarjeta en hover | `hover:shadow-[0_1px_2px_rgba(15,30,60,0.06),0_14px_32px_-16px_rgba(15,30,60,0.22)]` |
| Sombra de tarjetita de mosaico | `shadow-[0_1px_2px_rgba(15,30,60,0.05),0_8px_20px_-10px_rgba(15,30,60,0.22)]` |
| Sombra de popover (fecha, combobox) | `shadow-[0_16px_44px_rgba(15,30,60,0.18)]` |
| Sombra del modal de Food [P] (desvío, ver «Choques») | `shadow-[0_24px_60px_-20px_rgba(6,19,51,0.45)]` (`FoodModal.tsx:43`) |
| Sombra del primario en hover | `hover:shadow-[0_8px_20px_rgba(37,99,235,0.35)]` |
| Halo de foco de input | `focus:shadow-[0_0_0_3px_rgba(37,99,235,0.12)]` |
| Radio de botón | `rounded-[20px]` [D] |
| Separador | `border-[#f1f5f9]` (= `border-slate-100`, preferir la clase) |

## Tipografía

Familia: Inter variable (`font-sans`), pesos 400/500/600/700. Mono (JetBrains) solo para códigos y hex.

| Rol | Clases | Origen |
|---|---|---|
| Título de pantalla (h1) | `text-[24px] sm:text-[30px] font-bold text-campy-ink leading-tight` | [D]. Shift usa `text-[30px]` fijo con cabecera `flex items-center gap-3.5` (`ShiftHubPage.tsx:35-37`); en [F] el 24/30 es el `h2` de la pestaña Resumen (`FoodResumen.tsx:393`) y el `h1` del módulo es `CabeceraPantalla` de 28 px (`campy-ui.tsx:30`) |
| Subtítulo de pantalla | `text-[13.5px] text-slate-500` | F, S |
| Título de pestaña interna (h2) | `text-[27px] font-bold text-campy-ink tracking-tight leading-none` | [D, Agustín 21/10/2026] (Shift tenía 26 y 28) |
| Subtítulo de pestaña | `mt-2 text-[14px] text-slate-500` | S |
| Título de tarjeta / panel | `text-[16px] font-bold text-campy-ink leading-snug` | F, S |
| Subtítulo de tarjeta | `text-[13px] text-slate-500` | F |
| Rótulo en mayúscula | `text-[12px] font-bold uppercase tracking-[0.1em] text-slate-500` | F [D] |
| Número de cabecera / KPI | `text-[30px] font-bold tabular leading-none text-campy-ink` (24px si pasa 6 caracteres, 22px si pasa 9) | F, S |
| Etiqueta de KPI | `text-[14px] text-slate-500` (arriba del número) | F, S |
| Contexto bajo el número | `text-[13px] text-slate-500` | F |
| Número mediano (mosaico, mini KPI) | `text-[24px] font-bold leading-none tabular` | F |
| Encabezado de tabla | `text-[12px] font-bold uppercase tracking-[0.06em] text-slate-400` | F [D] |
| Celda | `text-[13px] text-slate-600` | F, S |
| Celda principal | `text-[14px] font-bold text-campy-ink` | S |
| Línea secundaria | `text-[12px] text-slate-400` | S |
| Etiqueta de formulario | `text-[13.5px] font-semibold text-slate-500` (+ `<span className="text-red-500">*</span>`) | S |
| Input, select | `text-[15px]` | S |
| Botón primario / secundario | `text-[15px]` / `text-[14px]` `font-semibold` | S |
| Chip de estado | `text-[12px] font-semibold` | S [D] |
| Chip de leyenda | `text-[13.5px] font-medium text-slate-600` | F |
| Tooltip | `text-[13px]`, título `text-[13.5px] font-bold`, pie `text-[12px]` | F |
| Ejes de gráfico | `fontSize 12`, `fill #64748b` | F |
| Enlace | `text-[13px] font-semibold text-action-blue hover:underline` | S, P (`FoodPlanificacion.tsx:273, 464`) |
| Título de la pantalla de planificación (h2 dentro del módulo) | `text-[20px] font-bold text-campy-ink` + sub `text-[13.5px] text-slate-500` (ver «Choques») | P `FoodPlanificacion.tsx:209-210` |
| Título de sección fuera de tarjeta | `text-[16px] font-bold text-campy-ink` | P `FoodPlanificacion.tsx:475` |
| Título de sección dentro de modal o formulario | `text-[12px] font-bold uppercase tracking-[0.12em] text-action-blue mb-2.5` (Shift: `tracking-[0.1em]`) | P `FoodPlanificacion.tsx:674`, `food-lib.tsx:377`; S `ConveniosPage.tsx:293` |
| KPI compacto (fila de 5) | etiqueta `text-[12.5px] text-slate-500`, número `text-[24px] font-bold tabular`, sub `text-[11px] text-slate-400` | P `KpiCard.tsx:56, 64, 67` |
| Total de una celda de día | `text-[17px] font-bold tabular text-campy-ink` | P `FoodPlanificacion.tsx:287` |
| Número de una celda de servicio | `text-[22px] font-bold tabular text-campy-ink` | P `FoodPlanificacion.tsx:334` |
| Píldora chica de dato (origen, dieta) | `text-[10.5px] font-bold` / `font-semibold` | P `FoodPlanificacion.tsx:44, 357` |

`leading-none` en números y títulos grandes; `leading-snug` en nombres que pueden ir en dos renglones
(`line-clamp-2`).

## Grises por rol

| Rol | Clase |
|---|---|
| Texto principal, números | `text-campy-ink` |
| Valores de tabla | `text-slate-600` |
| Secundario, rótulos, contexto | `text-slate-500` |
| Terciario, `th`, placeholder, «—» | `text-slate-400` |
| Ícono de estado vacío | `text-slate-300` |
| Borde de tarjeta | `border-slate-200/80` |
| Borde de input, botón secundario | `border-slate-200` (se ve slate-300 por el CSS global) |
| Separadores, filas | `border-slate-100`, `divide-y divide-slate-100` |
| Fondo de riel / esqueleto | `bg-slate-100` |
| Fondo de chip de leyenda | `bg-slate-100` (`#f1f5f9`) |

## Espaciado y grilla

- Página: `space-y-5`. Cabecera: `flex flex-col sm:flex-row sm:items-start justify-between gap-3`.
- KPIs: `grid grid-cols-2 sm:grid-cols-3 auto-rows-fr gap-3 sm:gap-4` [F]
  (Shift: `grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-4`; planificación, cinco compactos:
  `grid-cols-2 md:grid-cols-3 xl:grid-cols-5 gap-3.5` [P] `FoodPlanificacion.tsx:241`).
- Contenido + panel lateral: `grid xl:grid-cols-[1.4fr_1fr] gap-4 items-start` [P] `FoodPlanificacion.tsx:249`.
- Tarjetas: `grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4`.
- Tarjeta: `p-4 sm:p-5`; KPI `p-5` (`max-sm:p-4`). Del título al visual: `mt-5`.
- Vista lista + detalle: `lg:grid-cols-[340px_1fr] gap-5` (Shift Asignaciones; Solicitudes y DAE usan `xl:grid-cols-[360px|340px_minmax(0,1fr)] gap-4`).
- Barra de filtros: `p-4 flex items-center gap-3 flex-wrap` dentro de una tarjeta [P] `campy-ui.tsx:158`.
- Breakpoints de Tailwind por defecto; sin ancho máximo de página.

## Íconos (lucide-react 0.408)

| Uso | size / strokeWidth |
|---|---|
| KPI (en círculo `h-14 w-14 rounded-full border` con fondo -50) | 24 / 1.8 |
| Íconos de tarjeta, mosaico | 20–22 / 2 |
| Cerrar modal, toasts | 18 (modal de Food: 17, `FoodModal.tsx:53`) |
| Ícono de la cabecera del modal de Food, en cuadrado `h-10 w-10 rounded-[10px] bg-white/10` | 18 [P] |
| Ícono de servicio en una celda, escudo de viabilidad | 16 / 14 [P] |
| Botones, buscador | 15 |
| Chevron de fila | 16 `text-slate-400` |
| Estado vacío | 32 / 1.5 `text-slate-300` |
| Dentro de chip | 11–12 |

El color va por `className` de texto (currentColor). Íconos decorativos con `aria-hidden`; los que dan
información (triángulo de riesgo) con `role="img"` y `aria-label={t(…)}`.

## Choques entre las tres referencias

Las tres pantallas de referencia ([F], [P], [S]) mandan sobre todo lo demás, pero en estos puntos **no coinciden
entre sí**. No se elige uno por cuenta propia: vale la columna «Hoy vale». Las filas en negrita las decidió
Agustín (17/10/2026) y son firmes; lo que queda del otro lado es un **desvío** que no se copia en pantallas nuevas.
En el resto, hasta que decida, vale lo que la guía marca [D].

| Qué | [F] dashboard | [P] planificación | [S] Shift | Hoy vale |
|---|---|---|---|---|
| Botón primario / secundario | — | alto 40, `rounded-[10px]`, 13.5 px (`food-lib.tsx:428-429`): **desvío** | alto 44, `rounded-[20px]`, 15 / 14 px (`ShiftDAEPage.tsx:150, 155`) | **[S] [D, 17/10/2026]** |
| Título de la pantalla dentro de un módulo | `h2` 24/30 px `leading-tight` (`FoodResumen.tsx:393`) | 20 px (`FoodPlanificacion.tsx:209`) | **dos valores**: 28 px `tracking-tight leading-none` en Solicitudes (`ShiftSolicitudesPage.tsx:462`), Calendario, DAE, Colores; 26 px en Asignaciones, Esquemas y Horarios | **27 px [D, Agustín 21/10/2026]** |
| Borde del chip de estado (también el chip con punto) | del color del texto, `rounded-[20px]` 12 px (`TarjetasPestana.tsx:33-34`) | tono -200, 11.5 px (`food-lib.tsx:175-212, 261`): desvío | tono -200 (`ShiftSolicitudesPage.tsx:129-133`); chip con punto sin borde (`HistogramaPage.tsx:322-329`): desvío | **color del texto [F] [D, 17/10/2026]; sin punto al inicio [D, Agustín 17/10/2026]** |
| Cabecera de modal | — | `bg-campy-ink` sólido (**desvío**), ícono en cuadrado blanco 10 %, título 17, sub 12.5 al 70 % (`FoodModal.tsx:46-54`) | degradé navy de `DrawerHeader`, título `text-lg`, sub 13 al 60 % (`ShiftColorConfigPage.tsx` › `ModalShell`) | **[S] degradé navy, también en hojas de la app [D, 17/10/2026]** |
| Etiqueta / input de formulario | — | 12.5 px `mb-1` / 14 px, sin halo (`campy-ui.tsx:227-228`) | 13.5 px `mb-1.5` / 15 px con halo (`ShiftAssignmentsPage.tsx:658-659`, `horarios/horarios-lib.ts:138-139`) | [S] [D]: ya es igual en todos los formularios de Shift |
| Encabezado y celda de tabla | `th` 12 px `tracking-[0.06em]` (`FoodResumen.tsx:239`) | `th` 11.5 px `tracking-wide` `px-3 py-2.5`, `td` `px-3 py-3` (`food-lib.tsx:345-348`), columnas centradas (`FoodPlanificacion.tsx:429`) | `th` **11 px** `uppercase tracking-[0.06em] text-slate-400`, `px-5`/`px-4` `py-3` (`ShiftAssignmentsPage.tsx:300`); Solicitudes y Convenios 11 px `font-bold tracking-wide` | **12 px [D, Agustín 21/10/2026]**; los 11 px de Shift son desvío |
| Sub-pestañas | — | subrayado azul 3 px en caja blanca `rounded-[12px]` (`campy-ui.tsx:185-199`, usado en `FoodPlanificacion.tsx:252`) | **tres formas**: píldora azul rellena en el primer nivel (`ShiftHubPage.tsx:43-53`); `bg-blue-50` dentro de una tarjeta `p-1.5` (`ShiftSolicitudesPage.tsx:500-506`); riel gris `bg-slate-100/80` con la activa blanca (`horarios/ShiftHorariosPage.tsx:70-74`, como el riel de la app) | primer nivel [S]; segundo nivel: **el del módulo en que se trabaja [D, Agustín 21/10/2026]** |
| Aviso en línea | — | `rounded-[10px] px-3.5 py-2.5 text-[12.5px] font-medium` (`food-lib.tsx:433-441`) | uno parecido al de estados.md (`ShiftSolicitudesPage.tsx:658`) | estados.md (`rounded-card-sm`, 13 px) |
| Rojo para un número que baja | — | delta negativo `text-red-500`, egresos `text-red-500` (`FoodPlanificacion.tsx:348, 448`) | — | **un número que baja va en rojo [D, Agustín 21/10/2026]** |
| Violeta fuera de IA | — | solo IA (`FoodPlanificacion.tsx:387-397`: «el único morado es Ver explicación») | `INFO_REQUERIDA` violeta (`ShiftSolicitudesPage.tsx:133`); también la «versión» de un esquema (`ShiftSchemesPage.tsx:184`) | **violeta ya no es exclusivo de IA: IA, `INFO_REQUERIDA` y Bienestar [D, 17/10/2026]**; la versión de esquema también **[D, Agustín 21/10/2026]** |
| Vacío dentro de una lista o tira | ícono + una línea | solo la línea `text-[13px] text-slate-400` (`FoodPlanificacion.tsx:295, 367, 498`) | ícono de 28–36 + una línea; Horarios y Calendario solo la línea | estados.md › Vacío |
| Selector de vista | píldora `bg-slate-50` con la activa blanca (`Segmentado`, `ServiciosVista.tsx`) | — | rectangular `rounded-[10px]` con la activa azul rellena (`CalendarioPage.tsx:293-298`) | **el del módulo en que se trabaja [D, Agustín 21/10/2026]** |
| Color del ícono de un KPI | un tono por KPI, decorativo: raciones ámbar, servicio actual sky, población violeta, producción teal, stock rojo, equipo esmeralda (`FoodResumen.tsx:214-226`) | azul | azul | **se permite: tono decorativo en el ícono del KPI [D, Agustín 21/10/2026]** |
| Fila de alerta y «Ver todas» | llevan chevron a la derecha (y «Ver todas» triángulo) | — | — | **la fila que navega lleva chevron [D, Agustín 21/10/2026]** |
| Mes en una fecha larga | en minúscula («15 de octubre», `FECHA_LARGA`) | — | — | **mes con mayúscula también en la web [D, Agustín 21/10/2026]**: `FECHA_LARGA` en minúscula es desvío |
