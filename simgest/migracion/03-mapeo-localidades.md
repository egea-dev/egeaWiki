---
title: "3. Mapeo de Localidades (El proceso más complejo)"
description: "Migración Factusol a SIMGEST: 3. Mapeo de Localidades (El proceso más complejo)"
published: true
tags: simgest, migracion, factusol
editor: markdown
---

## 3. Mapear localidades

El mapeo de localidades es la parte más compleja de la migración porque Factusol y SIMGEST no almacenan la ubicación con la misma estructura. Factusol aporta principalmente el código postal y el nombre de la localidad, mientras que SIMGEST exige seleccionar un código interno de localidad relacionado con país, provincia o región y código postal.

> **Objetivo**
>
> Relacionar cada combinación de código postal y localidad de Factusol con el registro correcto de SIMGEST, evitando asignaciones automáticas que no correspondan a la dirección real.

## Cuándo utilizar este procedimiento

Debe realizarse antes de importar terceros y siempre que una ficha no pueda guardarse porque falta el código interno de localidad. También se utiliza durante la revisión posterior para comprobar asignaciones dudosas.

## Diferencia entre los sistemas

| Aspecto | Factusol | SIMGEST |
|---|---|---|
| Dato disponible | Código postal y nombre | País, provincia o región, localidad y código postal |
| Código de localidad | No existe | Código interno único |
| Requisito para guardar | No exige código interno | El código de localidad es obligatorio |

Esta diferencia obliga a transformar el dato. No basta con copiar el texto de la localidad, porque SIMGEST necesita relacionarlo con un registro existente en su tabla auxiliar.

## Riesgo que evita

Un código postal puede corresponder a varias entidades, barrios, parroquias o distritos. El material de origen indica que, cuando se busca únicamente por código postal, SIMGEST puede devolver la primera localidad encontrada. Esa coincidencia técnica no garantiza que la localidad sea la correcta.

El riesgo es especialmente relevante en Mallorca, Galicia y Asturias, donde pueden existir varias denominaciones o entidades asociadas a un mismo código postal.

## Requisitos previos

- código postal de cada tercero;
- nombre de localidad de Factusol;
- dirección completa cuando sea necesaria para decidir;
- tabla de localidades de SIMGEST;
- datos de país y provincia o región;
- listado de combinaciones únicas;
- registro de incidencias.

## Vista general

Extraer combinaciones únicas
→ ordenar por código postal
→ buscar en SIMGEST
→ comprobar país y provincia
→ validar coincidencia exacta
→ revisar coincidencias múltiples
→ crear o marcar la localidad pendiente

## Procedimiento

### Paso 1. Preparar las combinaciones de origen

**Qué debe hacer**

Extraiga de Factusol el código postal y el nombre de localidad de cada tercero. Agrupe las combinaciones repetidas para que una misma localidad se analice una sola vez.

**Por qué se hace**

Trabajar con combinaciones únicas reduce el número de búsquedas y evita aplicar criterios distintos a registros que comparten la misma ubicación.

**Qué debe comprobar**

- códigos postales completos;
- nombres sin recortes;
- variantes ortográficas;
- espacios o abreviaturas que puedan ocultar duplicados;
- país de los registros no españoles.

**Resultado esperado**

Existe una lista ordenada por código postal con todas las combinaciones que deben buscarse en SIMGEST.

### Paso 2. Acceder a las tablas auxiliares

Abra el módulo de tablas auxiliares y localice las tablas relacionadas con países, provincias y localidades.

[![Ruta de acceso a tablas auxiliares con las opciones territoriales señaladas](/assets/simgest/migracion/mig_04_ruta_tablas_auxiliares.png =70%x)](/assets/simgest/migracion/mig_04_ruta_tablas_auxiliares.png)

*La captura muestra el acceso documentado a las tablas necesarias para revisar la jerarquía territorial.*

**Qué debe comprobar**

No empiece creando registros. Primero determine si el país, la provincia y la localidad ya existen. En España, el material de origen indica que la mayoría de las localidades deberían estar disponibles.

### Paso 3. Resolver una coincidencia completa

**Qué debe hacer**

