# Piezas de referencia

Fragmentos para copiar. Antes de copiar, **buscá si ya existe un componente** en el repo
(`apps/web/src/components/ui/` —en los dos repos `campy-ui.tsx` y `KpiCard.tsx`; ojo: en campisoft `KpiCard` es el
formato viejo con zócalo y `campy-ui.tsx` trae `btnAzul`/`btnBlanco` de radio 12 y opacidad 40, que son desvío—,
`features/food/dashboard/piezas.tsx` (`TarjetaPestana`, `Total`, `SeparadorTotales`, `Segmentado`, `PillHoy`,
`ChipAlerta`, `TituloTarjeta`, `BarrasPorCategoria`, `CHIP_LEYENDA`, `FECHA_LARGA`), `features/food/food-lib.tsx`, `features/food/FoodModal.tsx`) y reusalo. Todos los textos van con `t()`; acá se ven como `t('…')`.

Origen: **F** = dashboard de Food (campyprov `apps/web/src/features/food/FoodResumen.tsx` + `dashboard/`) ·
**P** = planificación de Food (campyprov `features/food/FoodPlanificacion.tsx` + `FoodModal.tsx`, `food-lib.tsx`) ·
**S** = campisoft `apps/web/src/features/shift/`. Donde dos orígenes no coinciden, ver tokens.md › «Choques».

## Encabezado de pantalla (F `FoodResumen.tsx`, S `ShiftHubPage.tsx`)

```tsx
<div className="flex flex-col sm:flex-row sm:items-start justify-between gap-3">
  <div>
    <h1 className="text-[24px] sm:text-[30px] font-bold text-campy-ink leading-tight">{t('….titulo')}</h1>
    <p className="text-[13.5px] text-slate-500">{t('….subtitulo')}</p>
  </div>
  {/* acciones o selector de fecha (w-full sm:w-[210px]) */}
</div>
```

## Pestañas de módulo (S `ShiftHubPage.tsx:43-56`) [D]

En Shift son **rutas**: un `NavLink` por sub-ruta (pone `aria-current` solo). Pestañas de Shift hoy: Solicitudes,
Asignaciones, Calendario, Horarios, Esquemas, DAE, Colores (Convenios pasó al menú lateral; Cobertura e Histograma están
ocultas y con estilo viejo: **no son referencia**).

```tsx
<nav className="flex flex-wrap gap-1 rounded-[30px] border border-slate-200/80 bg-white px-1 py-1 shadow-[0_1px_2px_rgba(15,30,60,0.04)]">
  {tabs.map((x) => (
    <NavLink key={x.to} to={x.to}
      className={({ isActive }) => cn('rounded-[20px] px-3.5 py-2.5 text-[13.5px] font-semibold transition-colors',
        isActive ? 'bg-action-blue text-white' : 'text-slate-500 hover:text-campy-ink')}>
      {x.label}
    </NavLink>
  ))}
</nav>
```

En pantallas nuevas, `bg-action-blue` (Shift escribe `bg-[#2563eb]`, que es el mismo color sin token).

Sub-pestañas dentro de una pantalla: **cada módulo conserva la suya** [D, Agustín 21/10/2026]; al trabajar en un módulo se usa la que ya
tiene, y en uno nuevo se pregunta. Las formas de [S]:
- Dentro de una tarjeta (`ShiftSolicitudesPage.tsx:500-506`): `card p-1.5 flex flex-wrap items-center gap-1`, pestaña
  `rounded-[9px] px-4 py-2 text-[13px] font-semibold`, activa `bg-blue-50 text-action-blue`, inactiva
  `text-slate-500 hover:text-slate-700 hover:bg-slate-50`. Contador `rounded-pill px-1.5 text-[11px] font-bold`, solo
  si es mayor que 0; en la activa toma el tono del estado (`:172-175`).
- Riel gris (`horarios/ShiftHorariosPage.tsx:70-77`, nuevo 19–20/10): `flex w-fit flex-wrap items-center gap-1
  rounded-[14px] bg-slate-100/80 p-1` con `role="tablist"`; pestaña `px-4 py-2 rounded-[10px] text-[13.5px]
  font-semibold`, activa `bg-white text-campy-ink shadow-[0_1px_2px_rgba(15,30,60,0.08)]`. Es la misma idea que el riel
  de la Worker App (`PestanasCampy`).
La planificación [P] usa otra forma para sus sub-solapas: `SolapasModulo` de `campy-ui.tsx:185-199` (caja blanca
`rounded-[12px] border-slate-200/80 px-2 py-1`, pestaña `px-3 py-2.5 text-[13px] font-semibold`, activa
`text-action-blue` con subrayado `after:h-[3px] after:rounded-full after:bg-action-blue`). Es un choque entre
referencias (tokens.md › «Choques»): no se mezcla en una pantalla nueva sin preguntar.

## Selector de vista (segmentado) — F `dashboard/piezas.tsx` → `Segmentado<T>` [D]

Usá `Segmentado<T>` (genérico; además frena el clic para que no llegue a la tarjeta). El de abajo es el mismo dibujo
(`SelectorVistaServicios` de `ServiciosVista.tsx`). Shift tiene otro, rectangular con la activa azul rellena
(`CalendarioPage.tsx:293-298`): es un choque (tokens.md).

