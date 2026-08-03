---
title: "2. Cartera (recibos)"
description: "Manual de tesorería y contabilidad SIMGEST: 2. Cartera (recibos)"
published: true
tags: simgest, operativa, tesoreria, contabilidad
editor: markdown
---

## 2. Cartera (recibos)

La cartera agrupa los **recibos derivados de facturas** y sirve como punto de control para vencimientos, pagos y cobros.

## Objetivo

Entender cómo se generan y cómo deben gestionarse los recibos antes de incorporarlos a remesas o marcarlos como pagados/cobrados.

## Cuándo utilizar este procedimiento

Utilice esta página cuando necesite revisar vencimientos, dividir pagos, controlar el estado de un recibo o comprobar si un recibo puede modificarse.

## Ruta confirmada

`Tesorería > Cartera > Pagos` o `Tesorería > Cartera > Cobros`

## Requisitos previos

- Debe existir una factura previa.
- El recibo debe haberse generado en cartera.

## Vista general del proceso

Factura emitida o recibida → recibo automático en cartera → revisión del vencimiento → posible división del pago → incorporación a remesa → cambio de estado hasta pago o cobro.

## Funcionamiento confirmado

### Cada factura genera un recibo automático

La cartera no se alimenta manualmente desde cero en el flujo descrito. La documentación indica que **cada factura genera automáticamente un recibo**, que después puede ser revisado y gestionado.

### Los vencimientos se modifican en cartera

La formación insiste en un criterio importante:

- Los **vencimientos se modifican solo en cartera**.
- **No deben modificarse en la remesa**.

Esto significa que la remesa debe construirse a partir de recibos ya revisados. Si el vencimiento es incorrecto, el ajuste debe hacerse antes, en la cartera.

### Se pueden dividir recibos en varios pagos

Cuando un mismo importe deba gestionarse en más de un pago, la cartera permite dividirlo. El efecto práctico es que un único recibo puede transformarse en varios movimientos controlados por separado.

### Los recibos en remesas cerradas no son modificables

Una vez que el recibo forma parte de una remesa **cerrada**, deja de ser editable. Por tanto, conviene revisar bien los importes y vencimientos antes de cerrar la remesa.

## Estados confirmados

La formación resume el ciclo del recibo así:

**Pendiente → En remesa (Nº remesa) → Pagado (fecha)**

### Qué debe comprobar

- Que el recibo corresponda a la factura correcta.
- Que el vencimiento sea el deseado antes de crear o cerrar la remesa.
- Que el recibo no esté ya vinculado a una remesa cerrada si se pretende modificar.

## Resultado esperado

La cartera refleja recibos correctos, con el vencimiento revisado y en el estado que corresponda según el punto del proceso.

## Errores habituales

### Intentar modificar un recibo dentro de una remesa cerrada

**Qué ocurre:** el sistema no lo permite.

**Qué hacer:** revisar si es necesario reabrir o rehacer el proceso. **Pendiente de validación por Hacchi** el criterio exacto de actuación cuando la remesa ya está cerrada y el cambio es imprescindible.

[← Anterior](/simgest/operativa/tesoreria-contabilidad/01-configuracion-bancos) | [Índice](/simgest/operativa/tesoreria-contabilidad) | [Siguiente →](/simgest/operativa/tesoreria-contabilidad/03-remesas-pago-confirming)
