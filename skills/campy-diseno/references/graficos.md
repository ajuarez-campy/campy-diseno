# Gráficos

Origen: campyprov `apps/web/src/features/food/dashboard/piezas.tsx`, `dashboard/TarjetasPestana.tsx` y
`features/food/GraficoDemanda.tsx`. Antes de un gráfico nuevo, mirá si una pieza ya lo resuelve (`BarrasApiladas`,
`BarrasPorCategoria`, `AnillosCobertura`, `FilaBarra`, `Semicirculo`, `LeyendaChips`, `Total`, `SeparadorTotales`,
`PillHoy`, `ChipAlerta`, `CHIP_LEYENDA`, `FECHA_LARGA`). El `GraficoDemanda` de campisoft (Operators) es viejo (verde y
ámbar punteados, ejes de 10 px, `Legend` de Recharts): no es referencia.

## Color

- **Azules** para series: `#1d4ed8`, `#3b82f6`, `#60a5fa`, `#93c5fd`, `#bfdbfe`, `#1e3a8a`. Las barras
  intercalan solo dos, `AZULES_BARRAS = ['#1D4ED8', '#3B82F6']` (`piezas.tsx:19`); las líneas van en `#1E3A8A` y
  `#60A5FA`; los sectores usan 8 azules (`TarjetasPestana.tsx:215`) y «Sin sector» va en `#94A3B8`.
- **Hoy en el gráfico de demanda:** `PillHoy` (píldora `#2563eb` con el previsto) y la barra de hoy tramada (`pattern`
  de 7 px a 45°, línea blanca al 38 %; `GraficoDemanda.tsx:234-237, 267-270`). Con una fecha pasada, una línea `#cbd5e1`
  de 1,5 separa lo que pasó de lo que venía (`:272-274`).
- **Anillos:** 128×128 en `grid-cols-[repeat(auto-fit,minmax(144px,1fr))]`, rótulo 15 px semibold. Semicírculo de
  Producción de ancho 252 con el centro en `text-[36px]` (fuera de la escala: no copiar el tamaño).
- **Hoy:** `#2563eb` (`action-blue`); línea de referencia `strokeDasharray "4 4"`, `strokeOpacity .65`,
  ancho 2. Plan o días que vienen: `#bfdbfe`. Pasado sin dato: `#cbd5e1`.
- **Rojo** solo para lo que hay que resolver (faltante `#ef4444`). Verde/ámbar no se usan en series salvo
  que la serie misma sea un estado.
- Categorías con color propio del dominio (bolsas de residuos, dietas) usan ese color; si choca con el azul
  de Campy, se aclara (`#2563eb` → `#60a5fa`).

## Recharts

```tsx
<ResponsiveContainer width="100%" height="100%">           {/* el padre con alto fijo: h-[190px] */}
  <BarChart data={filas} margin={{ top: 8, right: 2, left: -18, bottom: 0 }} barCategoryGap="18%">
    <CartesianGrid vertical={false} stroke="#eef1f6" />
    <XAxis dataKey="fecha" tickLine={false} axisLine={{ stroke: '#e2e8f0' }} interval={0} height={32} />
    <YAxis tick={{ fontSize: 12, fill: '#64748b' }} tickLine={false} axisLine={false} allowDecimals={false} width={44} />
    <Tooltip content={<MiTooltip />} cursor={{ fill: '#f8fafc' }} />
    <Bar dataKey="x" fill="#1d4ed8" maxBarSize={22} radius={[3, 3, 0, 0]} isAnimationActive={false} />
  </BarChart>
</ResponsiveContainer>
```

- Sin animación (`isAnimationActive={false}`).
- Barras: radio solo arriba (`[3,3,0,0]` finas, `[5,5,0,0]` anchas hasta `maxBarSize 34`); en apiladas, solo
  la última serie lleva radio.
- Líneas: `type="monotone" strokeWidth={2.5} dot={{ r: 3.5, fill: '#fff', strokeWidth: 2.5 }}`.
- Eje Y con pasos «bonitos» (1 / 1.25 / 2 / 2.5 / 5 × 10ⁿ), 5 ticks.
- El alto del gráfico es **fijo** (`h-[190px]` tarjeta, `h-[210px]` gráfico principal): con solo un
  mínimo, Recharts mide 0.

## Tooltip

```tsx
<div className="rounded-card-sm border border-slate-200 bg-white px-3 py-2 text-[13px] shadow-card-hover">
  <p className="text-[13.5px] font-bold text-campy-ink">{fmtFecha(f, FECHA_LARGA)}</p>
  <p className="flex items-center gap-1.5 py-px text-slate-500 tabular">
    <span className="h-2 w-2 rounded-[3px]" style={{ background: color }} />
    <span className="flex-1">{nombre}</span>
    <b className="text-campy-ink">{fmtNum(v, 1)} kg</b>
  </p>
  {/* otro desglose */}
  <div className="mt-1.5 border-t border-slate-100 pt-1.5 text-[12px] text-slate-500">…</div>
</div>
```

## Leyenda en chips

`flex flex-wrap justify-center gap-2 mt-2.5`; cada chip
`inline-flex items-center gap-1.5 rounded-pill bg-slate-100 px-3.5 py-1.5 text-[13.5px] font-medium text-slate-600`
con punto `h-2.5 w-2.5 rounded-full`. Si el chip prende/apaga la serie: `<button aria-pressed>`.

## Días tocables

Tocar el número del eje o la columna elige el día: la cabecera de la tarjeta pasa al total de ese día
(rótulo «Total del día») y tocar otra vez vuelve al período. Píldora `#1e3a8a` (rx 8.5, 26×17), texto
blanco bold, columna `ReferenceArea fill="#dbeafe" fillOpacity={0.45}`. Área tocable transparente 28×22,
`role="button"`, Enter/Espacio. El clic no burbujea a la tarjeta (`stopPropagation`).

## Anillos y arcos (SVG)

- Perímetro 100: `r = 15.915`, `viewBox 0 0 42 42`, `-rotate-90`, aro de fondo `#f1f5f9` ancho 5.
- **Puntas redondeadas y separación:** `strokeLinecap="round"`, cada tramo se acorta `ancho + 0.6` y se
  corre `ancho/2 + 0.3`. Un tramo de 100 % va sin puntas; uno muy chico queda como punto.
- Centro: `text-[23px] font-bold tabular`; sin dato, aro gris y «—».
- Semicírculo: `pathLength 100`, `strokeWidth 11`, `round`, color `#1d4ed8` sobre `#bfdbfe`.

## Barras HTML (progreso por fila)

Riel `h-3.5 rounded-pill bg-slate-100`, relleno `bg-action-blue`; rótulo arriba
`text-[14px] font-semibold text-campy-ink truncate mb-1.5`, valor a la derecha
`text-[14px] font-semibold tabular min-w-12 text-right`. Sin dato: riel vacío y «—».
