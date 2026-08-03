---
title: "6. Proceso de Revisión Post-Migración"
description: "Migración Factusol a SIMGEST: 6. Proceso de Revisión Post-Migración"
published: true
tags: simgest, migracion, factusol
editor: markdown
---

## 6. Revisar la migración

> **Objetivo**
>
> Comprobar que los terceros y sus datos principales se han trasladado correctamente antes de extender la migración o comenzar la operativa diaria.

## Cuándo utilizar este procedimiento

Se aplica cuando el responsable técnico comunica que la ejecución de la migración ha finalizado y señala el punto de corte a partir del cual los datos deben mantenerse en SIMGEST.

## Requisitos previos

- Confirmación de finalización de la ejecución técnica.
- Relación de registros señalados como problemáticos.
- Inventarios de cuentas, formas de pago y localidades.
- Acceso de consulta a los terceros migrados.
- Criterio de cierre del periodo de trabajo en Factusol.

## Vista general

Recibir notificación
→ revisar muestra general
→ revisar incidencias señaladas
→ corregir errores
→ validar el resultado
→ autorizar la siguiente fase

## Procedimiento

### Fase 1. Confirmar el alcance migrado

La fuente indica que la migración incluye terceros, clientes, proveedores y acreedores, con una secuencia técnica que incorpora primero la información común y después los roles específicos.

**Qué debe comprobar:** solicita o revisa la relación de entidades incluidas en la ejecución y el momento exacto del corte.

### Fase 2. Aplicar el punto de corte

Cuando Pedro comunique que la migración está completa, el equipo debe identificar qué datos ya forman parte de SIMGEST.

**Regla documentada:** no modificar en Factusol los datos ya incluidos en la migración después del punto de corte comunicado.

**Procedimiento para cambios urgentes durante el corte:** Pendiente de validación por Hacchi

### Fase 3. Realizar una revisión general

La fuente no plantea revisar manualmente todos los registros uno por uno. Se realiza una revisión general y se presta atención específica a los registros señalados.

[![Listado general de terceros migrados con el área de registros señalada](/assets/simgest/migracion/mig_09_revision_post_migracion.png =70%x)](/assets/simgest/migracion/mig_09_revision_post_migracion.png)

*Vista utilizada para revisar el resultado general de la migración. Pulsa la imagen para abrirla a tamaño completo.*

Comprueba una muestra que incluya:

- códigos de terceros;
- cliente o proveedor asociado;
- NIF o CIF;
- razón social;
- cuenta contable;
- forma de pago;
- dirección y localidad;
- notas propias de cada rol.

### Fase 4. Revisar las incidencias prioritarias

Da prioridad a:

- localidades no identificadas;
- localidades asignadas por coincidencia parcial;
- valores Desconocida;
- cuentas que no coincidan con Factusol;
- formas de pago provisionales;
- terceros con el mismo CIF y varios roles.

### Fase 5. Corregir y volver a comprobar

Después de corregir un dato, vuelve a abrir el registro y compara el resultado con la fuente de origen. No cierres una incidencia únicamente porque se haya guardado un cambio.

### Fase 6. Validar la siguiente migración

La fuente plantea utilizar la primera empresa migrada como validación antes de aplicar el mismo proceso al resto.

**Responsable que autoriza el paso a la siguiente empresa:** Pendiente de validación por Hacchi

## Resultado esperado

Los registros revisados mantienen sus códigos y datos esenciales, las incidencias conocidas están corregidas o documentadas y existe una decisión explícita sobre la continuación del proceso.

## Comprobación final

- [ ] Se conoce el alcance y el punto de corte.
- [ ] Se ha realizado una revisión general.
- [ ] Los registros señalados se han comprobado individualmente.
- [ ] Las correcciones se han validado después de guardar.
- [ ] Los valores provisionales siguen registrados si no están resueltos.
- [ ] Existe autorización para continuar con la siguiente fase.

## Errores habituales

| Error | Riesgo | Actuación |
|---|---|---|
| Seguir modificando Factusol tras el corte | Divergencia entre sistemas | Detener el cambio y comunicar la incidencia. |
| Revisar solo registros aleatorios | Omitir los casos ya señalados | Empezar por la lista de incidencias. |
| Cerrar una incidencia sin comprobar el resultado | Mantener datos incorrectos | Reabrir la ficha y comparar con el origen. |

---

[← 5. Utilizar la localidad Desconocida](/simgest/migracion/05-localidad-desconocida) · [Índice de migración](/simgest/migracion) · [7. Controles y advertencias →](/simgest/migracion/07-notas-advertencias)
