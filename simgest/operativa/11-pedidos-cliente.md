---
title: "11. Consultar pedidos de cliente"
description: "Manual operativo SIMGEST: 11. Consultar pedidos de cliente"
published: true
tags: simgest, manual, operativa
editor: markdown
---

## 11. Consultar pedidos de cliente

El pedido de cliente es el documento que resulta de una oferta confirmada. Conserva la información comercial necesaria para continuar con compras, producción, preparación y entrega. La consulta debe permitir comprobar qué se ha pedido, de qué oferta procede y qué líneas forman parte del proyecto.

> **Objetivo**
>
> Localizar el pedido correcto, revisar su cabecera y sus líneas y mantener la trazabilidad con la oferta o presupuesto que lo originó.

## Cuándo utilizar este procedimiento

Utilícelo para:

- comprobar que una oferta confirmada ha generado el pedido esperado;
- revisar artículos, cantidades, precios o fechas;
- investigar una necesidad de compra;
- comparar el pedido con el presupuesto;
- verificar la vinculación con el proyecto;
- preparar una consulta relacionada con entrega o producción.

No debe modificarse un pedido únicamente para que coincida con una oferta antigua sin comprobar cuál es la versión aprobada.

## Relación con la oferta

La documentación funcional indica que al confirmar una oferta el sistema genera un pedido de cliente vinculado al mismo proyecto y conserva productos, cantidades y precios.

La relación esperada es:

Oferta confirmada
→ pedido de cliente
→ compras o aprovisionamiento
→ producción
→ entrega

Una diferencia entre oferta y pedido debe investigarse antes de continuar, porque puede trasladarse a necesidades de material o documentos posteriores.

## Requisitos previos

- cliente, proyecto o referencia conocidos;
- oferta de origen disponible cuando sea necesario;
- número o fecha aproximada del pedido;
- acceso a Ventas o Pedidos;
- criterios para distinguir varias versiones del mismo proyecto.

## Vista general

Abrir Pedidos
→ aplicar búsqueda o filtro
→ identificar cabecera
→ seleccionar pedido
→ revisar líneas
→ comparar con oferta
→ registrar diferencias
→ comprobar proyecto y estado

## Procedimiento

### Paso 1. Abrir la consulta de pedidos

Acceda al módulo de pedidos de cliente. La documentación indica la ruta funcional **Ventas → Pedidos**.

[![Pantalla de pedidos de cliente con cabecera y líneas inferiores señaladas](/assets/simgest/operativa/cap_16_pedido_cliente.png =70%x)](/assets/simgest/operativa/cap_16_pedido_cliente.png)

*La captura muestra la tabla de pedidos y el detalle asociado al registro seleccionado.*

### Paso 2. Buscar por criterios identificables

Utilice los filtros o campos disponibles para reducir el listado.

**Criterios documentados:**

- cliente;
- referencia;
- proyecto;
- fecha.

Cuando existan varias ofertas o pedidos del mismo proyecto, no seleccione únicamente por cliente. Compare también referencia, fecha, número y estado.

### Paso 3. Confirmar la cabecera del pedido

Antes de revisar las líneas, compruebe:

- número del pedido;
- cliente;
- referencia;
- proyecto;
- fecha;
- estado;
- oferta de origen cuando aparezca;
- dirección o datos adicionales visibles.

**Por qué se hace**

La tabla inferior cambia según el pedido seleccionado. Una revisión realizada sobre otra cabecera puede llevar a conclusiones incorrectas sobre artículos o cantidades.

### Paso 4. Revisar las líneas inferiores

Para cada línea compruebe:

- artículo;
- descripción;
- cantidad;
- unidad;
- precio;
- IVA;
- fechas;
- estado o información adicional visible;
- relación con el proyecto.

No se limite a comprobar que existe el mismo número de líneas. Una línea puede haber cambiado de artículo, cantidad o variante.

### Paso 5. Comparar con la oferta de origen

Abra la oferta o el PDF aprobado y compare:

| Elemento | Oferta / PDF | Pedido | Resultado |
|---|---|---|---|
| Cliente | Valor aprobado | Valor del pedido | Coincide / No coincide |
| Referencia | Texto aprobado | Texto del pedido | Coincide / No coincide |
| Proyecto | Proyecto original | Proyecto del pedido | Coincide / No coincide |
| Artículo | Línea de oferta | Línea de pedido | Coincide / No coincide |
| Cantidad | Cantidad aprobada | Cantidad pedida | Coincide / No coincide |
| Precio | Precio aprobado | Precio del pedido | Coincide / No coincide |
| IVA | Tipo aplicado | Tipo del pedido | Coincide / No coincide |

**Qué debe hacer ante una diferencia**

Determine primero si:

- se confirmó otra versión de la oferta;
- hubo una modificación posterior autorizada;
- la línea se transformó por configuración;
- existe un error de conversión;
- está consultando otro pedido.

No corrija la diferencia hasta conocer su origen.

### Paso 6. Comprobar la vinculación con el proyecto

La documentación indica que los pedidos generados desde ofertas del proyecto quedan vinculados al mismo.

**Qué debe comprobar**

- proyecto visible en la cabecera;
- coherencia con la oferta;
- líneas pertenecientes al trabajo;
- ausencia de artículos de otra oferta o proyecto.

### Paso 7. Revisar entregas parciales con precaución

La documentación funcional menciona que el sistema soporta entregas parciales basadas en fases de producción completadas y que solo los productos que hayan completado embalaje pueden entregarse.

El procedimiento completo de entrega parcial no está desarrollado visualmente en este paquete. Antes de utilizar esa función: **Pendiente de validación por Hacchi**.

### Paso 8. Registrar una incidencia cuando no coincida

Anote:

- pedido afectado;
- oferta o PDF utilizado como referencia;
- línea o campo diferente;
- valor esperado;
- valor encontrado;
- estado del documento;
- acción pendiente.

## Resultado esperado

El pedido consultado puede relacionarse con la oferta correcta y el proyecto. Sus líneas, cantidades y precios están revisados y las diferencias están explicadas o registradas antes de continuar con compras, producción o entrega.

## Comprobación final

- [ ] Se ha localizado el pedido correcto.
- [ ] Cliente, referencia, proyecto, fecha y estado se han revisado.
- [ ] Todas las líneas se han comprobado.
- [ ] Artículos, cantidades, precios e IVA coinciden con el origen.
- [ ] Se ha comparado con la versión aprobada de la oferta.
- [ ] No existen líneas de otro proyecto.
- [ ] Las diferencias están documentadas.
- [ ] No se ha iniciado una entrega parcial sin procedimiento validado.

## Errores habituales

| Error | Consecuencia | Actuación |
|---|---|---|
| Buscar solo por cliente | Se selecciona otro pedido | Comparar referencia, fecha y proyecto. |
| Revisar líneas sin confirmar cabecera | Se analiza otro documento | Validar cabecera primero. |
| Comparar con un PDF antiguo | Se detectan diferencias falsas | Utilizar la versión aprobada. |
| Corregir sin conocer el origen | Se altera un pedido válido | Investigar la conversión o versión. |
| Ejecutar entrega parcial sin criterio confirmado | Se entrega un producto no preparado | Pendiente de validación por Hacchi. |

---

[← 10. Registrar una recepción](/simgest/operativa/10-recepcion-mercancia) · [Índice de operativa](/simgest/operativa) · [12. Configurar columnas →](/simgest/operativa/12-columnas-visibles)
