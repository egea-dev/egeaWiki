---
title: "2. Mapeo de Formas de Pago"
description: "Migración Factusol a SIMGEST: 2. Mapeo de Formas de Pago"
published: true
tags: simgest, migracion, factusol
editor: markdown
---

## 2. Mapear formas de pago

Factusol y SIMGEST utilizan sus propios códigos para identificar las formas de pago. Por este motivo, copiar el código numérico de un sistema al otro no garantiza que se mantenga la misma condición. La migración necesita una tabla de correspondencias que relacione el significado de cada código de origen con el registro adecuado de SIMGEST.

> **Objetivo**
>
> Asignar a cada forma de pago utilizada en Factusol una equivalencia válida en SIMGEST, dejando identificados los casos provisionales y los códigos que requieren crear una nueva opción.

## Cuándo utilizar este procedimiento

Debe realizarse antes de importar clientes, proveedores o cualquier ficha que dependa de una forma de pago. También debe revisarse si aparece en los datos de origen un código que no figuraba en el inventario inicial.

No debe asumirse que dos códigos iguales significan lo mismo. La comparación debe hacerse por descripción y condición, no solo por número.

## Riesgo que evita

Una asignación incorrecta puede dejar una ficha con una condición de cobro o pago distinta a la que se utilizaba en Factusol. El registro puede importarse sin mostrar un error técnico, pero la operativa posterior partiría de un dato equivocado. Por eso, la trazabilidad del mapeo debe mantenerse incluso cuando se utiliza un valor provisional.

## Requisitos previos

- listado completo de códigos de forma de pago usados en Factusol;
- descripción asociada a cada código;
- acceso a la tabla o selector de formas de pago de SIMGEST;
- relación de formas de pago disponibles en SIMGEST;
- documento de mapeo con columnas para origen, destino y estado;
- criterio validado para crear nuevas formas de pago o usar una provisional.

El criterio definitivo para elegir entre crear una forma de pago nueva o asignar temporalmente **Contado** es **Pendiente de validación por Hacchi**.

## Vista general

Inventariar códigos de Factusol
→ consultar opciones de SIMGEST
→ comparar por significado
→ asignar equivalencias
→ resolver códigos sin destino
→ registrar provisionalidades
→ revisar antes de migrar

## Procedimiento

### Paso 1. Inventariar las formas de pago de Factusol

**Qué debe hacer**

Liste todos los códigos utilizados en las fichas de origen y escriba junto a cada código su descripción completa.

**Por qué se hace**

El código por sí solo no permite conocer la condición. El inventario debe mostrar qué significa cada valor y cuántos registros dependen de él.

**Qué debe comprobar**

- que no queden códigos sin descripción;
- que se han incluido códigos poco utilizados;
- que no existan dos descripciones diferentes bajo un mismo código;
- que la lista procede de la versión más reciente de los datos.

**Resultado esperado**

Existe un inventario único de formas de pago de origen, preparado para comparar con SIMGEST.

### Paso 2. Consultar las formas de pago disponibles en SIMGEST

**Qué debe hacer**

Abra la tabla auxiliar o el selector de formas de pago de SIMGEST y documente los códigos y descripciones disponibles.

[![Selector de forma de pago con el código y la descripción señalados](/assets/simgest/migracion/mig_03_forma_pago.png =70%x)](/assets/simgest/migracion/mig_03_forma_pago.png)

*La captura muestra la zona que debe revisarse para comparar el código de SIMGEST con su descripción.*

**Qué debe comprobar**

- código interno;
- descripción visible;
- posibles opciones que parecen similares;
- existencia de la forma de pago equivalente;
- ausencia de duplicados con nombres distintos.

No debe elegirse una opción únicamente porque su nombre se parezca. Cuando la condición exacta no pueda comprobarse, debe quedar pendiente de validación.

### Paso 3. Crear la tabla de correspondencias

Prepare una tabla con, como mínimo, estas columnas:

| Código Factusol | Descripción Factusol | Código SIMGEST | Descripción SIMGEST | Estado | Observaciones |
|---|---|---|---|---|---|
| Valor de origen | Condición de origen | Valor de destino | Condición de destino | Definitivo / Provisional / Pendiente | Explicación |

**Qué debe hacer**

Compare cada forma de pago de Factusol con las opciones disponibles en SIMGEST. La equivalencia se considera directa solo cuando el significado coincide.

**Qué debe comprobar**

- que todos los códigos de origen aparecen una sola vez;
- que cada código tiene un destino o una incidencia;
- que el estado indica si la decisión es definitiva o provisional;
- que cualquier diferencia queda explicada.

### Paso 4. Asignar las coincidencias directas

Cuando exista una forma de pago equivalente:

1. registre el código de SIMGEST;
2. copie su descripción exacta;
3. marque la correspondencia como definitiva;
4. revise una muestra de fichas después de la migración.

**Resultado esperado**

Los registros migrados conservan una condición equivalente a la de Factusol aunque el código interno de SIMGEST sea diferente.

### Paso 5. Resolver códigos sin equivalencia

El material de origen contempla dos alternativas:

- crear una nueva forma de pago en SIMGEST;
- asignar temporalmente **Contado**.

Estas opciones no son intercambiables. Antes de elegir debe conocerse el criterio corporativo aplicable. Hasta que se confirme, registre el caso como **Pendiente de validación por Hacchi**.

Si se autoriza una asignación provisional:

- identifique el código de origen;
- registre el valor provisional utilizado;
- indique por qué no existe equivalencia;
- mantenga una lista de fichas afectadas;
- programe su corrección cuando la forma de pago definitiva esté disponible.

### Paso 6. Revisar la aplicación del mapeo

Después de importar, seleccione registros representativos de cada código y compruebe:

- forma de pago mostrada en la ficha;
- coincidencia con la tabla de correspondencias;
- estado definitivo o provisional;
- ausencia de fichas sin valor;
- ausencia de códigos de origen interpretados como códigos de SIMGEST.

## Resultado esperado

Todas las formas de pago de Factusol tienen una equivalencia documentada en SIMGEST o una incidencia registrada. Las asignaciones provisionales son identificables y pueden corregirse sin volver a analizar toda la migración.

## Comprobación final

- [ ] Se han inventariado todos los códigos de origen.
- [ ] Cada código incluye su descripción.
- [ ] Se ha documentado la lista de opciones de SIMGEST.
- [ ] Las coincidencias se han realizado por significado.
- [ ] No quedan códigos sin destino ni incidencia.
- [ ] Las asignaciones provisionales están identificadas.
- [ ] Se ha revisado una muestra de registros después de la migración.

## Errores habituales

| Error | Consecuencia | Cómo detectarlo | Actuación |
|---|---|---|---|
| Copiar el mismo número de código | Puede representar otra condición en SIMGEST | Descripción de destino distinta | Rehacer la correspondencia por significado. |
| Omitir códigos poco utilizados | Algunas fichas quedan sin forma de pago | Registros importados sin valor | Completar el inventario y mapearlos. |
| Usar Contado sin registrar la incidencia | El valor provisional parece definitivo | No existe lista de afectados | Documentar y revisar las fichas. |
| Crear una forma de pago sin criterio confirmado | Se añade una opción no validada | No existe autorización funcional | Pendiente de validación por Hacchi. |

---

[← 1. Conservar cuentas y códigos](/simgest/migracion/01-cuentas-contables) · [Índice de migración](/simgest/migracion) · [3. Mapear localidades →](/simgest/migracion/03-mapeo-localidades)
