---
title: Migración desde Factusol
description: Página de entrada para la documentación de migración de datos hacia SIMGEST.
published: true
tags: simgest, migracion, factusol
editor: markdown
---

## Migración de Factusol a SIMGEST

Esta sección reúne los procedimientos necesarios para trasladar los datos maestros de Factusol a SIMGEST sin perder la correspondencia entre códigos, cuentas contables, formas de pago, localidades y funciones de cada tercero.

La migración no consiste únicamente en importar registros. Antes de considerar un dato válido en SIMGEST es necesario comprobar que conserva su significado operativo, que puede utilizarse dentro de la estructura del nuevo sistema y que las incidencias detectadas quedan identificadas para su corrección.

> **Objetivo de la sección**
>
> Establecer un proceso de migración controlado, trazable y revisable que permita comenzar la operativa en SIMGEST con datos coherentes y con las excepciones claramente registradas.

## Alcance confirmado

El material de origen documenta la migración de:

- terceros;
- clientes;
- proveedores;
- acreedores;
- cuentas bancarias asociadas;
- cuentas contables y códigos comerciales;
- formas de pago;
- localidades y su estructura territorial.

No se describen en esta sección procesos de venta, compra, producción o recepción. Esos procedimientos pertenecen a la [operativa diaria](/simgest/operativa).

## Principios de trabajo

La migración debe respetar cuatro principios:

1. **Conservar el dato original cuando exista correspondencia directa.** Los códigos y cuentas contables procedentes de Factusol no deben renumerarse por comodidad.
2. **Transformar solo lo que SIMGEST exige de forma diferente.** Las formas de pago y las localidades requieren una tabla de correspondencias porque ambos sistemas utilizan codificaciones distintas.
3. **Separar los distintos roles de un mismo tercero.** Un mismo CIF puede actuar como cliente y proveedor y conservar información distinta en cada función.
4. **Registrar las excepciones.** Los valores provisionales, las localidades desconocidas y las correspondencias dudosas deben quedar anotados para revisión posterior.

## Secuencia recomendada

La secuencia documentada es la siguiente:

1. Preparar la última versión de los archivos de origen.
2. Inventariar códigos comerciales y cuentas contables.
3. Crear el mapeo de formas de pago.
4. Preparar y resolver el mapeo de localidades.
5. Crear las localidades que no existan en SIMGEST.
6. Utilizar la localidad **Desconocida** únicamente como solución provisional.
7. Ejecutar la migración.
8. Marcar el punto de corte a partir del cual Factusol deja de ser la fuente de actualización.
9. Revisar los datos migrados y corregir las incidencias.
10. Validar el resultado antes de migrar el resto de empresas.

## Procedimientos

1. [Conservar cuentas contables y códigos](/simgest/migracion/01-cuentas-contables)
2. [Mapear formas de pago](/simgest/migracion/02-mapeo-formas-pago)
3. [Mapear localidades](/simgest/migracion/03-mapeo-localidades)
4. [Crear una localidad](/simgest/migracion/04-crear-localidad)
5. [Utilizar la localidad Desconocida](/simgest/migracion/05-localidad-desconocida)
6. [Revisar la migración](/simgest/migracion/06-revision-post-migracion)
7. [Controles y advertencias de migración](/simgest/migracion/07-notas-advertencias)

## Criterio de finalización

La migración puede considerarse preparada para validación cuando:

- se ha utilizado la última entrega de datos;
- los códigos y cuentas de origen tienen una correspondencia comprobable;
- todas las formas de pago tienen un destino definitivo o provisional documentado;
- las localidades están resueltas, creadas o marcadas como incidencia;
- los roles de cliente, proveedor, acreedor y agente permanecen separados;
- se ha definido el punto de corte entre Factusol y SIMGEST;
- el equipo conoce qué registros requieren revisión humana.

La aprobación definitiva de una migración y el momento exacto para continuar con el resto de empresas son **Pendiente de validación por Hacchi**.

---

[← Manual SIMGEST](/simgest) · [1. Conservar cuentas y códigos →](/simgest/migracion/01-cuentas-contables)
