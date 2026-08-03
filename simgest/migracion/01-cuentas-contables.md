---
title: "1. Cuentas Contables: Configuración Inicial"
description: "Migración Factusol a SIMGEST: 1. Cuentas Contables: Configuración Inicial"
published: true
tags: simgest, migracion, factusol
editor: markdown
---

## 1. Conservar cuentas contables y códigos

> **Objetivo**
>
> Mantener en SIMGEST los códigos de cliente o proveedor y las cuentas contables procedentes de Factusol, sin alterar los valores que deban conservarse.

## Cuándo utilizar este procedimiento

Utiliza este procedimiento antes de migrar terceros, clientes, proveedores y acreedores. Su finalidad es preparar una correspondencia verificable entre los datos de origen y los datos que quedarán registrados en SIMGEST.

## Requisitos previos

- Relación actualizada de terceros de Factusol.
- Código original de cada cliente, proveedor o agente.
- Cuenta contable asociada a cada registro.
- Identificación de los registros que comparten CIF pero tienen funciones distintas.
- Confirmación de que se está utilizando la última entrega de datos.

## Vista general

Inventariar códigos y cuentas
→ comprobar correspondencias
→ generar el código interno de tercero
→ mantener separados los roles
→ revisar el resultado

## Procedimiento

### Paso 1. Preparar el inventario de origen

**Qué debe hacer:** extrae o lista los códigos y las cuentas contables que se utilizan en Factusol.

**Para qué sirve:** permite comparar el origen con el resultado de la migración y detectar alteraciones antes de comenzar la operativa.

**Qué debe comprobar:** el listado debe incluir todos los registros que se van a migrar y debe distinguir, cuando proceda, entre cliente, proveedor, acreedor o agente.

**Resultado esperado:** existe una relación de control con el código original y la cuenta contable de cada registro.

[![Listado de terceros con las columnas de código, identificación y tipo de registro señaladas](/assets/simgest/migracion/mig_01_listado_terceros.png =70%x)](/assets/simgest/migracion/mig_01_listado_terceros.png)

*Listado utilizado para revisar los terceros que formarán parte de la migración. Pulsa la imagen para abrirla a tamaño completo.*

### Paso 2. Mantener la correspondencia original

**Qué debe hacer:** conserva los códigos y las cuentas contables tal como se reciben desde Factusol.

**Criterio documentado:** si un cliente tiene un código determinado y una cuenta del grupo 430 con la misma terminación, ambos valores deben mantenerse. Para proveedores, se revisan las cuentas del grupo 400 y su terminación original.

**Qué debe comprobar:**

- el código del registro coincide con el de Factusol;
- la cuenta contable conserva el valor original;
- los últimos dígitos no se han cambiado durante el traspaso;
- no se ha aplicado una renumeración manual.

**Resultado esperado:** código de Factusol y cuenta contable mantienen una correspondencia directa en SIMGEST.

[![Ficha del tercero con las zonas de cliente, tercero y cuenta contable señaladas](/assets/simgest/migracion/mig_02_cuentas_codigos.png =70%x)](/assets/simgest/migracion/mig_02_cuentas_codigos.png)

*Ficha utilizada para comparar el código del tercero con sus datos de cliente y cuenta contable. Pulsa la imagen para abrirla a tamaño completo.*

### Paso 3. Diferenciar el código interno de tercero

SIMGEST incorpora un código de tercero que no existía en Factusol. Según el procedimiento de migración, este código se genera durante el traspaso y funciona como identificador interno.

**Qué debe comprobar:** al convertir o relacionar el tercero con cliente, proveedor o agente, deben seguir conservándose los códigos originales de Factusol en las tablas correspondientes.

**No debe hacerse:** utilizar el nuevo código interno como sustituto del código original de cliente o proveedor.

### Paso 4. Tratar un mismo CIF con varios roles

Un mismo CIF puede aparecer como cliente y como proveedor con datos diferentes.

- Los datos propios de cliente deben permanecer en la tabla de clientes.
- Los datos propios de proveedor deben permanecer en la tabla de proveedores.
- Las notas de cada rol deben incorporarse al registro correspondiente.
- No deben mezclarse los datos de ambos roles en una única ficha funcional.

## Resultado esperado

Los terceros quedan identificados en SIMGEST y los códigos y cuentas que proceden de Factusol conservan sus valores. Cuando un CIF tiene varios roles, cada uno mantiene sus datos específicos.

## Comprobación final

- [ ] Se ha utilizado la versión más reciente de los datos.
- [ ] Todos los códigos de origen están incluidos en el control.
- [ ] Las cuentas contables coinciden con Factusol.
- [ ] El código interno de tercero no ha sustituido al código comercial original.
- [ ] Los roles de cliente y proveedor permanecen separados.
- [ ] Las diferencias detectadas están registradas para corrección.

## Errores habituales

| Error | Cómo detectarlo | Actuación |
|---|---|---|
| Código comercial renumerado | No coincide con Factusol | Detener la validación y recuperar el valor original. |
| Cuenta contable modificada | La cuenta o su terminación es distinta | Comparar con el inventario de origen antes de continuar. |
| Datos de cliente y proveedor mezclados | Un rol contiene notas o datos del otro | Separar la información en las tablas correspondientes. |
| Duda sobre la asignación de un registro | La fuente no permite confirmar el rol | Pendiente de validación por Hacchi |

---

[Índice de migración](/simgest/migracion) · [2. Mapear formas de pago →](/simgest/migracion/02-mapeo-formas-pago)
