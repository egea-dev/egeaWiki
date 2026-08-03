---
title: "4. Creación de una Nueva Localidad en Simgest (Paso a paso)"
description: "Migración Factusol a SIMGEST: 4. Creación de una Nueva Localidad en Simgest (Paso a paso)"
published: true
tags: simgest, migracion, factusol
editor: markdown
---

## 4. Crear una localidad

Una localidad debe darse de alta cuando la combinación correcta de país, provincia o región, nombre y código postal no existe en la tabla auxiliar de SIMGEST. Este procedimiento debe realizarse con cuidado porque el registro creado podrá utilizarse posteriormente en múltiples fichas de terceros.

> **Objetivo**
>
> Crear una localidad completa y correctamente relacionada con su país y provincia o región para que pueda asignarse a un tercero sin introducir datos territoriales incoherentes.

## Cuándo utilizar este procedimiento

Utilícelo únicamente después de comprobar que la localidad no existe. Es más habitual que sea necesario para ubicaciones fuera de España; el material de origen indica que en España la mayoría de las localidades ya están registradas.

No debe utilizarse para corregir una grafía sin confirmar si existe un registro equivalente, ni para crear una segunda localidad porque la búsqueda inicial no haya devuelto el resultado esperado.

## Requisitos previos

- nombre oficial de la localidad;
- código postal;
- país;
- provincia, región, condado, departamento o estado equivalente;
- comprobación previa en las tablas auxiliares;
- dirección del tercero que origina la necesidad;
- autorización funcional para crear datos maestros, si aplica.

La identificación de los perfiles autorizados para crear localidades es **Pendiente de validación por Hacchi**.

## Vista general

Confirmar que no existe
→ comprobar país
→ comprobar provincia o región
→ crear dependencias ausentes
→ crear localidad
→ guardar
→ volver a buscar
→ asignar al tercero

## Procedimiento

### Paso 1. Confirmar que la localidad no existe

**Qué debe hacer**

Busque por código postal y nombre. Revise las variantes que puedan corresponder a la misma entidad y compruebe la jerarquía territorial.

**Por qué se hace**

Crear un duplicado puede provocar que distintos usuarios seleccionen códigos diferentes para la misma localidad. La información dejaría de estar normalizada y las búsquedas posteriores serían menos fiables.

**Qué debe comprobar**

- coincidencias exactas;
- coincidencias con otra grafía;
- registros con el mismo código postal;
- provincia o región;
- país.

Solo continúe cuando haya evidencia de que no existe un registro válido.

### Paso 2. Acceder a las tablas auxiliares

Abra las tablas auxiliares y localice primero países y provincias o regiones. La localidad depende de estos registros y no debe crearse sin comprobarlos.

[![Tabla auxiliar de provincias con la relación territorial señalada](/assets/simgest/migracion/mig_05_tabla_provincias.png =70%x)](/assets/simgest/migracion/mig_05_tabla_provincias.png)

*La captura muestra la tabla que debe revisarse antes de asociar una provincia o región a la nueva localidad.*

### Paso 3. Revisar o crear el país

**Si el país existe**

Selecciónelo y compruebe que es el correcto.

**Si el país no existe**

El material de origen indica que debe darse de alta en la tabla de países antes de continuar. No se dispone en las fuentes de todos los campos requeridos para ese alta; por tanto, cualquier dato adicional no visible es **Pendiente de validación por Hacchi**.

**Qué debe comprobar**

- nombre del país;
- ausencia de duplicados;
- relación correcta con la provincia o región que se utilizará.

### Paso 4. Revisar o crear la provincia o región

La organización territorial depende del país. Puede tratarse de provincia, región, condado, departamento o estado.

**Qué debe hacer**

Busque el registro correspondiente y compruebe que está vinculado al país correcto. Si no existe, créelo antes de crear la localidad.

**Riesgo que evita**

Una provincia con el mismo nombre puede existir en otro país o puede haberse creado con una jerarquía incorrecta. La localidad heredaría esa relación y mostraría datos territoriales erróneos.

### Paso 5. Crear la localidad

Abra el alta de localidades.

[![Ficha de alta de localidad con los campos territoriales señalados](/assets/simgest/migracion/mig_06_ficha_localidad.png =70%x)](/assets/simgest/migracion/mig_06_ficha_localidad.png)

*La captura muestra la ficha donde se registran el nombre, el código postal y las relaciones territoriales.*

**Introduzca únicamente los datos confirmados:**

- nombre oficial de la localidad;
- código postal;
- país;
- provincia o región.

El código interno de localidad se asigna automáticamente según el material de origen. No debe introducirse manualmente salvo que el sistema muestre un comportamiento distinto, en cuyo caso será **Pendiente de validación por Hacchi**.

### Paso 6. Guardar y comprobar el registro

Guarde la localidad y vuelva a buscarla en la tabla.

**Qué debe comprobar**

- el registro aparece una sola vez;
- el código postal es correcto;
- el nombre no está truncado;
- país y provincia son correctos;
- el sistema ha generado el código interno.

**Resultado esperado**

La nueva localidad aparece disponible para selección y conserva la jerarquía territorial correcta.

### Paso 7. Asignar la localidad al tercero

Vuelva a la ficha del tercero y seleccione el código recién creado.

[![Ficha del tercero con la localidad creada y los datos territoriales señalados](/assets/simgest/migracion/mig_07_asignar_localidad_tercero.png =70%x)](/assets/simgest/migracion/mig_07_asignar_localidad_tercero.png)

*La captura muestra la comprobación posterior en la ficha del tercero.*

**Qué debe comprobar**

El material de origen indica que la selección de la localidad completa automáticamente provincia, país y código postal. Revise esos datos antes de guardar el tercero.

### Paso 8. Registrar el alta en el control de migración

Anote:

- localidad creada;
- código postal;
- país y provincia;
- código interno asignado;
- tercero que originó el alta;
- fecha de creación;
- observaciones.

Este registro evita repetir la investigación si la misma combinación aparece en otra ficha.

## Resultado esperado

La localidad queda registrada una sola vez, vinculada a la jerarquía correcta y disponible para asignar a los terceros que compartan esa ubicación.

## Comprobación final

- [ ] Se ha comprobado que la localidad no existía.
- [ ] El país es correcto.
- [ ] La provincia o región está vinculada al país correcto.
- [ ] El nombre y el código postal están confirmados.
- [ ] El código interno ha sido generado por SIMGEST.
- [ ] La localidad puede seleccionarse desde la ficha del tercero.
- [ ] Los campos territoriales se completan correctamente.
- [ ] El alta está registrada en el control de migración.

## Errores habituales

| Error | Consecuencia | Prevención | Actuación |
|---|---|---|---|
| Crear sin buscar variantes | Localidad duplicada | Buscar por nombre y CP | Revisar y corregir antes de usarla. |
| Asociar una provincia de otro país | Dirección territorial incoherente | Comprobar jerarquía | Corregir la relación. |
| Escribir manualmente un código interno | Posible conflicto de identificadores | Permitir la generación automática | Pendiente de validación por Hacchi si el sistema lo exige. |
| No revisar la ficha del tercero | El error se detecta demasiado tarde | Comprobar autocompletado | Corregir antes de guardar. |

---

[← 3. Mapear localidades](/simgest/migracion/03-mapeo-localidades) · [Índice de migración](/simgest/migracion) · [5. Utilizar Desconocida →](/simgest/migracion/05-localidad-desconocida)
