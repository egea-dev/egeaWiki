---
title: "7. Notas y Advertencias Importantes"
description: "Migración Factusol a SIMGEST: 7. Notas y Advertencias Importantes"
published: true
tags:
  - simgest
  - migracion
  - factusol
editor: markdown
---

<!-- AÑADIR_CONTENIDO_ANTES_DEL_MODULO -->


| # | Nota |
| --- | --- |
| 1 | Los archivos Excel y Access contienen los mismos datos, solo cambia la estructura de presentación. El Access organiza la información en múltiples tablas relacionadas, mientras que el Excel la presenta integrada en una sola hoja. Ambos formatos son válidos para la migración. |
| 2 | Usar SIEMPRE la versión más reciente de los datos — desde la primera entrega ha habido cambios en cuentas bancarias, emails, teléfonos y nuevas fichas de clientes y proveedores. |
| 3 | En España, el 99% de las localidades ya existen en Simgest. Es muy raro encontrar una que no esté dada de alta. |
| 4 | En localidades como Mallorca, Galicia o Asturias, cuidado con múltiples entidades (barrios, parroquias, distritos) que comparten el mismo código postal. Verificar siempre que la localidad asignada corresponda a la dirección real. |
| 5 | Para localidades fuera de España, es probable que haya que crear país, provincia y localidad desde cero, ya que es menos probable que estén dados de alta en el sistema. |
| 6 | El código de tercero es el único dato completamente nuevo que no existía en Factusol. Es generado automáticamente por Simgest y su valor es irrelevante para la operativa del equipo. |
| 7 | Un mismo CIF puede tener datos diferentes como cliente y como proveedor — se gestionan en tablas separadas. Los datos de cada rol se mantienen independientes y no se mezclan. |

Documento generado a partir de la reunión "Data Migration & System Setup" del 23 de julio de 2026.

Segmento de referencia: minutos 12:00 a 34:00


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_MODULO -->

---

[← 6. Proceso de Revisión Post-Migración](/simgest/migracion/06-revision-post-migracion) · [Índice](/simgest) · [Inicio →](/simgest)
