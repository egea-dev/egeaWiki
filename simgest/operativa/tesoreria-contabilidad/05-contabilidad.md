---
title: "5. Contabilidad"
description: "Manual de tesorería y contabilidad SIMGEST: 5. Contabilidad"
published: true
tags: simgest, operativa, tesoreria, contabilidad
editor: markdown
---

## 5. Contabilidad

Esta página reúne los bloques de contabilidad confirmados en el manual base: movimientos automáticos, borrador contable, plantillas, extractos, cierres, cuentas contables e importación masiva del PGC.

## Objetivo

Entender qué procesos contables se generan automáticamente, cómo crear o traspasar asientos desde borrador y qué criterios deben respetarse al trabajar con cuentas contables y cierres.

## 5.1 Movimientos automáticos

**Ruta confirmada:** `Contabilidad > Movimientos`

La formación indica que en esta pantalla se concentran los **asientos generados desde gestión**, entre ellos:

- ventas;
- compras;
- cobros;
- pagos;
- confirming.

El objetivo de este apartado es revisar el resultado contable ya generado por otros procesos del sistema.

## 5.2 Borrador contable

**Ruta confirmada:** `Contabilidad > Borrador`

El borrador permite preparar asientos antes de su traspaso a contabilidad.

### Crear un asiento

#### Cabecera

En la cabecera se documentan los siguientes campos:

- **Tipo** (Normal, Apertura, etc.).
- **Concepto**.
- **Fecha**.
- **Moneda**.

#### Detalle

En el detalle se informa:

- **Cuenta** (con búsqueda mediante **F3**).
- Uso de **“.”** para completar ceros, según la explicación del curso.
- **Importe** en **Debe/Haber**.

### Validar

La opción **Validar** comprueba:

- que el asiento esté cuadrado;
- que las cuentas existan.

### Traspasar a contabilidad

El botón **Traspasar a contabilidad** asigna **RIC** y envía el asiento a movimientos.

### Devolver

La devolución solo se permite, según el documento base, en asientos de tipo **Normal** y **requiere permisos**.

**Pendiente de validación por Hacchi** el detalle exacto de esos permisos.

### Regla crítica

La formación subraya una restricción importante:

> NO usar 472/477 en borrador. No generan impuesto.

Por tanto, si el objetivo es reflejar IVA con el comportamiento fiscal esperado, este tipo de cuenta no debe introducirse en borrador siguiendo el flujo mostrado.

<a href="/assets/simgest/operativa/tesoreria-contabilidad/07_borrador_contable_cabecera.png"><img src="/assets/simgest/operativa/tesoreria-contabilidad/07_borrador_contable_cabecera.png" alt="Borrador de apuntes contables con la zona de cabecera, los importes y el detalle del asiento señalizados." style="width: 70%; height: auto;" /></a>
<a href="/assets/simgest/operativa/tesoreria-contabilidad/08_borrador_contable_detalle_y_traspaso.png"><img src="/assets/simgest/operativa/tesoreria-contabilidad/08_borrador_contable_detalle_y_traspaso.png" alt="Borrador contable comparado con la pantalla de destino, señalando el detalle y la zona a la que se traspasa el asiento." style="width: 70%; height: auto;" /></a>
## 5.3 Plantillas

**Ruta confirmada:** `Contabilidad > Borrador > Exportar plantilla`

La recomendación documentada es usar **cuentas a nivel 5**, es decir, con todos los dígitos informados.

## 5.4 Extractos / Mayores

**Ruta confirmada:** `Contabilidad > Extractos`

Permite filtrar por:

- **cuenta**;
- **fechas**.

La documentación también confirma acceso a **histórico de ejercicios anteriores**.

## 5.5 Cierres mensuales

**Ruta confirmada:** `Contabilidad > Mantenimiento cierres contables`

Se contemplan bloqueos independientes para:

- Contabilidad;
- IVA;
- IRPF;
- Intracomunitarios.

La configuración puede ser **mensual o trimestral**.

## 5.6 PGC (Plan General Contable)

**Ruta confirmada:** `Contabilidad > Cuentas > Cuentas contables`

### Criterios confirmados

- **Nivel 5 obligatorio**.
- Grupo 4 **automático** → **no crear manualmente**: 430, 431, 431.1, 438, 400, 401, 410.
- Grupo 4 **manual sí**: 472, 477 (IVA), 47x (Hacienda), 465 (empleados).

El sentido práctico de esta regla es evitar crear manualmente cuentas que el sistema ya gestiona de forma automática por su propia lógica de terceros.

## 5.7 Importación masiva del PGC

La instrucción base es **enviar un Excel a Grupo SIM** con:

- **cuenta**;
- **título**.

### Qué no debe incluirse

- cuentas automáticas del grupo 4.

### Qué sí debe incluirse, si se utiliza

- IVA;
- cuentas de empleados.

<a href="/assets/simgest/operativa/tesoreria-contabilidad/09_plantillas_y_extractos.png"><img src="/assets/simgest/operativa/tesoreria-contabilidad/09_plantillas_y_extractos.png" alt="Pantalla de plantillas y extractos con las áreas principales de exportación, listado y consulta señalizadas." style="width: 70%; height: auto;" /></a>
## Comprobación final

- Asiento correctamente informado en borrador.
- Validación realizada.
- Traspaso efectuado cuando corresponda.
- Cuentas a nivel 5 en plantillas.
- Cierres configurados según la política deseada.
- No creación manual de cuentas automáticas del grupo 4.

## Errores habituales

### Usar 472/477 en borrador

**Consecuencia:** no se genera el impuesto según el comportamiento esperado.

**Qué hacer:** respetar la regla indicada en la formación.

### Crear manualmente cuentas automáticas del grupo 4

**Consecuencia:** duplicidad o incoherencia con la lógica automática del sistema.

**Qué hacer:** utilizar solo las cuentas que el manual base identifica como manuales.

[← Anterior](/simgest/operativa/tesoreria-contabilidad/04-remesas-cobro) | [Índice](/simgest/operativa/tesoreria-contabilidad) | [Siguiente →](/simgest/operativa/tesoreria-contabilidad/06-nominas-empleados)