Dos o tres opciones que cambian cómo se ve el mismo dato («Por comida / Por comedor»). Píldora, como
los chips de estado:

```tsx
<div className="inline-flex rounded-pill border border-slate-200 bg-slate-50 p-0.5">
  {opciones.map((x) => (
    <button key={x.id} type="button" onClick={() => setVista(x.id)} aria-pressed={vista === x.id}
      className={cn('h-8 rounded-pill px-3.5 text-[12.5px] font-semibold transition-colors',
        vista === x.id ? 'bg-white text-action-blue shadow-sm' : 'text-slate-500 hover:text-campy-ink')}>
      {x.label}
    </button>
  ))}
</div>
```

## Tarjeta con cabecera (F `dashboard/piezas.tsx` → `TarjetaPestana`)

En campyprov **usá `TarjetaPestana`** (resuelve carga, error, vacío, número, contexto y aviso). Forma:

```tsx
<div role="button" tabIndex={0} onClick={onVer} onKeyDown={enterOEspacio(onVer)}
  className="flex flex-col rounded-card border border-slate-200/80 bg-white p-4 sm:p-5
    shadow-[0_1px_2px_rgba(15,30,60,0.04),0_10px_28px_-18px_rgba(15,30,60,0.14)]
    cursor-pointer transition-all hover:border-slate-300
    hover:shadow-[0_1px_2px_rgba(15,30,60,0.06),0_14px_32px_-16px_rgba(15,30,60,0.22)]
    focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-action-blue/40">
  <div className="flex flex-wrap items-center justify-between gap-2">
    <h3 className="text-[16px] font-bold leading-snug text-campy-ink">{t('….titulo')}</h3>
    <span className="whitespace-nowrap text-[30px] font-bold leading-none tabular text-campy-ink">{fmtNum(n)}</span>
  </div>
  <p className="mt-1 text-[13px] text-slate-500">{t('….contexto')}</p>
  <div className="mt-5">{/* visual: alto fijo h-[190px] */}</div>
</div>
```

Totales con rótulo encima (varios lado a lado): `Total` (`rotulo`, `valor`, `ayuda`, `azul`) y `SeparadorTotales` de
`dashboard/piezas.tsx:43-56`, en `flex items-start gap-6 sm:gap-8` (`TarjetasPestana.tsx:312`, `GraficoDemanda.tsx:208`).
Rótulo `text-[12px] font-bold uppercase tracking-[0.1em] text-slate-500`, valor `mt-1 text-[30px] font-bold tabular
leading-none`, ayuda `mt-1.5 text-[12.5px] text-slate-500`.

## KPI (F `components/ui/KpiCard.tsx`, S inline en cada pestaña)

Etiqueta arriba, número en tinta, ícono a la derecha en círculo con fondo -50 del tono, **centrado en alto**
(`items-center`, `KpiCard.tsx:62`). Sin zócalo de color. Cada KPI lleva su `tone` (`FoodResumen.tsx:214-226`); el número
va en el tono solo si es una alerta (`valorEnTono`). Un valor no numérico de más de 12 caracteres baja a `text-[16px]
leading-tight` (`KpiCard.tsx:54-56`). El `KpiCard` de campisoft es el formato viejo (zócalo `border-b-[3px]`): no se
toma como referencia.
En celular el círculo del ícono se oculta y el padding baja a 16 (F `FoodResumen.tsx:65`, `KPI_MOVIL`).
**Compacta** [P] (fila de 5, `KpiCard compacta` en `FoodPlanificacion.tsx:241-247`; `KpiCard.tsx:56-70`): `p-4`,
etiqueta `text-[12.5px]`, número `text-[24px]` a `mt-1`, sub `text-[11px] text-slate-400 truncate mt-1`, círculo
`h-11 w-11` con ícono 20. Sin dato, «—» (`KpiCard.tsx:50`).

```tsx
<div className="flex items-center justify-between gap-3 rounded-card border border-slate-200/80 bg-white p-5 max-sm:p-4 shadow-[…tarjeta…]">
  <div className="min-w-0">
    <p className="truncate text-[14px] text-slate-500">{t('….kpi')}</p>
    <p className="mt-1.5 whitespace-nowrap text-[30px] font-bold leading-none tabular text-campy-ink">{fmtNum(v)}</p>
  </div>
  <span className="flex h-14 w-14 shrink-0 items-center justify-center rounded-full border border-blue-100 bg-blue-50 text-action-blue max-sm:hidden">
    <Users size={24} strokeWidth={1.8} aria-hidden />
  </span>
</div>
```

## Chip de estado [D]

```tsx
const TONO = {
  ok:     'bg-emerald-50 text-emerald-700 border-emerald-700',
  espera: 'bg-amber-50 text-amber-700 border-amber-700',
  critico:'bg-red-50 text-red-600 border-red-600',
  info:   'bg-blue-50 text-action-blue border-action-blue',
  cerrado:'bg-slate-100 text-slate-500 border-slate-500',
  ia:     'bg-violet-50 text-violet-600 border-violet-600',
} as const;

<span className={cn('inline-flex items-center gap-1 whitespace-nowrap rounded-pill border px-2.5 py-1 text-[12px] font-semibold', TONO[tono])}>
  {etiqueta}
</span>
```

