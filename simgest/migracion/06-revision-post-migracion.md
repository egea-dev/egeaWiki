---
title: "6. Proceso de Revisión Post-Migración"
description: "Migración Factusol a SIMGEST: 6. Proceso de Revisión Post-Migración"
published: true
tags: simgest, migracion, factusol
editor: markdown
---

## 6. Revisar la migración

La revisión posterior confirma que los datos importados pueden utilizarse en SIMGEST y que las incidencias conocidas están controladas. El material de origen indica que la primera migración se realiza sobre la empresa de mayor volumen y que, si el resultado es válido, el mismo proceso se aplica posteriormente al resto de empresas.

> **Objetivo**
>
> Comprobar de forma estructurada la integridad de los datos migrados, corregir las incidencias prioritarias y autorizar únicamente después la continuación del proceso.

## Cuándo utilizar este procedimiento

Debe iniciarse cuando la persona responsable de ejecutar la migración comunica que el proceso ha terminado. También debe repetirse después de cada lote de correcciones y antes de utilizar los mismos scripts o criterios en otra empresa.

## Punto de corte entre sistemas

La notificación de finalización debe marcar el momento a partir del cual los datos migrados dejan de actualizarse en Factusol y pasan a mantenerse en SIMGEST.

**Por qué es importante**

Si un usuario modifica en Factusol un registro ya migrado, el cambio no aparecerá automáticamente en SIMGEST. Se crearían dos versiones distintas del mismo dato y no habría una fuente única de verdad.

La hora, fecha y forma exacta de comunicar el punto de corte son **Pendiente de validación por Hacchi**.

## Requisitos previos

- confirmación de que la migración ha finalizado;
- alcance del lote ejecutado;
- versión de los archivos utilizada;
- listado de registros importados;
- tabla de mapeos aplicada;
- relación de incidencias detectadas durante el proceso;
- acceso de consulta a las fichas migradas;
- criterio para aprobar o rechazar el lote.

## Vista general

Confirmar el alcance
→ registrar el punto de corte
→ revisar integridad general
→ analizar incidencias señaladas
→ comprobar muestras por tipo
→ corregir
→ repetir controles
→ decidir continuidad

## Procedimiento

### Fase 1. Confirmar el alcance migrado

El material de origen documenta una migración que cubre terceros, bancos, clientes, proveedores y acreedores mediante scripts preparados para insertar los datos en una secuencia determinada.

**Qué debe comprobar**

- empresa migrada;
- tablas incluidas;
- número aproximado de registros;
- versión de los archivos;
- mapeos utilizados;
- fecha de ejecución;
- incidencias generadas.

No comience la validación sin saber qué contenido debía haberse importado. Un registro ausente solo puede detectarse si forma parte del alcance esperado.

### Fase 2. Aplicar el punto de corte

Registre el momento desde el que los nuevos cambios deben hacerse en SIMGEST.

**Qué debe comunicar el aviso**

- que la migración ha terminado;
- qué datos están incluidos;
- desde qué momento Factusol deja de actualizarse para ese alcance;
- dónde deben registrarse las nuevas altas o cambios;
- qué incidencias siguen pendientes.

**Resultado esperado**

El equipo trabaja sobre una sola fuente de datos y no genera cambios paralelos.

### Fase 3. Realizar una revisión general

El material de origen señala que no se revisan individualmente los aproximadamente 1.500 registros. La revisión general debe combinar controles globales con muestras representativas.

**Controles globales recomendados a partir del material disponible**

- comparar el número de registros por tipo;
- comprobar que existen terceros, clientes, proveedores y acreedores;
- buscar fichas sin cuenta contable;
- localizar formas de pago provisionales;
- localizar localidades **Desconocida**;
- revisar registros sin país o provincia;
- revisar duplicados evidentes por CIF y rol;
- comprobar que los códigos originales se conservan.

El tamaño exacto de la muestra y los criterios estadísticos de validación son **Pendiente de validación por Hacchi**.

[![Listado de revisión posterior con registros migrados y zonas de control señaladas](/assets/simgest/migracion/mig_09_revision_post_migracion.png =70%x)](/assets/simgest/migracion/mig_09_revision_post_migracion.png)

