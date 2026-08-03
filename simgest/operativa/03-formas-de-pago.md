---
title: "3. Seleccionar condiciones y forma de pago"
description: "Manual operativo SIMGEST: 3. Seleccionar condiciones y forma de pago"
published: true
tags: simgest, manual, operativa
editor: markdown
---

## 3. Seleccionar la forma de pago

La forma de pago forma parte de las condiciones comerciales de la oferta. Debe corresponder a la condición pactada con el cliente y quedar guardada antes de generar el presupuesto en PDF o confirmar la oferta.

> **Objetivo**
>
> Seleccionar y comprobar la forma de pago correcta dentro de la oferta, evitando que el documento se emita con una condición diferente a la acordada.

## Cuándo utilizar este procedimiento

Utilícelo al crear una oferta, al revisar una oferta existente y siempre que el cliente haya solicitado un cambio de condición antes de la emisión.

No debe modificarse una forma de pago en un documento sin comprobar si el cambio afecta a documentos ya generados. El alcance de la actualización sobre pedidos o documentos posteriores es **Pendiente de validación por Hacchi**.

## Requisitos previos

- oferta correcta abierta;
- cliente y referencia confirmados;
- condición pactada conocida;
- listado de formas de pago disponible en SIMGEST;
- autorización para modificar la oferta cuando corresponda.

## Por qué debe revisarse

Una oferta puede contener precios y cantidades correctos y, aun así, ser comercialmente incorrecta si muestra otra condición de pago. El usuario no debe seleccionar la primera opción del desplegable ni interpretar el código sin leer su descripción.

## Vista general

Abrir la oferta
→ localizar condiciones
→ desplegar opciones
→ comparar con lo pactado
→ seleccionar
→ aceptar
→ guardar
→ volver a comprobar

## Procedimiento

### Paso 1. Abrir la oferta correcta

Localice la oferta por cliente, proyecto, referencia o número. Antes de modificarla, compruebe:

- cliente;
- referencia;
- estado;
- proyecto;
- fecha.

Este control evita cambiar la condición de otro documento similar.

### Paso 2. Localizar el bloque de condiciones

El material visual muestra el bloque **Condiciones y Forma de Pago** en la zona central de la oferta.

[![Oferta con el bloque Condiciones y Forma de Pago señalado](/assets/simgest/operativa/cap_02_forma_pago.png =70%x)](/assets/simgest/operativa/cap_02_forma_pago.png)

*La captura muestra la zona desde la que se selecciona la condición aplicable a la oferta.*

**Qué debe comprobar**

- valor actualmente seleccionado;
- código y descripción visibles;
- existencia de una condición previa del cliente;
- coherencia con la documentación comercial disponible.

### Paso 3. Abrir el selector

Abra el desplegable o selector asociado al campo.

**Qué debe hacer**

Revise las opciones por descripción completa. Cuando existan códigos, utilícelos como identificadores, pero no deduzca su significado sin leer el texto asociado.

**Qué no debe hacer**

- seleccionar por posición en la lista;
- elegir una opción de nombre parecido sin comprobarla;
- crear una nueva forma de pago desde esta pantalla si el procedimiento no está validado;
- sustituir una condición dudosa por **Contado** sin registrar la incidencia.

### Paso 4. Comparar con la condición pactada

La selección debe basarse en la condición confirmada con el cliente o en el dato maestro validado.

**Qué debe comprobar**

- descripción completa;
- posibles plazos;
- modalidad de cobro;
- ausencia de una condición provisional;
- coherencia con las notas o acuerdos registrados.

Cuando el material no permita determinar la opción correcta, escriba **Pendiente de validación por Hacchi** y no emita el documento.

### Paso 5. Seleccionar y aceptar

Seleccione la opción correcta y utilice la acción de aceptación visible en el selector.

**Resultado inmediato esperado**

El bloque de condiciones muestra la opción elegida y el selector queda cerrado.

### Paso 6. Guardar y volver a comprobar

Guarde la oferta. Después:

1. vuelva a revisar el campo;
2. confirme que el valor se mantiene;
3. compare con la condición pactada;
4. compruebe que no se ha modificado otra parte de la cabecera;
5. continúe con la revisión completa de la oferta.

## Resultado esperado

La oferta conserva la forma de pago correcta y puede pasar a la revisión previa a emisión. La selección es visible, comprensible y coherente con la condición comercial confirmada.

## Comprobación final

- [ ] La oferta correcta está abierta.
- [ ] Cliente, referencia y proyecto están confirmados.
- [ ] Se ha leído la descripción completa de la forma de pago.
- [ ] La opción coincide con lo pactado.
- [ ] La selección se ha aceptado.
- [ ] La oferta se ha guardado.
- [ ] El valor se mantiene después de guardar.
- [ ] No existen dudas pendientes antes de emitir.

## Errores habituales

| Error | Riesgo | Actuación |
|---|---|---|
| Seleccionar por código sin leer la descripción | Condición incorrecta | Abrir el selector y comparar. |
| Modificar la oferta equivocada | Se altera otro presupuesto | Confirmar cliente y referencia. |
| No guardar | El PDF puede mantener el valor anterior | Guardar y volver a comprobar. |
| Elegir Contado como solución automática | Se oculta una falta de equivalencia | Pendiente de validación por Hacchi. |
| Emitir con una duda abierta | Se envía una condición no confirmada | Detener la emisión. |

---

[← 2. Crear una oferta](/simgest/operativa/02-presupuestos) · [Índice de operativa](/simgest/operativa) · [4. Revisar la oferta →](/simgest/operativa/04-revision-presupuesto)