**Chip con punto: ya no se usa** [D, Agustín 17/10/2026]: toda bala de estado va sin punto (SKILL.md, regla 10). Lo que sigue queda como referencia de los existentes, que son desvío. Antes: **también con borde del color del texto** [D, 17/10/2026], como el dashboard (`TarjetasPestana.tsx:33-34`):
punto `h-1.5 w-1.5 rounded-full bg-current` + `gap-1.5`. Los bordes -200 de [P] y [S] (`food-lib.tsx:261`,
`ShiftSolicitudesPage.tsx:129-133`) y el chip con punto sin borde de Shift (`HistogramaPage.tsx:322-329`) son desvíos.
`INFO_REQUERIDA` (solicitudes de Shift) va en el tono `ia` (violeta): el violeta ya no es exclusivo de IA [D, 17/10/2026].

El mapa estado → tono va en un `.ts`; la etiqueta se traduce al leer con `etiquetas(…)` / `etiquetasCfg(…)` de
`@/lib/i18n`, en los dos repos (campisoft `lib/i18n.ts:103,115`).

## Botones (S `ShiftAssignmentsPage.tsx`, `ShiftDAEPage.tsx`) [D]

Las pantallas de Shift todavía ponen íconos en botones con texto («Nueva asignación» con `Plus`, «Exportar» con
`Download`, «Configuración», «Generar con IA» con `Sparkles`): es desvío de la regla 11 y no se copia. Shift también usa
`#1d4fd8` para el hover (no es blue-700 `#1d4ed8`): en pantallas nuevas, `hover:bg-blue-700`.

```tsx
const BTN = 'inline-flex h-11 items-center justify-center gap-2 rounded-[20px] px-5 font-semibold transition-all active:scale-[0.98] disabled:cursor-not-allowed disabled:opacity-50';
const BTN_PRIMARIO   = `${BTN} text-[15px] text-white bg-action-blue hover:bg-blue-700 hover:shadow-[0_8px_20px_rgba(37,99,235,0.35)] disabled:hover:shadow-none`;
const BTN_SECUNDARIO = `${BTN} text-[14px] border border-slate-200 bg-white text-slate-600 hover:bg-slate-50`;
const BTN_PELIGRO    = `${BTN} text-[14px] border border-red-200 bg-white text-red-600 hover:bg-red-50`;
const BTN_IA         = `${BTN} text-[15px] text-white bg-violet-600 hover:bg-violet-700 hover:shadow-[0_8px_20px_rgba(124,58,237,0.35)]`;
const BTN_ICONO      = 'inline-flex h-8 w-8 items-center justify-center rounded-input text-slate-400 hover:bg-slate-100 hover:text-slate-600';
```

**Ningún botón lleva el ícono de brillito de IA (`Sparkles`)**, tampoco los violetas de Campy AI: el violeta ya dice que es IA [D].

**Alto 44 y radio 20 en todo botón** [D, 17/10/2026]. Los `BTN_PRI`/`BTN_SEC`/`BTN_ROJO` de `food-lib.tsx:428-430`
(alto 40, `rounded-[10px]`, 13.5 px) son un **desvío**: no se copian. Sí coinciden en el secundario **gris** y el
peligro de **contorno rojo**.
Botón chico dentro de una franja o fila [P]: `h-8 px-3 rounded-[8px] text-[12px] font-semibold` (`FoodPlanificacion.tsx:394-396`);
secundario dentro de la cabecera de una tarjeta: el secundario con `h-9` (`:312-313`).

Orden en un pie: secundario (Cancelar) y después primario, `flex justify-end gap-3`. Un solo primario por
vista. Botón de ícono siempre con `aria-label` y `title` traducidos.

## Formulario (S `ShiftAssignmentsPage.tsx`) [D]

```tsx
const LBL   = 'mb-1.5 block text-[13.5px] font-semibold text-slate-500';
const INPUT = 'block h-11 w-full rounded-input border border-slate-200 bg-white px-3.5 text-[15px] text-campy-ink placeholder:text-slate-400 transition-all focus:border-action-blue focus:outline-none focus:shadow-[0_0_0_3px_rgba(37,99,235,0.12)] disabled:cursor-not-allowed disabled:bg-slate-50 disabled:text-slate-500';

<label className={LBL}>{t('….campo')} <span className="text-red-500">*</span></label>
<input className={INPUT} placeholder={t('….placeholder')} />
```

Selects: `Combobox` y fechas: `DateField` de `components/ui` (mismo alto, radio y foco). Buscador (placeholder **sin «…»**: `t('….buscar')` → «Buscar servicio»).

### Buscador (S `ShiftAssignmentsPage.tsx`) [D]

Igual que el de Shift › Asignaciones: **radio de input (10 px), no píldora**, alto 44, lupa 15 a la izquierda,
texto 14 px, borde azul al foco **sin halo**. Ocupa el ancho que sobra en la barra de filtros (`flex-1 min-w-[220px]`).
Vale para todo buscador: barra de filtros, buscador dentro de un wizard o de un panel.

