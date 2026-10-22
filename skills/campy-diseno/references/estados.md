# Estados

## Interacción

| Estado | Regla |
|---|---|
| **Hover de tarjeta clickeable** | `cursor-pointer transition-all hover:border-slate-300 hover:shadow-[0_1px_2px_rgba(15,30,60,0.06),0_14px_32px_-16px_rgba(15,30,60,0.22)]`. La tarjeta entera es `role="button" tabIndex={0}` con Enter/Espacio. |
| Hover de botón primario | `hover:bg-blue-700` + `hover:shadow-[0_8px_20px_rgba(37,99,235,0.35)]` |
| Hover de secundario / ícono | `hover:bg-slate-50`; botón de ícono `hover:bg-slate-100 hover:text-slate-600`; borrar `hover:bg-red-50 hover:text-red-600` |
| Hover de borde (inputs, opciones) | `hover:border-slate-300` |
| Hover de fila de tabla | lo pone el CSS global (slate-100): no agregar `hover:bg-*` a filas |
| Hover de ítem de alerta | `hover:bg-red-50` y chevron `group-hover:translate-x-0.5` |
| Hover de chip de leyenda (si filtra) | `hover:bg-slate-200/70`; serie apagada `opacity-40` + `aria-pressed` |
| **Foco** | Global (outline azul). Si se usa `outline-none`: `focus-visible:ring-2 focus-visible:ring-action-blue/40`. Inputs: `focus:border-action-blue focus:shadow-[0_0_0_3px_rgba(37,99,235,0.12)] focus:outline-none` [D] |
| **Active** | `active:scale-[0.98]` en botones; `active:cursor-grabbing` en arrastrables |
| **Deshabilitado** [D] | Botón: `disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:shadow-none`. Input: `disabled:bg-slate-50 disabled:text-slate-500 disabled:cursor-not-allowed`. **Sin permiso no se deshabilita: no se muestra.** La planificación [P] deshabilita con el motivo en `title` (`bloqueo`, `food-lib.tsx:35`; `FoodPlanificacion.tsx:222, 476`): eso choca con la regla 6 de CLAUDE.md y **no se copia**. |
| **Seleccionado** | Fila o ítem de lista: `bg-blue-50/70`. Tarjeta de opción y **celda de día** [P]: `border-2 border-action-blue bg-blue-50/50` (no elegida `border-2 border-slate-200 hover:border-slate-300`), `border-2` también en la no elegida para que nada se corra y **sin `ring`** (`FoodPlanificacion.tsx:276-285`). Sin selección explícita queda elegido el primer día con datos (`:128`); al cambiar de semana se borra la selección (`:202`). Día elegido de un gráfico: píldora `#1e3a8a` con texto blanco + columna `#dbeafe` al 45 %. Tocar otra vez deselecciona. |
| **Arrastre** | Elementos `cursor-grab active:cursor-grabbing`; origen `opacity-40`; destino `rounded-[16px] ring-2 ring-action-blue/40` (siempre 16, también sobre las tarjetitas de 12; `dashboard/arrastre.ts:79-81`). Orden guardado en `localStorage` por usuario **y** por sitio (`campy-food-orden:<lista>:<userId>:<campId>`, `arrastre.ts:12`). |
| Riesgo operativo (no crítico) [P] | Ámbar: celda `border-amber-200 bg-amber-50/50`, píldora `bg-amber-100 text-amber-700`, aviso `text-[11.5px] font-semibold text-amber-600` («supera la capacidad del comedor», `FoodPlanificacion.tsx:327-331, 363`). Rojo solo si es crítico. |
| Hoy | Azul `action-blue` y bold (tick del eje, día del calendario, línea de referencia punteada `4 4`). |

## Datos

### Vacío [D]

Base: **ícono gris + título + explicación + acción** (si el usuario puede crear algo).

```
ícono lucide 32 · strokeWidth 1.5 · text-slate-300
título      text-[14.5px] font-semibold text-slate-500
explicación text-[13px] text-slate-400
acción      botón secundario (solo si tiene permiso)
contenedor  flex flex-col items-center justify-center text-center py-12
```