Busque la combinación de código postal y localidad. Cuando aparezca una coincidencia, revise también país y provincia o región.

**La coincidencia se considera completa cuando:**

- coincide el código postal;
- coincide el nombre o corresponde inequívocamente a la misma entidad;
- coincide la provincia o región;
- coincide el país;
- la dirección del tercero es coherente con el registro.

**Resultado esperado**

Se identifica el código interno de localidad y puede asignarse al tercero sin crear registros nuevos.

### Paso 4. Revisar coincidencias por código postal

Cuando el código postal coincide pero el nombre es diferente, no debe aceptarse la primera opción sin revisión.

**Qué debe hacer**

1. compare las localidades asociadas al código postal;
2. consulte la dirección completa del tercero;
3. revise provincia y país;
4. determine si la diferencia es una variante de nombre, un barrio, una parroquia o una entidad distinta;
5. registre el caso cuando no exista certeza.

**Resultado posible**

El material de origen permite asignar el código encontrado y marcarlo para revisión posterior cuando el nombre exacto no coincide. Esta decisión debe quedar documentada; no debe ocultarse como una coincidencia definitiva.

### Paso 5. Aplicar el control especial de Mallorca y otras zonas con entidades múltiples

En Palma y otras zonas puede haber barrios o distritos asociados a códigos postales concretos. En Galicia y Asturias pueden existir parroquias u otras entidades con denominaciones diferentes.

**Qué debe comprobar**

- calle y número cuando estén disponibles;
- municipio real;
- provincia;
- país;
- coherencia entre el nombre de Factusol y la opción de SIMGEST.

Si la dirección no permite decidir con seguridad: **Pendiente de validación por Hacchi**.

### Paso 6. Tratar una localidad inexistente

Cuando no se encuentra una coincidencia válida existen dos vías documentadas:

- crear la localidad en SIMGEST;
- utilizar de forma provisional la localidad **Desconocida**.

La creación se explica en [Crear una localidad](/simgest/migracion/04-crear-localidad). El uso provisional se explica en [Utilizar la localidad Desconocida](/simgest/migracion/05-localidad-desconocida).

No debe crearse una localidad duplicada sin comprobar antes país, provincia, nombre y código postal.

### Paso 7. Aplicar el código a los terceros afectados

Una vez resuelta una combinación, utilice el mismo código de localidad para los terceros que compartan exactamente esa ubicación de origen.

**Qué debe comprobar después de la asignación**

- el código postal mostrado;
- localidad;
- provincia o región;
- país;
- coherencia con la dirección del tercero.

## Resultado esperado

Cada tercero dispone de un código de localidad válido de SIMGEST. Las coincidencias dudosas, las localidades creadas y los valores provisionales están documentados para poder revisarlos posteriormente.

## Comprobación final

- [ ] La lista de combinaciones únicas está completa.
- [ ] Las búsquedas se han realizado por código postal y nombre.
- [ ] Se han comprobado país y provincia.
- [ ] Las coincidencias múltiples se han revisado con la dirección.
- [ ] No se ha aceptado automáticamente la primera localidad del código postal.
- [ ] Las localidades inexistentes se han tratado mediante el procedimiento correspondiente.
- [ ] Los casos dudosos están registrados.

## Errores habituales

| Error | Consecuencia | Detección | Actuación |
|---|---|---|---|
| Buscar solo por código postal | Puede asignarse otra entidad del mismo CP | El nombre o dirección no coinciden | Revisar todas las opciones del código. |
| Crear una localidad que ya existe | Se duplican registros territoriales | Mismo país, provincia y CP con otra grafía | Comparar antes de crear. |
| Ignorar país o provincia | Se selecciona una localidad homónima | La jerarquía territorial es distinta | Corregir la asignación. |
| Marcar como definitiva una coincidencia dudosa | La incidencia desaparece del control | No existe evidencia suficiente | Registrar para revisión. |

---

[← 2. Mapear formas de pago](/simgest/migracion/02-mapeo-formas-pago) · [Índice de migración](/simgest/migracion) · [4. Crear una localidad →](/simgest/migracion/04-crear-localidad)