```tsx
const BUSCADOR = 'h-11 w-full rounded-input border border-slate-200 bg-white pl-9 pr-3 text-[14px] text-campy-ink placeholder:text-slate-400 transition-all focus:border-action-blue focus:outline-none';

<div className="relative flex-1 min-w-[220px]">
  <Search size={15} className="pointer-events-none absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" aria-hidden />
  <input type="search" value={busca} onChange={(e) => setBusca(e.target.value)}
    placeholder={t('….buscar')} aria-label={t('….buscar')} className={BUSCADOR} />
</div>
```
Secciones de formulario: `text-[16px] font-bold text-campy-ink`, `space-y-5` entre secciones.

## Tabla [D]

```tsx
<div className="overflow-x-auto">
  <table className="w-full min-w-[640px]">
    <thead className="border-b border-slate-100">
      <tr>
        <th className="px-5 py-3 text-left text-[12px] font-bold uppercase tracking-[0.06em] text-slate-400">{t('….col')}</th>
        <th className="px-4 py-3 text-left text-[12px] font-bold uppercase tracking-[0.06em] text-slate-400">…</th>
      </tr>
    </thead>
    <tbody className="divide-y divide-slate-100">
      <tr className="cursor-pointer transition-colors">
        <td className="px-5 py-3.5">
          <p className="text-[14px] font-bold text-campy-ink">{nombre}</p>
          <p className="text-[12px] text-slate-400">{detalle}</p>
        </td>
        <td className="px-4 py-3.5 text-[13px] text-slate-600">{valor}</td>
      </tr>
    </tbody>
  </table>
</div>
```

Sin zebra. Fila seleccionada `bg-blue-50/70`. Primera y última columna `px-5`, el resto `px-4`. Dentro de un
panel, el contenedor lleva `rounded-input border border-slate-200`.

Paginación (fuera de la tarjeta; `ShiftSolicitudesPage.tsx:666-690`, `ShiftAssignmentsPage.tsx:426-450`): 20 filas
por página; texto `text-[13px] text-slate-500`; números `h-8 min-w-8 px-1 text-[13px] font-semibold rounded-[8px]
border border-slate-200 bg-white text-slate-500 hover:border-slate-300`, hasta 5; chevrons 14 **con `aria-label`**
(Shift no lo pone: desvío); página activa `border-action-blue bg-blue-50 text-action-blue`; deshabilitado
`disabled:opacity-40`. El calendario suma «Filas por página» (10/25/50).

## Modal (S `ShiftColorConfigPage.tsx` → `ModalShell` + `components/ui/FormSection.tsx` → `DrawerHeader`)

```tsx
createPortal(
  <div className="fixed inset-0 z-50 grid place-items-center bg-slate-900/40 p-4" onClick={cerrar}>
    <div role="dialog" aria-modal="true" onClick={(e) => e.stopPropagation()}
      className="sin-scrollbar max-h-[90vh] w-full max-w-[640px] overflow-y-auto overflow-x-hidden rounded-card bg-white p-5 pt-0 shadow-2xl">
      <DrawerHeader title={t('….titulo')} description={t('….desc')} />
      {/* cuerpo: space-y-5 */}
      <div className="flex justify-end gap-3 border-t border-slate-100 pt-5">
        <button className={BTN_SECUNDARIO}>{t('common.cancelar')}</button>
        <button className={BTN_PRIMARIO}>{t('….guardar')}</button>
      </div>
    </div>
  </div>, document.body)
```

La X de cerrar la pone `DrawerHeader` con el `onClose` que le da el contexto del modal: copiá `ModalShell`
(S `ShiftColorConfigPage.tsx`), que ya lo provee, en vez de armar el contenedor a mano.
**Cabecera de todo modal y de toda hoja de la app: este degradé navy** [D, 17/10/2026].
Encabezado navy (`DrawerHeader`): `bg-gradient-to-br from-campy-navy-soft to-campy-navy`, título
`text-lg font-bold text-white`, descripción `text-[13px] text-white/60`. Escape cierra. Anchos: 480 chico ·
520 · 560 confirmación · 640 formulario · 720 · 760 (`ModalHorario`) · 820 formulario grande · 860. Pie del modal
`pt-5 mt-5 border-t border-slate-100 flex justify-end gap-3 flex-wrap` (`horarios/horarios-ui.tsx:33`). En campyprov,
`components/ui/Modal.tsx` ya trae la cabecera de `DrawerHeader`; en campisoft sigue `ModalShell`.

## Tarjetita de mosaico con franja (F `dashboard/TarjetasPestana.tsx` → `TarjetaDietas`)

```tsx
<li className={cn('flex min-w-0 cursor-grab flex-col overflow-hidden rounded-xl border bg-white active:cursor-grabbing shadow-[0_1px_2px_rgba(15,30,60,0.05),0_8px_20px_-10px_rgba(15,30,60,0.22)]',
  riesgo ? 'border-red-200' : 'border-slate-100')} title={nombre}>
  <div className="flex h-10 shrink-0 items-center justify-between px-3"
    style={{ background: riesgo ? '#fee2e2' : fondo, color: riesgo ? '#dc2626' : color }}>
    <span className="flex h-7 w-7 items-center justify-center rounded-full bg-white" aria-hidden><Icono size={16} strokeWidth={2} /></span>
    {riesgo && <span className="flex h-7 w-7 items-center justify-center rounded-full bg-white text-red-600" role="img" aria-label={t('….riesgo')}><AlertTriangle size={15} strokeWidth={2.2} /></span>}
  </div>
  <div className="flex flex-1 items-start justify-between gap-2 px-3 pb-3 pt-2.5">
    <p className={cn('line-clamp-2 min-w-0 text-[14px] leading-snug', riesgo ? 'font-bold text-red-700' : 'font-medium text-slate-600')}>{nombre}</p>
    <p className={cn('shrink-0 text-[24px] font-bold leading-none tabular', riesgo ? 'text-red-600' : 'text-campy-ink')}>{fmtNum(n)}</p>
  </div>
</li>
```

