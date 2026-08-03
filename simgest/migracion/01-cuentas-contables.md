---
title: "1. Cuentas Contables: Configuración Inicial"
description: "Migración Factusol a SIMGEST: 1. Cuentas Contables: Configuración Inicial"
published: true
tags: simgest, migracion, factusol
editor: markdown
---

## 1. Conservar cuentas contables y códigos

La primera comprobación de la migración consiste en garantizar que SIMGEST recibe los mismos códigos comerciales y las mismas cuentas contables que ya se utilizan en Factusol. Esta correspondencia permite reconocer los registros, comparar ambos sistemas y mantener la continuidad contable durante la transición.

> **Objetivo**
>
> Mantener sin alteración los códigos de cliente, proveedor, acreedor o agente y las cuentas contables relacionadas, diferenciándolos del nuevo código interno de tercero que genera SIMGEST.

## Cuándo utilizar este procedimiento

Debe realizarse antes de ejecutar la migración de terceros y antes de validar el resultado importado. También debe repetirse cuando se recibe una nueva versión de los archivos de origen, porque pueden haberse añadido fichas o modificado datos desde la entrega anterior.

No debe utilizarse para decidir una renumeración ni para unificar registros únicamente porque compartan CIF. El material de origen establece que la correspondencia entre Factusol y SIMGEST debe respetarse.

## Por qué es un control crítico

En Factusol, el código comercial y la cuenta contable forman parte de la identificación práctica del cliente o proveedor. Si durante el traslado se cambia uno de estos valores, el registro puede seguir existiendo técnicamente, pero deja de coincidir con la referencia utilizada por el equipo y con los datos históricos.

SIMGEST incorpora además un código de tercero que no existía en Factusol. Ese nuevo identificador cumple una función interna y no sustituye al código comercial original. Confundir ambos códigos puede provocar que la migración parezca correcta en pantalla aunque la relación con el sistema de origen se haya perdido.

## Requisitos previos

Antes de comenzar deben estar disponibles:

- la versión más reciente del archivo de Factusol;
- el listado de terceros que entrarán en la migración;
- el código original de cada cliente, proveedor, acreedor o agente;
- la cuenta contable asociada;
- la identificación fiscal del registro;
- la indicación del rol o roles que desempeña;
- un registro donde anotar diferencias e incidencias.

Cuando existan varias entregas, no debe asumirse que contienen los mismos datos. El material de origen indica que entre versiones se modificaron cuentas bancarias, correos, teléfonos y fichas nuevas.

## Vista general

Preparar el inventario
→ clasificar cada rol
→ comparar código y cuenta
→ distinguir el código interno de tercero
→ revisar CIF con varios roles
→ registrar incidencias
→ validar el resultado

## Procedimiento

### Paso 1. Preparar el inventario de origen

**Qué debe hacer**

Extraiga o liste todos los registros que se van a migrar desde Factusol. Para cada registro, conserve como mínimo el código comercial, la cuenta contable, el CIF y el tipo de relación: cliente, proveedor, acreedor o agente.

**Por qué se hace**

Este inventario será la referencia contra la que se compare el resultado. Sin una lista de control no es posible saber si un código se ha alterado, si una cuenta se ha truncado o si una ficha se ha omitido.

**Qué debe comprobar**

- que no falten registros incluidos en la última entrega;
- que cada código tenga asociada su cuenta;
- que el rol esté identificado;
- que los registros con el mismo CIF no se hayan fusionado antes de analizar sus funciones.

**Resultado esperado**

Existe una relación de control completa y ordenada que permite localizar cualquier registro de origen y compararlo con SIMGEST.

[![Listado de terceros con las columnas de código, identificación y tipo de registro señaladas](/assets/simgest/migracion/mig_01_listado_terceros.png =70%x)](/assets/simgest/migracion/mig_01_listado_terceros.png)

*La captura muestra el listado utilizado como base para identificar los terceros que formarán parte de la migración. Ábrala a tamaño completo para revisar las columnas señaladas.*

### Paso 2. Conservar los códigos de Factusol

**Qué debe hacer**

Mantenga el código comercial exactamente como aparece en Factusol. La correspondencia documentada es directa: el código de origen debe continuar siendo el código del cliente, proveedor o agente en su tabla funcional de SIMGEST.

**Por qué se hace**

El código es una referencia reconocible por el equipo y permite rastrear el registro entre ambos sistemas. Renumerarlo durante la migración elimina esa relación directa y dificulta cualquier comprobación posterior.

**Qué debe comprobar**

- que el valor no se haya rellenado con ceros adicionales;
- que no se hayan eliminado dígitos;
- que no se haya sustituido por el código interno de tercero;
- que la misma referencia no se haya asignado a otro registro del mismo tipo.

### Paso 3. Conservar las cuentas contables

**Qué debe hacer**

