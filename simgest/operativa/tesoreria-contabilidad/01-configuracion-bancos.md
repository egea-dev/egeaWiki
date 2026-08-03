---
title: "1. Configuración de bancos"
description: "Manual de tesorería y contabilidad SIMGEST: 1. Configuración de bancos"
published: true
tags: simgest, operativa, tesoreria, contabilidad
editor: markdown
---

## 1. Configuración de bancos

Esta entrada reúne las instrucciones confirmadas para **dar de alta un banco** y **revisar su configuración principal** en el área de Tesorería.

## Objetivo

Crear o revisar una ficha bancaria de manera que el banco quede operativo para remesas, cobros, pagos y generación de ficheros.

## Cuándo utilizar este procedimiento

Utiliza esta página cuando necesites:

- dar de alta un banco nuevo;
- revisar una ficha bancaria ya creada;
- preparar el banco para remesas de pago o cobro;
- comprobar campos que pueden provocar errores en la generación de confirming o ficheros SEPA.

## Requisitos previos

- El tercero asociado al banco debe existir previamente.
- Deben estar disponibles los datos de cuenta y las cuentas contables necesarias.
- Si el banco se utilizará en SEPA, debe conocerse el **BIC/SWIFT**.

## Vista general del proceso

Acceder a Tesorería > Bancos → crear o abrir el banco → completar datos básicos → revisar campos críticos → guardar y validar la ficha.

## 1.1 Dar de alta un banco

**Ruta confirmada:** `Tesorería > Bancos`

### Paso 1. Acceder a la pantalla de bancos

Abra la opción **Tesorería > Bancos** para trabajar sobre el registro bancario. Esta pantalla es el punto de partida tanto para crear un banco nuevo como para revisar uno ya existente.

### Paso 2. Completar la ficha principal

En el alta inicial, la formación indica como obligatorios los siguientes elementos:

- **Tercero**.
- **Código IVA**.
- **Datos de cuenta**.
- **Cuentas contables**.

El objetivo de este paso es dejar la ficha vinculada a un tercero real y con la estructura contable mínima para que los procesos posteriores no fallen.

### Qué debe comprobar

- Que el tercero seleccionado sea el correcto.
- Que la cuenta bancaria corresponda realmente al banco que se está dando de alta.
- Que existan las cuentas contables necesarias para la operativa prevista.

### Resultado esperado del alta

La ficha del banco queda creada y vinculada a un tercero previamente dado de alta.

<a href="/assets/simgest/operativa/tesoreria-contabilidad/01_bancos_vinculacion_y_campos_basicos.png"><img src="/assets/simgest/operativa/tesoreria-contabilidad/01_bancos_vinculacion_y_campos_basicos.png" alt="Pantalla de bancos con la ficha principal, la ventana de remesa y la zona de detalle señalizadas." style="width: 70%; height: auto;" /></a>
## 1.2 Configuración del banco

**Ruta confirmada:** `Tesorería > Bancos > [Seleccionar banco] > Editar`

### Pestaña Básicos

En esta pestaña se revisan varias opciones que condicionan el comportamiento del banco en remesas y pagos.

#### Opciones confirmadas

- **Activa** → **Obligatorio**.
- **Banco por defecto para remesas**.
- **Abono**.
- **Por vencimiento** → varios cargos según fecha.
- **Por efecto** → varios cargos por efecto individual.
- **Sin marcar** → único cargo global (**recomendado** en la documentación base).

### Advertencia

La formación indica expresamente que **marcar demasiadas opciones puede causar errores**. Por tanto, no conviene activar campos adicionales por intuición. Si existe duda sobre una marca concreta, debe revisarse antes de cerrar la configuración.

### Pestaña Bloqueo por periodos

Esta pestaña permite **bloquear la cuenta corriente por meses cerrados**. Su finalidad es evitar movimientos manuales no autorizados sobre periodos que ya no deberían modificarse.

### Campos obligatorios críticos

#### Cuenta de confirming

Debe contener **la misma cuenta contable que la cuenta corriente**. Si este campo no está correctamente informado, el sistema puede mostrar el error:

> cuenta bancaria para confirming no es correcta

#### BIC/SWIFT

Es **obligatorio para ficheros SEPA**. Si falta, la generación del fichero puede fallar.

#### Código CSV

La documentación indica que debe ser un código identificador de **3 dígitos**. En la formación se comenta que **“000” suele funcionar**.

### Qué debe comprobar al finalizar

- Que la ficha esté activa.
- Que la cuenta de confirming esté informada correctamente.
- Que el BIC/SWIFT exista cuando el banco vaya a utilizarse para SEPA.
- Que no se hayan activado opciones innecesarias.

### Resultado esperado de la configuración

El banco queda preparado para su uso en remesas, cobros, pagos y generación de ficheros.

<a href="/assets/simgest/operativa/tesoreria-contabilidad/02_bancos_campos_criticos.png"><img src="/assets/simgest/operativa/tesoreria-contabilidad/02_bancos_campos_criticos.png" alt="Ficha de banco con la zona general, los campos contables y la parte inferior de la ficha señalizadas." style="width: 70%; height: auto;" /></a>
## Comprobación final

- Banco vinculado al tercero correcto.
- Datos de cuenta revisados.
- Cuentas contables informadas.
- Opción **Activa** marcada.
- BIC/SWIFT informado si procede.
- Cuenta de confirming revisada.

## Errores habituales

### Error: cuenta bancaria para confirming no es correcta

**Causa probable:** la cuenta de confirming no coincide con la cuenta corriente o no está bien informada.

**Qué hacer:** revisar la ficha del banco antes de continuar.

### Error al generar fichero SEPA

**Causa probable:** falta el campo **BIC/SWIFT**.

**Qué hacer:** completar el dato en la ficha bancaria y volver a intentarlo.

[← Anterior](/simgest/operativa/tesoreria-contabilidad) | [Índice](/simgest/operativa/tesoreria-contabilidad) | [Siguiente →](/simgest/operativa/tesoreria-contabilidad/02-cartera-recibos)