Dentro de una tarjeta chica del dashboard o de un gráfico alcanza con ícono + una línea: `BarChart3` 26/1.5
`text-slate-300` + `mt-2 text-[12.5px] text-slate-400`, ocupando el mismo alto que el visual (`h-[226px]`,
`dashboard/piezas.tsx:145-148`), para que la tarjeta no salte de tamaño. En Shift: ícono de 28–36 + una línea;
Horarios y Calendario, solo la línea.
En [P] las listas y la tira de días muestran solo esa línea, sin ícono (`FoodPlanificacion.tsx:295, 367, 457, 498`):
vale para una fila o tira dentro de una tarjeta que ya tiene título; una pantalla o tarjeta vacía entera sigue
llevando ícono + título + explicación.
Un dato que **no llegó** se marca con píldora de **borde punteado** gris (`border-dashed border-slate-300 bg-white
text-slate-500`, «Sin demanda», `FoodPlanificacion.tsx:50`), distinta del dato presente.
Cada vacío dice **qué** falta («Sin pesajes en los últimos 14 días»), no un «Sin datos» genérico, salvo
que no haya nada más que decir.

«—» para un valor puntual sin dato (`fmtNum(null)`, celda vacía, centro de anillo sin dato).

### Cargando [D: depende del lugar]

| Lugar | Qué |
|---|---|
| Tarjeta, gráfico, KPI | Esqueleto `animate-pulse` con la forma de lo que viene: `h-6 w-24 rounded-md bg-slate-100` + bloque `rounded-input bg-slate-100/80` del alto del visual |
| Tabla | Spinner centrado en una fila `py-14`: `h-8 w-8 animate-spin rounded-full border-4 border-slate-200 border-t-action-blue` |
| Botón que guarda | Texto en gerundio (`t('…guardando')` → «Guardando…») y `disabled` mientras dura |
| Página entera | Esqueleto del layout (lo pone `AppLayout`) |

**Nunca** mostrar el estado vacío mientras carga.

### Error

- En tarjeta: mensaje `text-[13px] font-semibold text-campy-ink` (`dashboard/piezas.tsx:133`) + botón «Reintentar»
  `rounded-input border border-slate-200 px-3 py-1.5 text-[12px] font-semibold text-action-blue
  hover:border-slate-300` (con `stopPropagation` si la tarjeta es clickeable).
- 403: mensaje de permiso, **sin** «Reintentar».
- Al guardar: toast `variant: 'error'` con el mensaje del servidor (ya traducido por el filtro global).

### Gráficos sin registro

Un día sin registro es `null` (no se dibuja, `connectNulls={false}`), no `0`. Tooltip: «fecha · sin
registro». Si son varios días seguidos, banda `#f1f5f9` al 55 % con el texto «SIN REGISTRO»
(10.5px, 600, tracking 1.5, `#94a3b8`) solo si entra.

## Avisos y alertas

| Tipo | Clases |
|---|---|
| Aviso informativo en línea | `rounded-card-sm bg-blue-50/70 border border-blue-100 px-4 py-2.5 text-[13px] text-slate-600` + ícono `Info` 15. En [P] (`Aviso`, `food-lib.tsx:433-441`) va `rounded-[10px] px-3.5 py-2.5 text-[12.5px] font-medium` con ícono 14 y tonos ok/alerta/rojo/ia (`bg-*-50/70 border-*-100 text-*-700`): choque de medidas, ver tokens.md |
| Aviso de IA [P] | `rounded-input border border-violet-100 bg-violet-50/60` con texto `text-violet-700` (franja de recomendación, `FoodPlanificacion.tsx:387`); solo para lo que propone Campy AI |
| Advertencia en línea | `rounded-card-sm bg-amber-50 border border-amber-200 p-4` |
| Ítem que requiere atención | `group w-full flex items-center gap-3 rounded-card-sm border border-red-200 bg-red-50/60 hover:bg-red-50 px-3 py-2.5 text-left transition-colors`; ícono en `h-9 w-9 rounded-lg bg-red-100 text-red-700` |
| Sin alertas | círculo `h-10 w-10 rounded-full bg-emerald-50` con `ShieldCheck` 20 `text-emerald-600` |
| Toast | `useToast()` compartido: success / error / warning / info. Éxito **solo** cuando el servidor confirmó, con el antes → después si hubo cambio (`FoodPlanificacion.tsx:171-184`); error con el mensaje del servidor |
| Confirmación | modal propio con paso «¿Confirmar…?»; `confirm()` nativo solo si no hay otra |