Grupos con mini título (rótulo en mayúscula; el de riesgo en `text-red-600` con el conteo a la derecha),
primero lo crítico.
**Alto fijo** [D]: la grilla usa `gridAutoRows: '108px'` (nunca `minmax(…, 1fr)`): con pocas tarjetitas no
se agrandan y el alto que sobra queda libre al pie de la tarjeta.

## Planificación de Food [P]

Pantalla que convierte la demanda en raciones: cabecera con navegador de semana, KPI compactos, sub-solapas
(Calendario semanal · Demanda por servicio · Escenarios) a la izquierda y panel de viabilidad a la derecha
(`grid xl:grid-cols-[1.4fr_1fr] gap-4 items-start`, `FoodPlanificacion.tsx:249`). **No hay arrastre ni grilla de
calendario mes/semana**: el «calendario semanal» es una tira horizontal de celdas de día.

### Cabecera con navegador de semana (`FoodPlanificacion.tsx:207-238`)

```tsx
<div className="flex items-end justify-between flex-wrap gap-3">
  <div>{/* título y sub: ver tokens.md › Choques (27 px [D, Agustín 21/10/2026]) */}</div>
  <div className="flex items-center gap-2.5 flex-wrap">
    <div className="inline-flex items-center gap-1 h-10 px-2 rounded-input bg-white border border-slate-200">
      <button type="button" aria-label={t('….semana_anterior')} title={t('….semana_anterior')}
        className="h-7 w-7 rounded-[7px] text-slate-500 hover:bg-slate-100" onClick={() => mover(-7)}>‹</button>
      <span className="px-1 text-[12.5px] font-semibold tabular text-slate-600">{fmtFecha(desde)} — {fmtFecha(hasta)}</span>
      <button type="button" aria-label={t('….semana_siguiente')} title={t('….semana_siguiente')}
        className="h-7 w-7 rounded-[7px] text-slate-500 hover:bg-slate-100" onClick={() => mover(7)}>›</button>
    </div>
    <button className={BTN_SECUNDARIO}><RefreshCw size={15} aria-hidden /> {t('….actualizar')}</button>
  </div>
</div>
```

El original no tiene `aria-label` en ‹ › (`:215, 217`) y calcula la fecha con `toISOString()` (`:202`): no copiar
eso (CLAUDE.md reglas 4 y 7).

### Tira de días (celda de día seleccionable) (`FoodPlanificacion.tsx:277-296`)

```tsx
<div className="flex gap-2 overflow-x-auto pb-1">
  {dias.map(([f, total, est]) => (
    <button key={f} type="button" onClick={() => setDiaSel(f)} aria-pressed={activo === f}
      className={cn('min-w-[118px] rounded-card-sm border-2 px-3 py-2.5 text-center transition-colors',
        activo === f ? 'border-action-blue bg-blue-50/50' : 'border-slate-200 bg-white hover:border-slate-300')}>
      <p className="text-[12px] font-semibold uppercase tracking-wide text-slate-500">{diaCorto(f)}</p>
      <p className="text-[17px] font-bold tabular text-campy-ink">{fmtNum(total)}</p>
      <p className={cn('inline-flex items-center gap-1 text-[11px] font-semibold',
        est === 'VALIDADO' ? 'text-emerald-600' : est === 'PLANIFICADO' ? 'text-action-blue' : 'text-slate-400')}>
        ● {etiquetaEstado(est)}
      </p>
    </button>
  ))}
</div>
```

- **`border-2` en todas las celdas**, elegida o no, para que la selección no corra el contenido 1 px (`:282`).
  Un solo borde azul, **sin `ring`** (`:276`). Es la misma regla que estados.md › Seleccionado (tarjeta de opción).
- Día de la semana en MAYÚSCULAS; el estado del día como texto con punto, **sin chip** (verde validado, azul
  planificado, gris borrador). Encabezado de día de tabla en dos líneas: `text-[11px] font-bold uppercase
  tracking-wide text-slate-400` + `text-[13px] font-semibold text-campy-ink uppercase` («VIE» / «11 SEP», `:437-440`).
- Sin días: `text-[13px] text-slate-400 py-6 px-2` (`:295`).

### Detalle del día y celdas de servicio (`FoodPlanificacion.tsx:299-370`)

Tarjeta `CARD p-4`: título `text-[16px] font-bold` con la fecha larga capitalizada, sub `text-[12.5px] text-slate-500`
y a la derecha secundarios `h-9`. Debajo, `grid sm:grid-cols-2 gap-3 mt-3` de celdas:

