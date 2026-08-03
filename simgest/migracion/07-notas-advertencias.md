---
title: "7. Notas y Advertencias Importantes"
description: "Migración Factusol a SIMGEST: 7. Notas y Advertencias Importantes"
published: true
tags: simgest, migracion, factusol
editor: markdown
---

## 7. Controles y advertencias de migración

Esta entrada reúne los controles transversales que deben aplicarse durante toda la migración. No sustituye a los procedimientos anteriores; funciona como una lista de seguridad para evitar decisiones inconsistentes entre distintos lotes o personas.

> **Objetivo**
>
> Mantener una fuente de datos identificada, aplicar criterios uniformes y evitar que las excepciones de migración se conviertan en errores permanentes dentro de SIMGEST.

## 1. Utilizar siempre la última versión de los datos

El material de origen indica que las entregas posteriores incorporaron cambios en cuentas bancarias, correos, teléfonos y nuevas fichas de clientes y proveedores.

Antes de ejecutar cualquier proceso debe registrarse:

- nombre del archivo;
- fecha de recepción;
- versión;
- empresa a la que corresponde;
- persona que confirma que es la entrega vigente.

No deben mezclarse tablas de versiones diferentes. Aunque dos archivos parezcan equivalentes, pueden contener cambios que no se distinguen a simple vista.

## 2. Diferenciar formato y contenido

Los archivos Excel y Access contienen, según el material de origen, los mismos datos organizados de forma distinta:

- Access distribuye la información en varias tablas relacionadas;
- Excel presenta la información integrada en una hoja.

Ambos formatos pueden utilizarse, pero el proceso debe comprobar que se están leyendo las mismas entidades y relaciones. Cambiar de formato no debe interpretarse como una nueva versión de los datos.

## 3. Mantener la trazabilidad de los códigos

El código de tercero es el único identificador completamente nuevo respecto a Factusol. SIMGEST lo genera internamente.

Esto no autoriza a modificar:

- código de cliente;
- código de proveedor;
- código de agente;
- cuenta contable;
- referencias históricas.

Siempre debe poder reconstruirse la relación:

Dato de Factusol
→ criterio aplicado
→ dato registrado en SIMGEST
→ estado de validación

## 4. No mezclar los roles de un tercero

Un mismo CIF puede aparecer como cliente y proveedor con datos distintos. Deben mantenerse separadas:

- notas;
- condiciones;
- códigos;
- cuentas;
- información propia de cada función.

La ficha general de tercero no debe utilizarse para borrar las diferencias entre roles.

## 5. Controlar especialmente las localidades

En España, la mayoría de las localidades deberían existir en SIMGEST. Una falta de coincidencia debe motivar una búsqueda más completa antes de crear un registro.

Para Mallorca, Galicia y Asturias se requiere especial atención porque pueden existir:

- barrios;
- distritos;
- parroquias;
- varias entidades con un mismo código postal;
- diferencias entre el nombre postal y el nombre administrativo.

Para localidades fuera de España puede ser necesario crear:

1. país;
2. provincia, región, condado, departamento o estado;
3. localidad;
4. código postal.

No debe crearse el nivel inferior antes de confirmar los superiores.

## 6. Utilizar valores provisionales de forma visible

Una forma de pago provisional o una localidad **Desconocida** debe aparecer en un registro de incidencias. El valor provisional no puede considerarse una solución final.

El registro mínimo debe incluir:

| Campo | Contenido |
|---|---|
| Registro afectado | Código, nombre y CIF |
| Dato de origen | Valor de Factusol |
| Valor provisional | Dato asignado en SIMGEST |
| Motivo | Razón de la provisionalidad |
| Acción pendiente | Corrección necesaria |
| Estado | Pendiente / En revisión / Resuelto |
| Comprobación | Fecha y evidencia de revisión |

## 7. No completar datos por intuición

Cuando una relación no pueda confirmarse mediante archivos, vídeo, captura o validación funcional, debe escribirse exactamente:

**Pendiente de validación por Hacchi**

Esta marca debe utilizarse en el punto concreto donde falta la información. No debe ocultarse en una nota general al final del manual.

## 8. Controlar el punto de corte

Después de la migración:

- no deben seguir modificándose en Factusol los datos ya migrados;
- las nuevas altas deben realizarse en SIMGEST;
- las correcciones deben registrarse en el sistema que se ha definido como fuente vigente;
- cualquier excepción debe comunicarse.

El proceso exacto de autorización y comunicación es **Pendiente de validación por Hacchi**.

## 9. Revisar antes de repetir el proceso

Antes de aplicar los mismos scripts a otra empresa, debe comprobarse que:

- no quedan errores críticos en la primera migración;
- los mapeos están actualizados;
- los problemas repetibles se han corregido en origen;
- las tablas auxiliares creadas son reutilizables;
- las incidencias provisionales están identificadas;
- existe aprobación para continuar.

## Checklist de cierre

- [ ] Se ha identificado la versión de origen.
- [ ] No se han mezclado entregas.
- [ ] Los códigos y cuentas conservan su trazabilidad.
- [ ] Los roles permanecen separados.
- [ ] Las localidades se han revisado con su jerarquía completa.
- [ ] Los valores provisionales están registrados.
- [ ] El punto de corte está comunicado.
- [ ] Las correcciones se han comprobado.
- [ ] La siguiente migración no comenzará sin aprobación.

## Regla de seguridad

Cuando exista duda sobre un código, una cuenta, una forma de pago, una localidad o la función de un tercero, el proceso debe detenerse para ese registro. La continuidad del resto del lote no justifica completar el dato sin evidencia.

---

[← 6. Revisar la migración](/simgest/migracion/06-revision-post-migracion) · [Índice de migración](/simgest/migracion) · [Operativa diaria →](/simgest/operativa)
