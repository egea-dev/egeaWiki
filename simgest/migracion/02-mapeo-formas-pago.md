---
title: "2. Mapeo de Formas de Pago"
description: "Migración Factusol a SIMGEST: 2. Mapeo de Formas de Pago"
published: true
tags: simgest, migracion, factusol
editor: markdown
---

## 2. Mapear formas de pago

> **Objetivo**
>
> Convertir cada código de forma de pago de Factusol en el código equivalente de SIMGEST y dejar identificadas las asignaciones provisionales.

## Cuándo utilizar este procedimiento

Utilízalo después de preparar los códigos y cuentas, y antes de validar las fichas migradas. Factusol y SIMGEST utilizan codificaciones diferentes; por tanto, no debe suponerse que un mismo número representa la misma condición en ambos sistemas.

## Requisitos previos

- Lista de códigos y descripciones de formas de pago utilizadas en Factusol.
- Tabla actual de formas de pago disponible en SIMGEST.
- Documento de correspondencias donde registrar el resultado.
- Criterio autorizado para crear una nueva forma de pago o utilizar un valor provisional.

## Vista general

Extraer códigos de Factusol
→ consultar códigos de SIMGEST
→ buscar equivalencias
→ resolver los casos sin coincidencia
→ registrar trazabilidad

## Procedimiento

### Paso 1. Inventariar las formas de pago de Factusol

**Qué debe hacer:** lista todos los códigos utilizados y escribe junto a cada uno su descripción.

**Qué debe comprobar:** no deben quedar códigos sin descripción ni formas de pago presentes en los terceros que no aparezcan en el inventario.

**Resultado esperado:** existe una lista única de códigos de origen preparada para comparar.

### Paso 2. Consultar las formas de pago de SIMGEST

**Qué debe hacer:** revisa la tabla auxiliar o el selector de formas de pago disponible en SIMGEST.

**Ruta exacta de acceso a la tabla auxiliar:** Pendiente de validación por Hacchi

**Qué debe comprobar:** anota el código de SIMGEST y el significado real de cada opción; no utilices únicamente el texto visible en una ficha ya migrada como referencia general.

[![Ficha de tercero con el bloque de forma de pago y las notas del cliente señalados](/assets/simgest/migracion/mig_03_forma_pago.png =70%x)](/assets/simgest/migracion/mig_03_forma_pago.png)

*Ejemplo de la ubicación de la forma de pago dentro de una ficha migrada. Pulsa la imagen para abrirla a tamaño completo.*

### Paso 3. Crear la tabla de correspondencias

Para cada código de Factusol:

1. Busca la condición equivalente en SIMGEST.
2. Registra el código de destino.
3. Marca la asignación como **definitiva** cuando la equivalencia esté confirmada.
4. Pasa al procedimiento de excepción cuando no exista coincidencia directa.

La trazabilidad mínima debe contener:

| Código Factusol | Descripción de origen | Código SIMGEST | Descripción de destino | Estado |
|---|---|---|---|---|
| Pendiente | Pendiente | Pendiente | Pendiente | Definitivo o provisional |

### Paso 4. Resolver códigos sin equivalencia

La fuente documenta dos posibilidades:

- crear una nueva forma de pago en la tabla de SIMGEST;
- asignar temporalmente **Contado** como valor provisional.

**Criterio para elegir entre ambas opciones:** Pendiente de validación por Hacchi

Cuando se utilice un valor provisional:

1. registra el código de origen;
2. identifica el tercero afectado;
3. anota el valor provisional utilizado;
4. incluye el registro en la revisión posterior;
5. no lo marques como definitivo hasta confirmar la condición correcta.

## Resultado esperado

Cada forma de pago de Factusol tiene una correspondencia documentada en SIMGEST o figura expresamente como provisional y pendiente de corrección.

## Comprobación final

- [ ] Todos los códigos de Factusol están inventariados.
- [ ] Cada código tiene descripción de origen y de destino.
- [ ] Las coincidencias se han validado por significado, no solo por número.
- [ ] Los valores provisionales están identificados.
- [ ] Los terceros afectados están incluidos en la revisión posterior.

## Errores habituales

| Error | Riesgo | Actuación |
|---|---|---|
| Copiar el mismo número de código entre sistemas | Asignar una condición distinta | Comparar las descripciones antes de migrar. |
| Usar Contado sin registrarlo como provisional | Perder la condición real del tercero | Añadirlo al control de incidencias. |
| Crear una forma de pago sin criterio confirmado | Duplicar o alterar la tabla auxiliar | Pendiente de validación por Hacchi |

---

[← 1. Conservar cuentas contables y códigos](/simgest/migracion/01-cuentas-contables) · [Índice de migración](/simgest/migracion) · [3. Mapear localidades →](/simgest/migracion/03-mapeo-localidades)