```tsx
<div className={cn('rounded-card-sm border p-3.5', riesgo ? 'border-amber-200 bg-amber-50/50' : 'border-slate-200 bg-white')}>
  <div className="flex items-center justify-between">
    <span className="inline-flex items-center gap-2 text-[13.5px] font-bold text-campy-ink"><Icono size={16} aria-hidden /> {servicio}</span>
    {riesgo ? <span className="rounded-pill bg-amber-100 px-2 py-0.5 text-[11px] font-semibold text-amber-700">{t('….supera')}</span>
            : <EstadoChip estado={estado} />}
  </div>
  <p className="mt-1 text-[22px] font-bold tabular text-campy-ink">{fmtNum(n)}</p>
  <p className="text-[12px] text-slate-500">{horario}</p>
</div>
```

Riesgo de capacidad = **ámbar** (no rojo: no es crítico). Desglose en píldoras chicas blancas
`rounded-pill border border-slate-200 bg-white px-2 py-0.5 text-[10.5px] font-semibold text-slate-600` con el número
en `text-campy-ink` (`:357`). Píldora de origen del dato: con dato `border-emerald-200 bg-emerald-50 text-emerald-700
text-[10.5px] font-bold`; **sin dato, borde punteado** `border-dashed border-slate-300 bg-white text-slate-500` (`:44, 50`).

### Panel lateral con barras finas (viabilidad) (`FoodPlanificacion.tsx:523-546`)

Tarjeta `CARD p-4 space-y-3.5`, título `text-[15.5px] font-bold`. Cada fila: rótulo fijo `w-44 text-[13px]
font-semibold text-slate-600` → escudo 14 (`ShieldCheck` `text-emerald-500`, `ShieldAlert` `text-amber-500` en riesgo,
`text-slate-300` sin dato) → barra fina → valor `w-10 text-right text-[12.5px] font-bold tabular` («—» sin dato).
Barra fina (`food-lib.tsx:415-421`): riel `h-1.5 rounded-full bg-slate-100`, relleno `bg-emerald-500` /
`bg-amber-400` / `bg-action-blue`. Es la variante en fila; la barra con rótulo encima es la de F (`FilaBarra`, 14 px).
Al pie, si hay algo que resolver, el «ítem que requiere atención» de estados.md (`:539`); si no,
`text-[12px] text-slate-400`.

### Franja de recomendación de IA (`FoodPlanificacion.tsx:387-405`)

`rounded-input border border-violet-100 bg-violet-50/60 px-3.5 py-2.5 flex items-center justify-between flex-wrap gap-2`;
texto `text-[12.5px] font-semibold text-violet-700`. Botones chicos `h-8 px-3 rounded-[8px] text-[12px] font-semibold`:
el de IA `bg-violet-600 hover:bg-violet-700 text-white` («Ver explicación»), el de acción **azul**
(`bg-action-blue hover:bg-blue-700`): **el único violeta es lo que es IA** (`:392`). El original pone `Sparkles` 14
en el texto (no en un botón); la regla de piezas › Botones (sin brillito en botones) sigue valiendo.
Señales consideradas: cajitas `rounded-input border border-slate-200 p-3` con título `text-[13px] font-bold truncate`,
detalle `text-[11.5px] text-slate-500` y chip a la derecha; en el modal, ícono en cuadro `h-9 w-9 rounded-[9px]` del
tono (`:592`).

### Lista de escenarios (`FoodPlanificacion.tsx:474-499`)

Encabezado de sección **fuera de tarjeta**: `text-[16px] font-bold text-campy-ink` a la izquierda y el primario a la
derecha (`:474-477`). Cada ítem `CARD p-4 flex items-start justify-between gap-3 flex-wrap`: nombre
`text-[14.5px] font-bold` + chip + tipo `text-[11.5px] font-semibold uppercase tracking-wide text-slate-400`; detalle
`text-[13px] text-slate-500`; a la derecha número `text-[20px] font-bold tabular` y su rótulo `text-[11.5px] text-slate-400`.

### Modal de Food (`FoodModal.tsx`) — la cabecera es un desvío

```tsx
<div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/40 p-4" onClick={cerrar}>
  <div role="dialog" aria-modal="true" aria-label={titulo} onClick={(e) => e.stopPropagation()}
    className="flex max-h-[calc(100vh-2rem)] w-full max-w-lg flex-col rounded-card bg-white shadow-[0_24px_60px_-20px_rgba(6,19,51,0.45)]">
    <div className="flex shrink-0 items-center gap-3 rounded-t-card bg-campy-ink px-5 py-4">
      <span className="grid h-10 w-10 shrink-0 place-items-center rounded-input bg-white/10 text-white"><CalendarDays size={18} aria-hidden /></span>
      <div className="min-w-0 flex-1">
        <p className="truncate text-[17px] font-bold leading-tight text-white">{titulo}</p>
        <p className="mt-0.5 text-[12.5px] text-white/70">{sub}</p>
      </div>
      <button type="button" onClick={cerrar} aria-label={t('….cerrar')}
        className="grid h-8 w-8 place-items-center rounded-[8px] text-white/60 transition-colors hover:bg-white/10 hover:text-white"><X size={17} /></button>
    </div>
    <div className="overflow-y-auto p-5">{/* cuerpo */}</div>
    <div className="flex shrink-0 flex-wrap items-center justify-end gap-2.5 px-5 pb-5 pt-1">
      <span className="mr-auto text-[12px] text-slate-500">{t('….nota')}</span>{/* opcional, a la izquierda */}
      <button className={BTN_SECUNDARIO}>{t('….cerrar')}</button>
      <button className={BTN_PRIMARIO}>{t('….aplicar')}</button>
    </div>
  </div>
</div>
```