Compare la cuenta de SIMGEST con la cuenta que figura en Factusol. El material de origen utiliza como ejemplo las cuentas del grupo 430 para clientes y del grupo 400 para proveedores y señala que deben mantenerse sus últimos dígitos originales.

**Por qué se hace**

La cuenta contable no es un campo descriptivo que pueda reconstruirse libremente. Forma parte del histórico y de la clasificación contable del registro. Un cambio puede afectar a la identificación y a futuras comprobaciones.

**Qué debe comprobar**

- número completo de la cuenta;
- grupo contable correspondiente;
- terminación original;
- relación con el código comercial;
- ausencia de renumeraciones manuales.

**Resultado esperado**

El código de Factusol y la cuenta contable conservan en SIMGEST la misma correspondencia que tenían en origen.

[![Ficha del tercero con las zonas de cliente, tercero y cuenta contable señaladas](/assets/simgest/migracion/mig_02_cuentas_codigos.png =70%x)](/assets/simgest/migracion/mig_02_cuentas_codigos.png)

*La captura permite distinguir el identificador interno del tercero de los datos específicos de cliente y de la cuenta contable.*

### Paso 4. Diferenciar el código interno de tercero

SIMGEST necesita un código de tercero que no existía en Factusol. Según el procedimiento documentado, este código se genera durante la migración y sirve como identificador interno.

**Qué debe hacer**

Acepte la creación del código interno, pero no lo utilice para reemplazar el código original de cliente, proveedor o agente.

**Qué debe comprobar**

- el tercero dispone de su identificador interno;
- la tabla funcional conserva el código de Factusol;
- el equipo puede seguir localizando el registro por su referencia habitual;
- el nuevo código no ha provocado la eliminación de otro dato.

El número exacto asignado al código de tercero no se considera relevante para la operativa diaria según el material de origen. Su proceso técnico de generación no debe modificarse desde este manual.

### Paso 5. Tratar un mismo CIF con varios roles

Un mismo CIF puede aparecer como cliente y como proveedor y contener información distinta en cada función.

**Qué debe hacer**

Mantenga los datos específicos de cliente en la tabla de clientes y los datos específicos de proveedor en la tabla de proveedores. Las notas y condiciones propias de cada función deben quedar asociadas al rol correspondiente.

**No debe hacerse**

- fusionar toda la información en una única ficha funcional;
- copiar las notas de cliente en proveedor o a la inversa;
- eliminar uno de los roles porque el CIF ya existe;
- asumir que ambos registros comparten todos los datos.

**Qué debe comprobar**

Abra cada función por separado y verifique que conserva sus datos. La ficha general de tercero sirve como elemento común, pero no debe borrar las diferencias operativas entre cliente y proveedor.

### Paso 6. Registrar las diferencias

Cuando un código, una cuenta o un rol no pueda confirmarse, no debe completarse por deducción. Registre:

- registro afectado;
- valor de Factusol;
- valor encontrado en SIMGEST;
- tipo de diferencia;
- acción pendiente;
- persona que debe validarla, cuando esté confirmada.

Si no existe evidencia suficiente para decidir, escriba exactamente: **Pendiente de validación por Hacchi**.

## Resultado esperado

Al finalizar, todos los registros migrados conservan sus códigos comerciales y cuentas contables de Factusol. SIMGEST dispone además de su código interno de tercero sin que este sustituya la referencia original. Los CIF con varios roles mantienen la información separada según su función.

## Comprobación final

- [ ] Se ha utilizado la última versión de los datos.
- [ ] Todos los registros de origen están incluidos en el inventario.
- [ ] Los códigos comerciales coinciden con Factusol.
- [ ] Las cuentas contables coinciden en número y terminación.
- [ ] El código interno de tercero no ha sustituido al código original.
- [ ] Cliente, proveedor, acreedor y agente se han tratado como funciones diferenciadas.
- [ ] Las notas de cada rol permanecen en su tabla correspondiente.
- [ ] Las diferencias están registradas y no se han resuelto por intuición.

## Errores habituales

| Error | Consecuencia | Detección | Actuación |
|---|---|---|---|
| Renumerar el código comercial | Se pierde la correspondencia directa con Factusol | El código no coincide con el inventario | Recuperar el valor original antes de validar. |
| Alterar la cuenta contable | El registro queda clasificado con una referencia distinta | La cuenta o su terminación difieren | Comparar con origen y corregir. |
| Usar el código de tercero como código de cliente | Se mezclan identificadores con funciones diferentes | La tabla de cliente no conserva el código original | Restaurar el código comercial. |
| Fusionar roles por CIF | Se pierden datos específicos de cliente o proveedor | Ambas funciones muestran la misma información sin justificación | Separar los datos en sus tablas. |
| Completar una cuenta dudosa por deducción | La migración incorpora un dato no validado | No existe respaldo en el archivo de origen | Pendiente de validación por Hacchi. |

---

[← Índice de migración](/simgest/migracion) · [2. Mapear formas de pago →](/simgest/migracion/02-mapeo-formas-pago)
