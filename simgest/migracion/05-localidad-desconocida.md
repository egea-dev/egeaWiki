---
title: "5. Procedimiento de Fallback: Localidad \"Desconocida"
description: "Migración Factusol a SIMGEST: 5. Procedimiento de Fallback: Localidad \"Desconocida"
published: true
tags: simgest, migracion, factusol
editor: markdown
---

## 5. Utilizar la localidad Desconocida

> **Objetivo**
>
> Permitir el registro temporal de un tercero cuando la localidad correcta no puede identificarse o crearse durante la migración, manteniendo una incidencia pendiente de resolución.

## Cuándo utilizar este procedimiento

Úsalo únicamente como solución provisional cuando no sea posible confirmar la localidad correcta en ese momento.

No debe utilizarse para evitar una búsqueda que sí puede resolverse con los datos disponibles.

## Requisitos previos

- Confirmación de que la localidad correcta no puede asignarse en ese momento.
- Código postal y nombre esperado, aunque estén incompletos.
- Registro de incidencias donde anotar el tercero afectado.
- Existencia de una localidad comodín adecuada en SIMGEST.

## Vista general

Buscar el valor comodín
→ asignarlo al tercero
→ registrar la incidencia
→ crear o localizar la localidad correcta
→ sustituir el valor provisional

## Procedimiento

### Paso 1. Buscar la localidad comodín

En el selector de localidades, busca el registro **Desconocida** o el valor equivalente documentado para el país correspondiente.

[![Selector de localidades con el valor Desconocida señalado](/assets/simgest/migracion/mig_08_localidad_desconocida.png =70%x)](/assets/simgest/migracion/mig_08_localidad_desconocida.png)

*Ejemplo de selección de la localidad provisional Desconocida. Pulsa la imagen para abrirla a tamaño completo.*

**Código exacto del valor comodín para cada país:** Pendiente de validación por Hacchi

### Paso 2. Asignar el valor provisional

Selecciona la localidad Desconocida en la ficha del tercero y comprueba que el sistema permite continuar con el registro.

**Qué debe comprobar:** la dirección escrita en la ficha no debe interpretarse como validada por el hecho de haber utilizado el valor comodín.

### Paso 3. Registrar la incidencia

Anota como mínimo:

- código del tercero;
- nombre o razón social;
- país;
- código postal;
- localidad indicada en Factusol;
- motivo por el que no pudo resolverse;
- fecha o fase de la migración;
- estado pendiente.

### Paso 4. Corregir el tercero posteriormente

Cuando la localidad correcta exista:

1. abre la ficha del tercero;
2. sustituye Desconocida por la localidad correcta;
3. comprueba país, provincia y código postal;
4. guarda el cambio;
5. marca la incidencia como resuelta.

## Resultado esperado

El tercero puede quedar registrado temporalmente, pero permanece identificado en una lista de incidencias hasta que se sustituya la localidad provisional.

## Comprobación final

- [ ] El valor Desconocida se ha utilizado solo por necesidad.
- [ ] El tercero está identificado en el control de incidencias.
- [ ] Se conserva el código postal y el nombre de localidad de origen.
- [ ] Existe una acción pendiente para corregir la ficha.
- [ ] La incidencia no se ha cerrado antes de sustituir el valor.

## Errores habituales

| Error | Riesgo | Actuación |
|---|---|---|
| Utilizar Desconocida como valor definitivo | Dirección incompleta de forma permanente | Mantener la incidencia abierta. |
| No registrar el tercero afectado | Imposibilidad de corregirlo en bloque | Añadirlo al control antes de continuar. |
| Seleccionar un comodín de otro país | País y provincia incorrectos | Revisar la tabla y solicitar validación. |

---

[← 4. Crear una localidad](/simgest/migracion/04-crear-localidad) · [Índice de migración](/simgest/migracion) · [6. Revisar la migración →](/simgest/migracion/06-revision-post-migracion)
