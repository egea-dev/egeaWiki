---
title: "6. Nóminas y empleados"
description: "Manual de tesorería y contabilidad SIMGEST: 6. Nóminas y empleados"
published: true
tags: simgest, operativa, tesoreria, contabilidad
editor: markdown
---

## 6. Nóminas y empleados

Esta entrada recoge los pasos confirmados para crear empleados a partir de terceros, configurar sus cuentas de nómina y entender la contabilización vinculada.

## Objetivo

Dejar preparado al empleado para su tratamiento contable y de tesorería, incluyendo las cuentas de nómina necesarias y la contabilización de retenciones.

## 6.1 Alta de empleados

**Ruta confirmada:** `Terceros > [Tercero] > Crear como empleado`

### Qué debe hacer

Parta de un tercero ya existente y utilice la opción **Crear como empleado**.

### Qué ocurre

El sistema genera una **ficha con código de empleado** a partir del tercero seleccionado.

### Qué debe comprobar

- Que el tercero base sea correcto.
- Que el empleado quede creado con su código correspondiente.

## 6.2 Cuentas de nómina

**Ruta confirmada:** `[Empleado] > Cuentas nóminas`

En esta sección deben existir las cuentas contables necesarias para el tratamiento de la nómina. La formación menciona expresamente:

- **Remuneración pendiente (465)**.
- **Sueldos (640)**.
- **SS (642)**.
- **Dietas**.
- **Embargos**.
- **IRPF**.

El documento base advierte que estas cuentas **deben existir en el PGC**. Por tanto, no basta con abrir la ficha del empleado: la estructura contable debe estar preparada previamente.

## 6.3 Contabilización

**Ruta confirmada:** `Contabilidad > Retenciones de empleados`

La contabilización:

- genera un **recibo en cartera**;
- genera un **asiento contable automático**;
- permite posteriormente **remesa confirming para pago**.

Esto conecta el área laboral con tesorería y contabilidad, por lo que es importante revisar que tanto el empleado como sus cuentas estén correctamente configurados antes de ejecutar el proceso.

## 6.4 Importación masiva

La formación indica tres requisitos previos:

- empleados existentes;
- cuentas creadas en el PGC;
- Excel procedente del asesor.

<a href="/assets/simgest/operativa/tesoreria-contabilidad/10_empleados_y_cuentas_nomina.png"><img src="/assets/simgest/operativa/tesoreria-contabilidad/10_empleados_y_cuentas_nomina.png" alt="Ficha de empleado y ventana de cuentas de nómina con la identificación del tercero, la zona de cuentas y el bloque inferior señalizados." style="width: 70%; height: auto;" /></a>
## Comprobación final

- Tercero convertido correctamente en empleado.
- Código de empleado generado.
- Cuentas de nómina existentes en PGC.
- Retenciones contabilizables desde la ruta indicada.

## Errores habituales

### Falta alguna cuenta de nómina

**Consecuencia:** el proceso de contabilización o importación puede quedar incompleto o fallar.

**Qué hacer:** revisar primero el PGC y la ficha del empleado.

[← Anterior](/simgest/operativa/tesoreria-contabilidad/05-contabilidad) | [Índice](/simgest/operativa/tesoreria-contabilidad) | [Siguiente →](/simgest/operativa/tesoreria-contabilidad/07-cartas-cobro)
