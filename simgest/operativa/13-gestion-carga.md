---
title: "13. Revisar gestión de carga y bultos"
description: "Manual operativo SIMGEST: 13. Revisar gestión de carga y bultos"
published: true
tags: simgest, manual, operativa
editor: markdown
---

## 13. Revisar la gestión de carga

La gestión de carga reúne información necesaria para preparar expediciones o entregas. En la pantalla documentada aparecen datos de cliente o documento, unidades, bultos, peso, palés, importes y líneas inferiores. La revisión debe asegurar que la carga representa lo que realmente está preparado.

> **Objetivo**
>
> Comprobar la cabecera y el detalle de una carga antes de considerarla preparada, evitando cerrar o continuar cuando faltan líneas, cantidades, bultos o datos logísticos.

## Cuándo utilizar este procedimiento

Utilícelo al preparar una expedición, revisar una carga existente o comprobar qué documentos y líneas se han incluido.

No debe cerrarse una carga únicamente porque exista un registro en pantalla. La mercancía y los datos logísticos deben estar verificados.

## Requisitos previos

- cliente o destino identificado;
- documento o referencia;
- líneas preparadas;
- unidades comprobadas;
- información de bultos, peso o palés cuando corresponda;
- estado de producción o embalaje confirmado cuando sea necesario;
- criterio de cierre validado.

El criterio exacto para cerrar una carga y los perfiles autorizados son **Pendiente de validación por Hacchi**.

## Vista general

Localizar la carga
→ confirmar cabecera
→ revisar documentos asociados
→ comprobar líneas
→ comparar cantidades físicas
→ revisar bultos y peso
→ detectar faltas
→ continuar o detener

## Procedimiento

### Paso 1. Abrir la carga correcta

Acceda a **Gestión de Carga** y localice el registro por cliente, documento, referencia o fecha.

[![Pantalla de gestión de carga con cabecera, datos logísticos y líneas inferiores señalados](/assets/simgest/operativa/cap_24_gestion_carga.png =70%x)](/assets/simgest/operativa/cap_24_gestion_carga.png)

*La captura muestra las zonas que deben revisarse antes de considerar la carga preparada.*

### Paso 2. Confirmar la cabecera

Revise:

- cliente;
- destino cuando aparezca;
- documento o referencia;
- fecha;
- proyecto;
- estado;
- otros datos visibles de identificación.

No continúe si la referencia no permite relacionar la carga con el pedido o entrega correctos.

### Paso 3. Revisar los documentos asociados

Compruebe qué pedidos, albaranes o líneas forman parte de la carga.

**Qué debe verificar**

- todos pertenecen al cliente;
- corresponden al proyecto o entrega;
- no aparecen documentos duplicados;
- no falta un documento esperado;
- el estado permite preparar la carga.

La relación exacta entre carga, albarán de venta y entrega no está completamente desarrollada en las fuentes. Cuando no pueda confirmarse: **Pendiente de validación por Hacchi**.

### Paso 4. Revisar las líneas inferiores

Para cada línea, compruebe:

- artículo;
- descripción;
- cantidad;
- unidades preparadas;
- bultos;
- peso;
- palés;
- importe cuando aparezca;
- observaciones o estado.

No dé por correcta una carga porque el total general parezca razonable. Revise línea por línea.

### Paso 5. Comparar con la mercancía preparada

La información de pantalla debe coincidir con la preparación física.

**Qué debe hacer**

- contar bultos;
- revisar etiquetas;
- comparar unidades;
- comprobar peso si forma parte del proceso;
- confirmar palés;
- identificar líneas parciales o pendientes.

### Paso 6. Detectar faltas o inconsistencias

Detenga el proceso cuando:

- falta una línea;
- la cantidad física no coincide;
- hay bultos sin identificar;
- el peso es incoherente;
- aparecen artículos de otro documento;
- no se conoce el estado de preparación;
- la carga contiene una entrega parcial no validada.

### Paso 7. Documentar la incidencia

Registre:

- carga;
- línea afectada;
- cantidad esperada;
- cantidad preparada;
- diferencia;
- acción pendiente;
- validación necesaria.

### Paso 8. Continuar únicamente después de la revisión

La acción final de cierre, expedición o generación de documentos no está confirmada en el material actual. Antes de ejecutarla: **Pendiente de validación por Hacchi**.

## Resultado esperado

La carga representa los documentos y artículos correctos, las cantidades físicas coinciden y cualquier falta está registrada antes de continuar con la entrega.

## Comprobación final

- [ ] Cliente, documento, referencia y proyecto correctos.
- [ ] Documentos asociados revisados.
- [ ] Todas las líneas pertenecen a la carga.
- [ ] Cantidades físicas comparadas.
- [ ] Bultos, peso y palés revisados cuando proceda.
- [ ] No hay líneas duplicadas ni ajenas.
- [ ] Las entregas parciales tienen validación.
- [ ] Las incidencias están registradas.
- [ ] No se ha cerrado sin criterio confirmado.

## Errores habituales

| Error | Consecuencia | Actuación |
|---|---|---|
| Seleccionar una carga parecida | Se prepara otro documento | Confirmar cliente y referencia. |
| Revisar solo el total | Se omiten faltas de líneas | Comprobar detalle. |
| No comparar con mercancía física | La pantalla no refleja la preparación real | Contar y verificar. |
| Cerrar con bultos pendientes | Entrega incompleta | Detener y registrar. |
| Ejecutar el cierre sin procedimiento validado | Documento o estado incorrecto | Pendiente de validación por Hacchi. |

---

[← 12. Configurar columnas](/simgest/operativa/12-columnas-visibles) · [Índice de operativa](/simgest/operativa) · [14. Listas de comprobación →](/simgest/operativa/14-checklists)