Cierra con clic afuera, X y Escape (`FoodModal.tsx:33-38`). Anchos `max-w-lg` (512) por defecto, `max-w-xl` (576)
para formulario. Con un `Combobox` adentro, el cuerpo no recorta (`desbordar`, `:29`). **La cabecera sólida
`bg-campy-ink` con ícono es un desvío** [D, 17/10/2026]: todo modal nuevo lleva la cabecera en degradé navy de Shift
(piezas › Modal, `ShiftColorConfigPage.tsx:499-524`). De `FoodModal` valen el cuerpo, el pie y el cierre.
Dentro: secciones con título azul en mayúscula `text-[12px] font-bold uppercase tracking-[0.12em] text-action-blue
mb-2.5` (`FoodPlanificacion.tsx:674`); detalle en solo lectura como filas `rounded-input border border-slate-200 px-4 py-3`
con nombre a la izquierda y número `text-[15px] font-bold tabular` + desglose `text-[11px] text-slate-400` a la derecha
(`:555-563`).

### Tarjeta de ajuste con stepper ± (`FoodPlanificacion.tsx:629-639, 690-699`)

Tarjeta `rounded-card-sm border border-slate-200 p-4`, título `text-[13.5px] font-bold`, ayuda
`text-[11.5px] text-slate-500 mb-3`. Stepper: botones `h-9 w-9 rounded-[9px] border border-slate-200 bg-white
text-slate-600 hover:border-slate-300 disabled:opacity-40 disabled:cursor-not-allowed` con `Minus`/`Plus` 15 y
`aria-label` traducido; valor `min-w-[56px] text-center text-[17px] font-bold tabular`.

### Barra de filtros (`components/ui/campy-ui.tsx:134-182`, usada en `FoodPlanificacion.tsx:264-274, 417-423`)

Tarjeta `p-4 flex items-center gap-3 flex-wrap`: buscador (piezas › Buscador, igual), después los `Combobox` con ancho
mínimo (`w-56` → `min-w-[14rem]`, nunca se encogen por debajo del texto, `:131-132`), y al final, en el slot
`acciones` con `ml-auto`, el enlace «Limpiar» `h-11 px-2 text-[13px] font-semibold text-action-blue hover:underline
whitespace-nowrap` (`FoodPlanificacion.tsx:273`). Si no entra, baja entero a una segunda línea a la derecha.
Opción «todos» del selector como primera opción con valor vacío.

### «Ver más» por tandas (`FoodPlanificacion.tsx:462-466`)

En vez de paginar: al pie de la tarjeta `flex justify-center border-t border-slate-100 py-3` con el enlace
`text-[13px] font-semibold text-action-blue hover:underline`; cada clic suma una tanda (dos días) **sobre el resultado
filtrado**, y al cambiar un filtro se vuelve a la primera tanda (`:200`).

## Estado vacío [D]

```tsx
<div className="flex flex-col items-center justify-center py-12 text-center">
  <CalendarX size={32} strokeWidth={1.5} className="text-slate-300" aria-hidden />
  <p className="mt-3 text-[14.5px] font-semibold text-slate-500">{t('….vacio_titulo')}</p>
  <p className="mt-1 text-[13px] text-slate-400">{t('….vacio_desc')}</p>
  {puedeCrear && <button className={cn(BTN_SECUNDARIO, 'mt-4')}>{t('….crear')}</button>}
</div>
```

## Dashboard de Food: grilla, tabla y tarjeta (F, campyprov)

- **Grilla con lugares** (`FoodResumen.tsx:39-46, 359-386`): tarjetas `ancha` (`md:col-span-2`), `angosta` y `alta`
  (`xl:row-span-2`). Cada una se cambia solo por otra del mismo tamaño; la ancha y la angosta de una fila pueden
  cambiar de lado. En celular, Atención va primero (`order-first xl:order-none`). Sin permiso de Inocuidad, Producción
  toma `xl:col-span-2`. El orden vive en `dashboard/logica.ts` y se guarda por usuario y sitio (estados.md › Arrastre).
- **`TarjetaPestana`** (`dashboard/piezas.tsx:100-156`): `aviso` (chip debajo del título, `mt-2`), `avisoEnTitulo`
  (el chip al lado del título, `gap-x-3.5`), `sub` (lugar para selectores), `estirar` (`flex min-h-[190px] flex-1
  flex-col`) y `pie`.
- **Tabla «Servicios de hoy»** (`FoodResumen.tsx:239-298`): `table-fixed` con `colgroup` en %, `min-w-[640px]`, filas
  `h-[68px]`; nombre `text-[15px] font-bold` + sub `text-[13px] text-slate-400`; para desplegar, `Plus` 14 que gira
  `rotate-45` con `aria-expanded`; filas desplegadas `bg-slate-50/50 text-[13.5px]` con un círculo `h-7 w-7 rounded-full
  border border-blue-100 bg-blue-50 text-action-blue` (`Utensils` 14/1.8); números centrados, el previsto en
  `text-[15px] font-bold text-action-blue`; `th` en `[&_th]:text-[12px] [&_th]:tracking-[0.06em]`.
