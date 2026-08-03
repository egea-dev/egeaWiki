---
title: "4. Creación de una Nueva Localidad en Simgest (Paso a paso)"
description: "Migración Factusol a SIMGEST: 4. Creación de una Nueva Localidad en Simgest (Paso a paso)"
published: true
tags: simgest, migracion, factusol
editor: markdown
---

## 4. Crear una localidad

> **Objetivo**
>
> Dar de alta en SIMGEST una localidad que no existe en su tabla auxiliar y asignarla posteriormente al tercero correspondiente.

## Cuándo utilizar este procedimiento

Utilízalo cuando el código postal o la localidad de origen no tenga un registro válido en SIMGEST y la dirección pueda identificarse correctamente.

No utilices este procedimiento para crear una localidad dudosa. En ese caso, aplica [Localidad Desconocida](/simgest/migracion/05-localidad-desconocida) y registra la incidencia.

## Requisitos previos

- Código postal confirmado.
- Nombre oficial de la localidad.
- País correspondiente.
- Provincia, región, condado, departamento o estado aplicable.
- Confirmación de que la localidad no existe ya con otra denominación.

## Vista general

Confirmar que no existe
→ abrir tablas auxiliares
→ crear país o provincia si falta
→ crear localidad
→ guardar
→ asignar al tercero

## Procedimiento

### Paso 1. Confirmar que la localidad no existe

Busca el código postal y el nombre antes de crear un registro nuevo. El procedimiento de origen indica que, al intentar utilizar una localidad inexistente, el sistema no encuentra el código interno necesario.

**Qué debe comprobar:** realiza la búsqueda por código postal y por nombre para evitar duplicados.

### Paso 2. Acceder a las tablas auxiliares

Abre el área desde la que se gestionan países, provincias y localidades.

[![Ruta visual hacia las tablas auxiliares geográficas de SIMGEST](/assets/simgest/migracion/mig_04_ruta_tablas_auxiliares.png =70%x)](/assets/simgest/migracion/mig_04_ruta_tablas_auxiliares.png)

*Acceso a las tablas de países, provincias y localidades. Pulsa la imagen para abrirla a tamaño completo.*

### Paso 3. Revisar o crear el país

Si el país ya existe, selecciónalo. Si no existe, la fuente indica que debe darse de alta antes de continuar con la localidad.

**Datos obligatorios y procedimiento exacto para crear un país:** Pendiente de validación por Hacchi

### Paso 4. Revisar o crear la provincia o región

Selecciona la división administrativa aplicable al país. La fuente menciona provincias para España y estructuras equivalentes para otros países.

Si no existe, créala asociándola al país correspondiente.

[![Tabla de provincias con los campos de país, código y título señalados](/assets/simgest/migracion/mig_05_tabla_provincias.png =70%x)](/assets/simgest/migracion/mig_05_tabla_provincias.png)

*Pantalla utilizada para revisar o dar de alta la provincia asociada al país. Pulsa la imagen para abrirla a tamaño completo.*

**Qué debe comprobar:** el país seleccionado en la provincia debe ser el mismo que se utilizará en la localidad.

### Paso 5. Crear la localidad

1. Abre una ficha nueva de localidad.
2. Introduce el código postal.
3. Introduce el nombre oficial.
4. Selecciona el país.
5. Selecciona la provincia o región.
6. Revisa la combinación completa antes de guardar.

[![Ficha de localidad con código postal, nombre, país y provincia señalados](/assets/simgest/migracion/mig_06_ficha_localidad.png =70%x)](/assets/simgest/migracion/mig_06_ficha_localidad.png)

*Campos que deben revisarse antes de guardar una localidad nueva. Pulsa la imagen para abrirla a tamaño completo.*

El procedimiento indica que SIMGEST asigna automáticamente el código interno de localidad. No lo sustituyas por el código postal ni introduzcas un valor manual salvo que la aplicación lo solicite expresamente.

### Paso 6. Guardar y comprobar el registro

Guarda la localidad y vuelve a buscarla en la tabla. Confirma que el código interno aparece asociado a país, provincia y código postal correctos.

**Resultado esperado:** la nueva localidad puede seleccionarse desde la ficha del tercero.

### Paso 7. Asignar la localidad al tercero

1. Vuelve a la ficha del tercero.
2. Selecciona el código de localidad recién creado.
3. Comprueba los datos de localidad, provincia, país y código postal que muestra la ficha.
4. Guarda el tercero.

[![Ficha del tercero con el bloque de dirección y localidad señalado](/assets/simgest/migracion/mig_07_asignar_localidad_tercero.png =70%x)](/assets/simgest/migracion/mig_07_asignar_localidad_tercero.png)

*Asignación de la localidad creada a la dirección del tercero. Pulsa la imagen para abrirla a tamaño completo.*

## Resultado esperado

La localidad existe una sola vez en la tabla auxiliar, tiene país y provincia correctos y queda asociada al tercero correspondiente.

## Comprobación final

- [ ] Se ha comprobado que la localidad no existía.
- [ ] Código postal y nombre oficial son correctos.
- [ ] País y provincia están relacionados correctamente.
- [ ] SIMGEST ha generado o mostrado el código interno.
- [ ] El tercero muestra la localidad recién creada.
- [ ] No se ha creado un duplicado con otra denominación.

## Errores habituales

| Error | Riesgo | Actuación |
|---|---|---|
| Crear una localidad sin buscar variantes del nombre | Duplicar la tabla | Buscar por código postal y nombre antes del alta. |
| Asociar una provincia a otro país | Dirección incoherente | Corregir la relación antes de asignarla al tercero. |
| Introducir manualmente un código interno | Romper la secuencia de SIMGEST | Utilizar el código generado por el sistema. |
| No poder confirmar los datos geográficos | Crear un registro incorrecto | Pendiente de validación por Hacchi |

---

[← 3. Mapear localidades](/simgest/migracion/03-mapeo-localidades) · [Índice de migración](/simgest/migracion) · [5. Utilizar la localidad Desconocida →](/simgest/migracion/05-localidad-desconocida)
