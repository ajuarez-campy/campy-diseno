# Checklist de revisión de UI

Recorrer sobre el diff (`git diff main...HEAD -- apps/web`). Reportar cada desvío como:
`archivo:línea — regla — qué hay → qué va`. Ordenar: primero lo que rompe reglas del proyecto, después lo
visual. Si algo no está cubierto por la guía, marcarlo como pregunta, no como error.
Si el diff toca `worker-app/`, recorré además el checklist de [mobile.md](mobile.md).

## Reglas del proyecto (bloquean)

- [ ] Ningún texto visible fijo: todo con `t()` en los 4 idiomas (incluye `title`, `aria-label`, placeholder, vacíos, toasts).
- [ ] Placeholder de buscador sin «…» ni «...» al final, en los 4 idiomas («Buscar servicio»).
- [ ] Placeholder de buscador sin «…» ni «...» al final, en los 4 idiomas («Buscar servicio»).
- [ ] Placeholder de buscador sin «…» ni «...» al final, en los 4 idiomas («Buscar servicio»).
- [ ] Ningún placeholder (buscador o campo) termina en «…» ni «...», en los 4 idiomas («Buscar servicio»).
- [ ] Textos con mayúscula inicial (también después de « · » y el mes de una fecha); códigos cortos enteros en mayúscula («ES»); continuaciones de una misma frase en minúscula.
- [ ] Botones solo con texto (sin flecha ni ícono al lado) y chips de estado sin punto al inicio.
- [ ] Animaciones con «reducir movimiento» y sin trabar la navegación.
- [ ] Buscador como el de Shift: `h-11 rounded-input` (no píldora), lupa 15 en `left-3.5`, `pl-9`, 14 px, borde azul al foco sin halo.
- [ ] Nada inventado: sin dato → «Sin datos» / «—»; en gráficos `null`, no `0`.
- [ ] Sin aclaraciones entre paréntesis en textos de UI.
- [ ] Descripciones en una sola oración simple, sin incisos entre comas.
- [ ] Descripciones en una sola oración simple, sin incisos entre comas.
- [ ] Descripciones en una sola oración simple, sin incisos entre comas.
- [ ] Descripciones en una sola oración simple, sin incisos entre comas.
- [ ] No se muestra (ni se deshabilita) lo que la API rechaza por permiso.
- [ ] Fechas y números con `fmtNum`, `fmtFecha`, `localeUi()`; «hoy» con `hoyLocalISO()`.
- [ ] Sin `dangerouslySetInnerHTML`.

## Tipografía

- [ ] Títulos: pantalla 30/24px, pestaña 27px, tarjeta 16px bold `text-campy-ink`.
- [ ] Rótulos en mayúscula: `12px bold uppercase tracking-[0.1em] text-slate-500`.
- [ ] `th`: `12px bold uppercase tracking-[0.06em] text-slate-400`.
- [ ] Números: `tabular` y `leading-none`; KPI 30px bold.
- [ ] Solo pesos 400/500/600/700; sin tamaños nuevos si uno de la escala sirve.

## Color

- [ ] Tokens donde existan: `text-campy-ink`, `bg-action-blue`, `rounded-card`, `rounded-input`, `rounded-pill`, `shadow-card-hover`.
- [ ] Nada de `campy-blue` (no existe en campisoft) ni `bg-gradient-cta` / `shadow-premium-*`.
- [ ] Estados con los cinco tonos (emerald, amber, red, blue, slate); violeta para IA, `INFO_REQUERIDA` y Bienestar (ya no es exclusivo de IA [D, 17/10/2026]).
- [ ] Rojo solo para crítico/riesgo/faltante. Gráficos en azules.
- [ ] Grises por rol (ink / slate-600 / 500 / 400 / 300).

## Piezas

- [ ] Tarjeta: `rounded-card border-slate-200/80` + sombra de tarjeta, `p-4 sm:p-5`.
- [ ] Chip: `rounded-pill border px-2.5 py-1 text-[12px] font-semibold` + tono, con el borde del mismo color que el texto.
- [ ] Botón: `h-11 rounded-[20px]`, primario azul, secundario con borde, un solo primario por vista.
- [ ] Input: `h-11 rounded-input text-[15px]` con borde y halo azul al foco.
- [ ] Pestañas: píldora azul rellena; sub-pestañas `bg-blue-50`.
- [ ] Modal: portal, `bg-slate-900/40`, `DrawerHeader` navy, pie Cancelar + primario a la derecha.
- [ ] Se reusa un componente existente en vez de copiar sus clases (TarjetaPestana, KpiCard, Combobox, DateField, LeyendaChips…).

## Estados

- [ ] Hover en todo lo clickeable; tarjeta clickeable con `role="button"`, `tabIndex`, Enter/Espacio.
- [ ] Foco visible (no `outline-none` sin `focus-visible:ring`).
- [ ] Disabled: `opacity-50 cursor-not-allowed`; input `bg-slate-50 text-slate-500`.
- [ ] Vacío: ícono 32 slate-300 + título + explicación + acción (si hay permiso); en tarjeta chica, ícono + línea con el mismo alto del visual.
- [ ] Cargando: esqueleto en tarjeta/gráfico, spinner en tabla, gerundio en botón. Nunca «vacío» mientras carga.
- [ ] Error: reintentar en tarjeta; 403 sin reintentar; toast al guardar.
- [ ] Sin `hover:bg-*` en filas de tabla (lo pisa el CSS global).

## Gráficos

- [ ] Alto fijo del contenedor; `isAnimationActive={false}`.
- [ ] Grilla `#eef1f6` sin verticales, ejes 12px `#64748b`.
- [ ] Tooltip con la pieza estándar (`rounded-card-sm`, `shadow-card-hover`, 13px).
- [ ] Hoy en `action-blue`; día elegido con píldora `#1e3a8a`.
- [ ] Anillos y arcos con puntas redondeadas y separación.

## Responsive y accesibilidad

- [ ] Funciona en celular (grillas que bajan a 1–2 columnas, tablas con `overflow-x-auto` y `min-w`).
- [ ] Íconos decorativos `aria-hidden`; informativos con `role="img"` + `aria-label`.
- [ ] Contraste: texto blanco sobre color solo si llega a 3:1 (si no, `#0f172a`).