- **Atención operativa** (`FoodResumen.tsx:196-209, 310-316`): el título de cada fila es la pestaña destino
  (`text-[15px] font-semibold`) y debajo el mensaje `text-[13.5px] font-medium opacity-85`; ícono `ShieldAlert` 18;
  «Ver todas» abre `components/ui/Modal.tsx`.
- **Paleta de dietas** `ESTILO_DIETA` (`TarjetasPestana.tsx:342-355`): un color y un fondo por familia, nunca rojo (el
  rojo queda para el riesgo).
- **Operators (campisoft):** su `FoodResumen.tsx` **no sigue este patrón** (sin `dashboard/`, `TarjetaPestana` ni
  arrastre; `KpiCard` viejo, chips -200, `GraficoDemanda` en verde y ámbar con `Legend`). No es referencia; si se
  alinea, se porta el de campyprov sin las acciones operativas.

## Shift: piezas propias (S, campisoft)

- **Filtros dentro de la tarjeta de la tabla:** fila `p-5 flex items-center gap-3 flex-wrap`
  (`ShiftAssignmentsPage.tsx:275`) o `p-4 border-b border-slate-100` (`ShiftSolicitudesPage.tsx:631`); la fila de `th`
  lleva `border-t border-slate-100`; `Combobox sinTexto` de ancho fijo (`w-44`/`w-48`); «Exportar» al final con `ml-auto`.
- **Encabezado de tabla de Shift:** `text-[11px] uppercase tracking-[0.06em] text-slate-400` (11, no 12: choque, ver
  tokens.md).
- **Lista + detalle:** `lg:grid-cols-[340px_1fr] gap-5` (Asignaciones), `xl:grid-cols-[360px_minmax(0,1fr)] gap-4`
  (Solicitudes), `xl:grid-cols-[340px_minmax(0,1fr)] gap-4` (DAE). Lista `h-[440px]` con buscador `h-10` dentro de
  `p-3 border-b`; panel de detalle `card p-5 space-y-4 sticky top-4` con «Editar» `h-8 px-3 rounded-[9px] text-[12.5px]`.
- **Calendario** (`CalendarioPage.tsx:285-512`): navegación `h-11 w-11 rounded-[10px] border` (con `aria-label`, que hoy
  falta) y «Hoy» `h-11 px-4 rounded-[10px]`; columna de hoy `bg-blue-600 rounded-t-[8px]` con «HOY» `text-[10px]
  tracking-[0.08em]` y línea `w-px bg-action-blue/50`; barras `h-8 rounded-[20px] text-[11.5px]` (en sitio azul,
  descanso `bg-slate-100 text-slate-400`); marcas S/B `h-6 w-6 rounded-full`, la bajada en rojo; vista mes `grid
  grid-cols-7 gap-1.5`, celda `rounded-[10px] border p-2 min-h-[88px]` con el color del código.
- **Pill con color configurado** (Colores): fondo con el hex elegido y texto de `textoSobre()` (blanco, o `#0f172a` si
  no contrasta) (`ShiftSolicitudesPage.tsx:129-141`).
- **Código de esquema:** una sola píldora pastel azul para todos los esquemas, `inline-flex items-center
  text-[12px] font-bold px-2.5 py-1 rounded-pill border border-action-blue bg-blue-50 text-blue-700` (Mateo, 26/10/2026,
  `ShiftAssignmentsPage.tsx`; reemplaza el color por esquema `ESQUEMA_COLORES` con radio 7).
- **Avatar de iniciales «cremita»:** `h-9 w-9 rounded-full text-[12px] font-bold` + `avatarColor(nombre)` de
  `@/lib/avatar` (fondo -100 y letra -700 de ocho tonos, fijo por persona); iniciales con `inicialesDe()`. En toda
  Planificación (Rosters, Turnos, DAE/DAP, Solicitudes, Calendario) desde el 26/10/2026.
- **Paginación de Shift:** sin selector de filas; «Mostrando…» a la izquierda y los botones a la derecha (26/10/2026).
- **Esquemas de roster:** sin la pastilla de versión «vN» (26/10/2026). Los esquemas de **horario** (Turnos) se
  editan en el lugar: no hay versión que mostrar.
- **Progreso del ciclo en una celda:** riel `h-[6px] rounded-full bg-slate-200` con relleno azul.
- **Barra fija de cambios en lote:** `sticky bottom-3 z-30 rounded-[14px] border border-slate-200 bg-white
  shadow-[0_8px_30px_-8px_rgba(15,30,60,0.25)] px-5 py-3` (`ShiftSolicitudesPage.tsx:694`).
- **Horarios:** vista previa de la rotación (`horarios/horarios-ui.tsx:58-86`).
- **Desvíos de Shift (no copiar):** chips con borde -200 y 11–11,5 px (`ShiftSolicitudesPage.tsx:144-148`,
  `horarios/horarios-lib.ts:144`), íconos en botones con texto, `#2563eb`/`#1d4fd8` sueltos, chevrons sin `aria-label`.