*La captura representa la revisión general de los registros importados y la localización de incidencias.*

### Fase 4. Revisar las incidencias prioritarias

La revisión debe centrarse especialmente en los registros señalados durante la migración:

- localidades no identificadas;
- coincidencias dudosas por código postal;
- cuentas contables incorrectas;
- códigos modificados;
- formas de pago provisionales;
- terceros con varios roles;
- fichas con datos incompletos.

**Qué debe hacer**

Abra la ficha, compárela con el archivo de origen y documente la decisión. No corrija varios campos a la vez sin dejar constancia, porque después será difícil saber qué cambio resolvió la incidencia.

### Fase 5. Corregir y volver a comprobar

Cada corrección debe seguir este ciclo:

1. identificar el dato incorrecto;
2. localizar el valor de origen;
3. aplicar la corrección en SIMGEST;
4. guardar;
5. volver a abrir la ficha;
6. comprobar el resultado;
7. actualizar el estado de la incidencia.

**Qué no debe hacerse**

- cerrar la incidencia antes de revisar la ficha;
- cambiar códigos o cuentas para que “encajen” sin respaldo;
- corregir en Factusol después del punto de corte y asumir que llegará a SIMGEST;
- reutilizar una localidad dudosa en otros registros.

### Fase 6. Validar la siguiente migración

El material de origen indica que, si la migración inicial es correcta, se continúa con otras empresas utilizando el mismo proceso y scripts.

Antes de continuar debe comprobarse:

- que los errores detectados se han corregido en el criterio o en el script, no solo en las fichas finales;
- que los mapeos están actualizados;
- que las incidencias repetibles tienen una solución definida;
- que la siguiente empresa dispone de archivos actualizados;
- que la aprobación está documentada.

La autorización final para continuar con otras empresas es **Pendiente de validación por Hacchi**.

### Fase 7. Establecer la operativa futura

Una vez completada la migración, las nuevas altas y modificaciones deben realizarse directamente en SIMGEST. El material de origen indica que el equipo pasará a:

- dar de alta nuevos terceros;
- configurar sus fichas según el tipo;
- alimentar la base con nuevos registros.

Antes de iniciar esa operativa, los usuarios deben conocer los procedimientos de alta y los criterios de datos maestros. Los detalles no incluidos en los materiales actuales permanecen pendientes de validación.

## Resultado esperado

El lote migrado dispone de una revisión documentada, las incidencias prioritarias están resueltas o controladas y existe una decisión explícita sobre si puede utilizarse como base para la operativa y para migraciones posteriores.

## Comprobación final

- [ ] Se conoce el alcance exacto del lote.
- [ ] Se ha registrado la versión de los archivos.
- [ ] El punto de corte ha sido comunicado.
- [ ] Se han realizado controles globales.
- [ ] Se han revisado muestras por tipo de registro.
- [ ] Las incidencias prioritarias están documentadas.
- [ ] Cada corrección se ha comprobado después de guardar.
- [ ] Los errores repetibles se han corregido en el proceso.
- [ ] La continuidad con otras empresas tiene validación expresa.

## Errores habituales

| Error | Riesgo | Actuación |
|---|---|---|
| Revisar solo algunas fichas fáciles | Las incidencias críticas quedan ocultas | Incluir registros marcados y muestras por tipo. |
| Continuar editando Factusol | Aparecen versiones divergentes | Aplicar y comunicar el punto de corte. |
| Corregir la ficha pero no el criterio | El error se repite en la siguiente empresa | Actualizar mapeo o script. |
| Aprobar sin registrar pendientes | Se confunden incidencias con datos válidos | Mantener una lista de riesgos abierta. |
| Migrar otra empresa sin aprobación | Se replica un proceso no validado | Pendiente de validación por Hacchi. |

---

[← 5. Utilizar Desconocida](/simgest/migracion/05-localidad-desconocida) · [Índice de migración](/simgest/migracion) · [7. Controles y advertencias →](/simgest/migracion/07-notas-advertencias)
