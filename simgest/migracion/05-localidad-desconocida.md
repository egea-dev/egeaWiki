---
title: "5. Procedimiento de Fallback: Localidad \"Desconocida"
description: "Migración Factusol a SIMGEST: 5. Procedimiento de Fallback: Localidad \"Desconocida"
published: true
tags: simgest, migracion, factusol
editor: markdown
---

## 5. Utilizar la localidad Desconocida

La localidad **Desconocida** es una solución provisional que permite guardar un tercero cuando no se puede identificar o crear inmediatamente la localidad correcta. No representa la ubicación real y, por tanto, su uso debe quedar siempre acompañado de una incidencia pendiente de corrección.

> **Objetivo**
>
> Evitar que la migración se detenga por una localidad no resuelta, manteniendo al mismo tiempo la trazabilidad necesaria para sustituir posteriormente el valor provisional.

## Cuándo utilizar este procedimiento

Utilícelo únicamente cuando:

- no puede identificarse con seguridad la localidad correcta;
- la localidad no existe y no puede crearse en ese momento;
- falta información territorial necesaria;
- el registro debe incorporarse para continuar la migración.

No debe utilizarse para ahorrar tiempo cuando la localidad puede encontrarse o crearse. En España, el material de origen indica que es poco frecuente necesitar este recurso; su uso es más probable en ubicaciones internacionales.

## Riesgo que debe controlarse

El tercero queda técnicamente guardado, pero su dirección estructurada no es correcta. Si la incidencia no se registra, el valor provisional puede mantenerse indefinidamente y utilizarse en búsquedas, documentos o procesos posteriores como si fuera definitivo.

## Requisitos previos

- haber intentado resolver la localidad mediante el procedimiento de mapeo;
- comprobar que no existe una coincidencia válida;
- disponer del código postal y nombre original, aunque estén incompletos;
- localizar el registro comodín **Desconocida** correspondiente al país;
- disponer de un registro de incidencias.

La existencia de un código comodín para todos los países no está confirmada en las fuentes. Cuando no aparezca, será **Pendiente de validación por Hacchi**.

## Vista general

Confirmar que no puede resolverse
→ localizar Desconocida
→ asignar valor provisional
→ guardar el tercero
→ registrar la incidencia
→ crear o identificar la localidad correcta
→ sustituir el valor
→ cerrar la incidencia

## Procedimiento

### Paso 1. Confirmar que el caso requiere un valor provisional

Antes de utilizar **Desconocida**, documente qué comprobaciones se han realizado:

- búsqueda por código postal;
- búsqueda por nombre;
- revisión de país y provincia;
- comprobación de variantes;
- revisión de la dirección completa;
- imposibilidad temporal de crear el registro.

**Resultado esperado**

Existe una razón concreta y registrada para utilizar el valor provisional.

### Paso 2. Localizar la localidad comodín

Busque el registro **Desconocida** en la tabla de localidades.

[![Tabla de localidades con el registro Desconocida señalado](/assets/simgest/migracion/mig_08_localidad_desconocida.png =70%x)](/assets/simgest/migracion/mig_08_localidad_desconocida.png)

*La captura muestra el registro provisional que debe seleccionarse cuando la localidad real no puede resolverse.*

**Qué debe comprobar**

- nombre del registro;
- país asociado;
- código interno;
- ausencia de otra localidad correcta;
- que se está seleccionando el comodín adecuado para el caso.

### Paso 3. Asignar el valor provisional al tercero

Seleccione **Desconocida** en la ficha del tercero y guarde el registro.

**Qué ocurre**

Según el material de origen, el tercero queda almacenado y puede continuar dentro de la migración. Esto no convierte la dirección en correcta; solo evita que el proceso se detenga.

**Qué debe comprobar**

- el tercero se guarda;
- el valor provisional queda visible;
- el código postal y nombre originales se conservan en el registro de incidencia;
- no se marca el caso como resuelto.

### Paso 4. Registrar la incidencia

Anote, como mínimo:

- código y nombre del tercero;
- CIF;
- dirección de origen;
- código postal;
- localidad indicada en Factusol;
- país y provincia cuando se conozcan;
- valor provisional asignado;
- motivo por el que no pudo resolverse;
- estado pendiente.

**Por qué se hace**

La corrección posterior no debe depender de recordar qué fichas se modificaron. La lista de incidencias es la única forma de localizar todos los valores provisionales de manera controlada.

### Paso 5. Resolver la localidad correcta

Cuando se disponga de la información necesaria:

1. busque nuevamente la localidad;
2. créela si no existe y está confirmado;
3. abra la ficha del tercero;
4. sustituya **Desconocida** por el código correcto;
5. compruebe país, provincia y código postal;
6. guarde la ficha;
7. marque la incidencia como resuelta.

### Paso 6. Comprobar que no quedan incidencias invisibles

Al cerrar una fase de migración, revise el listado de terceros con localidad **Desconocida** y compárelo con el registro de incidencias.

**Resultado esperado**

Cada tercero con valor provisional aparece en la lista de control y puede corregirse sin revisar manualmente toda la base de datos.

## Resultado esperado

La migración puede continuar sin perder la información necesaria para corregir la localidad. El valor **Desconocida** permanece claramente identificado como provisional y no se confunde con una asignación definitiva.

## Comprobación final

- [ ] Se intentó resolver la localidad antes de usar el comodín.
- [ ] Se seleccionó el registro provisional adecuado.
- [ ] El tercero quedó guardado.
- [ ] La dirección original se conserva en la incidencia.
- [ ] El caso está marcado como pendiente.
- [ ] Existe un procedimiento para sustituir el valor.
- [ ] La incidencia se cerrará únicamente después de revisar la ficha.

## Errores habituales

| Error | Consecuencia | Actuación |
|---|---|---|
| Utilizar Desconocida sin buscar | Aumentan innecesariamente las incidencias | Resolver la localidad antes de continuar. |
| No registrar el tercero afectado | El provisional puede quedar indefinidamente | Añadirlo al control de incidencias. |
| Borrar la dirección original | Se pierde la información para corregir | Recuperar los datos de Factusol. |
| Marcar el caso como resuelto al guardar | La incidencia desaparece sin corregirse | Mantener estado pendiente hasta sustituir el valor. |

---

[← 4. Crear una localidad](/simgest/migracion/04-crear-localidad) · [Índice de migración](/simgest/migracion) · [6. Revisar la migración →](/simgest/migracion/06-revision-post-migracion)
