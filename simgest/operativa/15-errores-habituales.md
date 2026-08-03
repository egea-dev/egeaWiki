---
title: "15. Errores habituales y cómo evitarlos"
description: "Manual operativo SIMGEST: 15. Errores habituales y cómo evitarlos"
published: true
tags: simgest, manual, operativa
editor: markdown
---

## 15. Errores habituales y actuación recomendada

> **Objetivo**
>
> Identificar fallos repetidos antes de que produzcan documentos, compras, recepciones o datos maestros incorrectos.

## Cómo utilizar esta entrada

Consulta primero el procedimiento específico. Esta tabla sirve como control rápido y no sustituye la revisión funcional.

## Ofertas y presupuestos

| Error | Señal de detección | Riesgo | Actuación |
|---|---|---|---|
| Crear líneas antes de completar la cabecera | Faltan cliente, proyecto, tarifa o forma de pago | Líneas asociadas a condiciones incorrectas | Completar y revisar la cabecera. |
| Seleccionar una forma de pago por defecto | No coincide con la condición comercial | Presupuesto incorrecto | Abrir el selector y confirmar el significado. |
| Revisar solo el total | No se comprueban artículos y cantidades | Error oculto en una línea | Revisar línea por línea. |
| Enviar un PDF sin compararlo | Oferta y PDF pueden diferir | Información incorrecta al cliente | Comparar cabecera, líneas y total. |
| Corregir el PDF fuera de SIMGEST | Dos versiones distintas | Pérdida de trazabilidad | Corregir la oferta y regenerar. |

## Artículos, variantes y tarifas

| Error | Señal de detección | Riesgo | Actuación |
|---|---|---|---|
| Editar un artículo parecido | Código distinto con descripción similar | Modificar otra referencia | Confirmar código antes de guardar. |
| Duplicar heredando proveedor o tarifa | El diálogo de duplicación se acepta sin revisar | Datos de compra incorrectos | Revisar la nueva ficha. |
| Copiar precio de otra columna | Acabado, ancho o unidad no coinciden | Coste incorrecto | Volver a la tarifa oficial. |
| Cambiar consumo o merma sin criterio | El escandallo se recalcula de forma inesperada | Necesidades erróneas | Pendiente de validación por Hacchi |

## Pedidos a proveedor

| Error | Señal de detección | Riesgo | Actuación |
|---|---|---|---|
| Filtrar por otro proyecto | Aparecen líneas ajenas | Compra para otro trabajo | Corregir filtros y repetir la búsqueda. |
| Utilizar Marcar todo sin revisar | Se seleccionan todas las líneas visibles | Pedido sobredimensionado | Seleccionar individualmente. |
| Generar sin validar tarifa | Precio no coincide con la fuente oficial | Coste incorrecto | Revisar proveedor, unidad y tarifa. |
| No abrir el pedido generado | No se comprueba el resultado | Error no detectado | Comparar pedido y selección. |

## Recepción

| Error | Señal de detección | Riesgo | Actuación |
|---|---|---|---|
| Registrar la cantidad pedida en lugar de la recibida | No se ha contado la mercancía | Stock y albarán incorrectos | Introducir solo la cantidad física. |
| Marcar una recepción parcial como servida | Quedan unidades pendientes | Cierre prematuro | Revisar estado y resto pendiente. |
| Introducir datos en otra línea | Artículo no coincide con el albarán | Recepción equivocada | Comparar código y descripción. |
| Confirmar sin revisar el albarán generado | Documento final no comprobado | Error persistente | Abrir y comparar el albarán. |

## Consultas y vistas

| Error | Señal de detección | Riesgo | Actuación |
|---|---|---|---|
| Pensar que falta un dato | La columna está oculta | Revisión incompleta | Abrir columnas visibles. |
| Guardar una vista sin conocer el alcance | Cambia la vista de otros usuarios | Interferencia operativa | Pendiente de validación por Hacchi |
| Revisar solo la cabecera de una carga | No se miran documentos ni líneas | Entrega incompleta | Revisar el detalle inferior. |

## Regla de detención

Detén el proceso cuando:

- el documento no pertenece al cliente o proyecto esperado;
- una cantidad no coincide con la mercancía o la fuente;
- un color o estado no tiene significado confirmado;
- no se conoce el efecto de una confirmación;
- existe una contradicción entre la captura, el vídeo y el documento;
- el procedimiento indica **Pendiente de validación por Hacchi**.

## Resultado esperado

Los errores se detectan antes de guardar o confirmar y se deriva a validación cualquier situación no documentada.

---

[← 14. Listas de comprobación](/simgest/operativa/14-checklists) · [Índice de operativa](/simgest/operativa) · [Manual SIMGEST →](/simgest)
