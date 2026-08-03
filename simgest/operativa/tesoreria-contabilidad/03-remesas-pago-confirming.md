---
title: "3. Remesas de pago — confirming y transferencias"
description: "Manual de tesorería y contabilidad SIMGEST: 3. Remesas de pago — confirming y transferencias"
published: true
tags: simgest, operativa, tesoreria, contabilidad
editor: markdown
---

## 3. Remesas de pago — confirming y transferencias

Esta página desarrolla la creación de remesas de pago, con especial atención al **confirming estándar**, que según la formación es el tipo utilizado en la mayoría de los casos.

## Objetivo

Crear correctamente una remesa de pago, revisar sus recibos, cerrarla cuando corresponda, generar el fichero bancario y completar el pago sin duplicar envíos ni provocar errores contables.

## Cuándo utilizar este procedimiento

Use este procedimiento cuando deba agrupar recibos de pago para remitirlos al banco mediante confirming o transferencia.

## Ruta confirmada

`Tesorería > Remesas de pago > Añadir`

## Requisitos previos

- Los recibos deben existir previamente en cartera.
- El banco debe estar configurado correctamente.
- Si se va a trabajar con confirming, debe estar revisada la **cuenta de confirming** del banco.

## Vista general del proceso

Añadir remesa → completar cabecera → revisar detalle → cerrar remesa → generar fichero → pagar la remesa.

## 3.1 Tipos de remesa confirmados

### Confirming estándar

Es el tipo **usado en torno al 95 %** según el documento base. El flujo descrito es:

**Recibos → asiento 400/410 → 401 → fichero → pago 572**

### Confirming pronto pago

Incluye **control de riesgo** y requiere contrato bancario. La documentación lo menciona, pero no desarrolla su configuración completa.

### Transferencias

Se utilizan para **pago directo**, sin cuenta intermedia de confirming.

## 3.2 Crear una remesa de confirming estándar

### Paso 1. Completar la cabecera

En la cabecera deben revisarse, al menos, estos elementos confirmados en la formación:

- **Título** (opcional).
- **Fecha de orden de pago**.
- **Banco** (con posibilidad de búsqueda mediante **F3**).
- **Cuaderno**.

La formación distingue:

- **Cuaderno 34** para recibos.
- **Cuaderno 68** para pagarés.

### Qué debe comprobar en la cabecera

- Que el banco sea el correcto.
- Que la fecha de orden de pago corresponda al momento real de emisión.
- Que el cuaderno seleccionado sea coherente con el tipo de documento.

### Resultado esperado de la cabecera

La remesa queda creada con una cabecera válida para empezar a incorporar o revisar recibos.

<a href="/assets/simgest/operativa/tesoreria-contabilidad/03_remesa_confirming_cabecera.png"><img src="/assets/simgest/operativa/tesoreria-contabilidad/03_remesa_confirming_cabecera.png" alt="Ventana de remesa con la cabecera, la zona de opciones y el área de filtros señalizadas." style="width: 70%; height: auto;" /></a>
### Paso 2. Revisar el detalle de la remesa

En el detalle se muestran los recibos incorporados o disponibles según el criterio de selección. La formación confirma que los recibos pueden filtrarse por:

- **vencimiento**;
- **razón social**;
- **importe**;
- **cuenta**.

También se indica que la **reorganización de columnas no afecta al fichero**, por lo que sirve para ordenar visualmente la consulta sin modificar el resultado bancario.

El contador de la ventana muestra el **importe total** de la remesa, un dato importante para verificar que la selección coincide con lo esperado antes de cerrar.

### Qué debe comprobar en el detalle

- Que los recibos incluidos son realmente los que se deben pagar.
- Que el importe total coincide con la previsión.
- Que los filtros no están dejando fuera registros necesarios.

### Resultado esperado del detalle

La remesa queda revisada y lista para su cierre.

<a href="/assets/simgest/operativa/tesoreria-contabilidad/04_remesa_confirming_detalle_y_filtros.png"><img src="/assets/simgest/operativa/tesoreria-contabilidad/04_remesa_confirming_detalle_y_filtros.png" alt="Ventana de remesa con la zona de filtros, el listado de recibos y el total de la parte inferior señalizados." style="width: 70%; height: auto;" /></a>
### Paso 3. Cerrar la remesa

El cierre tiene varias consecuencias importantes:

- **bloquea la remesa**;
- genera un **asiento automático**;
- cancela 400/410 y lleva el saldo a **401**;
- valida la **cuenta de confirming**.

Por eso no debe cerrarse una remesa que todavía requiera cambios en la selección o en los importes.

### Error crítico asociado

Si la cuenta de confirming no es correcta, este suele ser el momento en el que el sistema lo detecta.

### Paso 4. Generar el fichero

Una vez cerrada la remesa, se genera el fichero bancario.

La formación confirma:

- **Confirming** → cuaderno **CSB FINIM estándar**.
- **Transferencias** → **34SEPA TXT** o **XML**.
- El fichero se guarda como **.soc (TXT)**.

### Advertencia importante

El vídeo y el documento mencionan un **chivato parpadeante** que indica que el fichero **ya ha sido generado**. Si ese aviso aparece, no debe enviarse una segunda vez por rutina, porque puede provocar duplicidades en el envío bancario.

### Qué debe comprobar al generar el fichero

- Que el fichero se haya generado una sola vez.
- Que no exista duda sobre un envío anterior antes de volver a generarlo.

### Resultado esperado del fichero

La remesa queda con su fichero generado y lista para la fase de pago.

<a href="/assets/simgest/operativa/tesoreria-contabilidad/05_remesa_fichero_generado.png"><img src="/assets/simgest/operativa/tesoreria-contabilidad/05_remesa_fichero_generado.png" alt="Remesa con el aviso de fichero generado, la zona de tipo de remesa y la parte de control del registro señalizadas." style="width: 70%; height: auto;" /></a>
### Paso 5. Pagar la remesa

La formación indica el uso de:

**“Pagar toda la remesa” → “Cargo en un solo apunte” → Sí**

El efecto esperado es:

- quitar **401**;
- registrar **cargo individual por proveedor**;
- registrar **abono en 572**.

## 3.3 Transferencias: diferencias confirmadas

En las remesas por transferencia se han señalado estas diferencias:

- **No hay paso de cierre** (el botón aparece deshabilitado).
- Al **generar el fichero**, el sistema realiza el cierre automáticamente.
- La remesa se **puede reabrir** (candado abierto).
- El pago se realiza **directamente contra acreedor**.

## Comprobación final

- Banco correcto.
- Fecha de orden de pago revisada.
- Cuaderno correcto.
- Recibos y total validados.
- Remesa cerrada cuando corresponda.
- Fichero generado una única vez.
- Pago ejecutado con el criterio adecuado.

## Errores habituales

### Generar el fichero más de una vez

**Riesgo:** duplicar el envío al banco.

**Qué hacer:** comprobar si el chivato indica que el fichero ya se generó y revisar el estado antes de repetir la acción.

### Cerrar una remesa con recibos sin revisar

**Riesgo:** dejar bloqueada una selección incorrecta.

**Qué hacer:** revisar detalle, filtros e importe total antes del cierre.

[← Anterior](/simgest/operativa/tesoreria-contabilidad/02-cartera-recibos) | [Índice](/simgest/operativa/tesoreria-contabilidad) | [Siguiente →](/simgest/operativa/tesoreria-contabilidad/04-remesas-cobro)
