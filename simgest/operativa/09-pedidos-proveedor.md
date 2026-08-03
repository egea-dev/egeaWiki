---
title: "9. Generar pedidos a proveedor"
description: "Manual operativo SIMGEST: 9. Generar pedidos a proveedor"
published: true
tags: simgest, manual, operativa
editor: markdown
---

## 9. Generar pedidos a proveedor

La generación de pedidos a proveedor convierte las necesidades derivadas de los pedidos de cliente en documentos de compra. El material funcional distingue entre compras de tela y artículos de compraventa, y advierte que no deben mezclarse en el mismo procedimiento.

> **Objetivo**
>
> Revisar las necesidades de compra, asignar el proveedor correcto, verificar las cantidades agrupadas y generar únicamente los pedidos que corresponden al proyecto y tipo de compra seleccionado.

## Cuándo utilizar este procedimiento

Utilícelo cuando exista un pedido de cliente confirmado y el sistema muestre necesidades de material o artículos pendientes de comprar.

No debe generarse un pedido desde una oferta que todavía no se encuentra en el estado requerido. Para artículos de compraventa, la documentación indica que el presupuesto debe estar en estado **Pedido** y el artículo debe tener activada su condición de compraventa.

## Tipos de compra documentados

### Compra de materiales, como telas

Las líneas pueden agruparse por producto y proveedor. El usuario debe excluir artículos de compraventa que aparezcan mezclados y revisar las cantidades totales.

### Compraventa, como alfombras

El artículo se compra para el proyecto y puede requerir proveedor, medidas, acabado, color y precio calculado según tarifa.

No deben combinarse ambos tipos en un único pedido.

## Requisitos previos

- pedido de cliente confirmado;
- proyecto identificado;
- artículos y necesidades visibles;
- proveedor conocido o pendiente de asignar;
- cantidades revisables;
- tarifa validada;
- artículos de compraventa correctamente configurados;
- fechas o criterios de entrega disponibles.

## Vista general

Abrir generación de pedidos
→ aplicar filtros
→ revisar líneas y tipos de compra
→ excluir líneas incorrectas
→ asignar proveedores
→ comprobar agrupaciones y cantidades
→ seleccionar líneas
→ elegir modalidad de generación
→ validar mensajes
→ abrir el pedido creado

## Procedimiento A. Crear un pedido de compra de tela

### Paso 1. Acceder a la pantalla de generación

Abra la función de pedidos de compra o la pantalla de pedidos a proveedor según pedidos de cliente documentada en el entorno.

[![Pantalla de generación de pedidos a proveedor con filtros y necesidades señalados](/assets/simgest/operativa/cap_12_pedidos_proveedor.png =70%x)](/assets/simgest/operativa/cap_12_pedidos_proveedor.png)

*La captura muestra la cabecera de filtros y la tabla donde se revisan las necesidades.*

**Qué debe comprobar**

- empresa;
- serie;
- almacén;
- canal cuando aplique;
- proyecto;
- tipo de proveedor;
- opciones de búsqueda;
- fecha o estado de las líneas.

La documentación identifica una brecha: el filtro por proyecto no estaba disponible en una de las pantallas de compras y se encontraba en desarrollo. Si el entorno actual no dispone del filtro, no debe asumirse que las líneas pertenecen al mismo proyecto; deben revisarse individualmente.

### Paso 2. Resolver el aviso de recálculo cuando aparezca

Después de guardar o confirmar cambios relacionados con la oferta, SIMGEST puede mostrar la pregunta **¿Desea recalcular las necesidades de materia prima?**.

[![Mensaje de confirmación para recalcular las necesidades de materia prima con las acciones señaladas](/assets/simgest/operativa/cap_11_recalcular_materia_prima.png =70%x)](/assets/simgest/operativa/cap_11_recalcular_materia_prima.png)

*La captura muestra el aviso que puede modificar las necesidades que después se utilizan para preparar compras.*

**Qué debe comprender**

El recálculo puede actualizar las necesidades a partir de la configuración vigente del documento. No debe aceptarse por rutina si no se conoce qué cambios se han realizado y qué pedidos o necesidades existen ya.

**Antes de responder, compruebe:**

- qué oferta o pedido está abierto;
- qué artículo, cantidad, medida o variante se ha cambiado;
- si existen necesidades calculadas anteriormente;
- si ya se ha generado algún pedido a proveedor;
- si el recálculo puede duplicar o sustituir información.

La demostración visual señala la acción de aceptación, pero el criterio corporativo para aceptar o cancelar en cada escenario es **Pendiente de validación por Hacchi**.

### Paso 3. Revisar las líneas agrupadas

El sistema puede agrupar necesidades de un mismo producto. En el material se muestran ejemplos de telas agrupadas y una suma de cantidades procedentes de varias líneas.

**Qué debe hacer**

- identifique cada producto;
- revise descripción y variante;
- compruebe cantidad necesaria;
- compruebe cantidad ya pedida;
- revise fecha de entrega;
- confirme el proyecto de origen cuando sea visible.

**Por qué se hace**

Una cantidad agrupada puede ser correcta matemáticamente y contener líneas de otro proyecto o variante. La suma debe revisarse junto con el detalle que la compone.

### Paso 4. Excluir artículos de compraventa

La documentación muestra que una alfombra puede aparecer mezclada con las telas. Ese artículo no debe incluirse en un pedido de tela.

**Qué debe comprobar**

- tipo de artículo;
- indicador de compraventa;
- familia;
- proveedor;
- unidad;
- proceso de compra que le corresponde.

Desmarque o excluya las líneas de compraventa antes de continuar.

### Paso 5. Identificar líneas sin proveedor

Busque el mensaje **Línea sin proveedor asignada** o cualquier indicador equivalente visible.

**Qué debe hacer**

No genere el pedido mientras existan líneas sin proveedor. Abra el selector de la línea y asigne el proveedor que corresponda a la referencia.

La documentación utiliza **Industria Vitek** como ejemplo en una demostración. No debe utilizarse ese proveedor para otras referencias sin comprobar la ficha o la tarifa.

### Paso 6. Asignar proveedor individualmente

Seleccione el proveedor en la línea concreta.

**Qué debe comprobar**

- artículo;
- proveedor habitual;
- tarifa;
- unidad;
- variante;
- coherencia con la documentación oficial.

**Resultado esperado**

La línea deja de aparecer sin proveedor y puede formar parte del pedido correcto.

### Paso 7. Utilizar Marcar todo con control previo

[![Tabla con la acción Marcar todo y las líneas seleccionadas señaladas](/assets/simgest/operativa/cap_13_marcar_todo.png =70%x)](/assets/simgest/operativa/cap_13_marcar_todo.png)

*La captura muestra la selección masiva disponible en la tabla.*

La acción **Marcar todo** puede seleccionar todas las líneas visibles. Antes de usarla:

- revise los filtros;
- confirme que no hay artículos de compraventa;
- compruebe que todas las líneas pertenecen al alcance;
- asegúrese de que el proveedor es válido para todas.

No utilice una selección masiva para evitar revisar las líneas.

### Paso 8. Verificar las cantidades agrupadas

Compare las cantidades totales con las líneas que las originan.

**Qué debe comprobar**

- suma correcta;
- misma referencia;
- mismo color o variante;
- misma unidad;
- ausencia de cantidades ya pedidas;
- ausencia de líneas de otro proyecto.

### Paso 9. Elegir la modalidad de generación

El material documenta la acción **Realizar pedido de proveedor** con opciones como:

- Por totales;
- Por línea;
- Por unidades de producción.

La demostración selecciona **Por totales** para agrupar las cantidades. El criterio corporativo para elegir cada modalidad fuera del caso mostrado es **Pendiente de validación por Hacchi**.

### Paso 10. Revisar los mensajes de validación

Lea cualquier mensaje antes de confirmar. La documentación menciona un mensaje de validación relacionado con líneas de proveedor.

No pulse aceptar de forma automática. Compruebe que el mensaje confirma una condición válida y no advierte de un dato pendiente.

### Paso 11. Abrir y revisar el pedido generado

[![Pedido a proveedor generado con cabecera, líneas y totales señalados](/assets/simgest/operativa/cap_14_revision_final_pedido_prov.png =70%x)](/assets/simgest/operativa/cap_14_revision_final_pedido_prov.png)

*La captura muestra la revisión posterior del documento creado.*

Compruebe:

- proveedor;
- serie y fecha;
- líneas;
- artículos;
- cantidades;
- unidades;
- precios o tarifas cuando aparezcan;
- fecha prevista;
- ausencia de líneas ajenas.

## Procedimiento B. Crear un pedido de compraventa

### Paso 1. Confirmar el estado del documento de origen

La documentación indica que el presupuesto debe estar en estado **Pedido**, no **Oferta**, para que el artículo aparezca en compraventa.

**Qué debe comprobar**

- estado visible;
- proyecto;
- artículo con condición de compraventa;
- cantidades y medidas.

### Paso 2. Abrir la función de compraventa

Acceda al área de compras y abra la función de compraventa documentada.

### Paso 3. Seleccionar el artículo

Busque el artículo correcto y confirme que se trata de una referencia de compraventa.

### Paso 4. Asignar el proveedor

La documentación utiliza como ejemplos un proveedor de alfombras y Vitek para cuadrantes. La selección real debe basarse en la ficha y tarifa del artículo.

### Paso 5. Introducir medidas

Registre ancho, alto o metros cuadrados según los campos y la unidad del artículo.

**Control crítico**

No intercambie dimensiones ni introduzca metros cuadrados en un campo de medida lineal.

### Paso 6. Seleccionar acabado y color

El material documenta acabados como **Sin doblado**, **Doble y flex** y **Just**, además de una referencia de tejido o color.

Seleccione únicamente las opciones que correspondan al producto solicitado.

### Paso 7. Verificar el precio calculado

Compare el precio con la tarifa oficial y su estructura: precio base y posibles incrementos por acabado.

Cuando no se conozca un dato necesario, como ancho máximo o tamaño de rollo, no confirme el precio por estimación.

### Paso 8. Confirmar y revisar el pedido

Genere el pedido y aplique la misma revisión de cabecera, proveedor, artículo, medidas, acabado, color, precio y proyecto.

## Fechas de entrega y reclamaciones

La documentación indica que puede registrarse una fecha prevista de entrega y que los pedidos fuera de plazo aparecen en rojo en la pantalla de recepción. También documenta una acción manual para generar una reclamación.

El procedimiento completo de seguimiento se desarrolla junto con la recepción. La reclamación no se envía automáticamente; debe revisarse antes del envío.

## Resultado esperado

El pedido a proveedor contiene únicamente las líneas necesarias, asociadas al proveedor correcto, con cantidades y modalidad de generación revisadas. Los artículos de tela y compraventa se mantienen separados y el documento creado puede relacionarse con su pedido de cliente y proyecto.

## Comprobación final

- [ ] El documento de origen está en el estado requerido.
- [ ] Los filtros o la revisión manual limitan el alcance correcto.
- [ ] Tela y compraventa no están mezcladas.
- [ ] Todas las líneas tienen proveedor.
- [ ] Las cantidades agrupadas se han comprobado.
- [ ] Variantes y unidades coinciden.
- [ ] La modalidad de generación es la adecuada para el caso documentado.
- [ ] Los mensajes se han leído antes de confirmar.
- [ ] El pedido generado se ha abierto y revisado.
- [ ] No contiene líneas de otro proyecto.

## Errores habituales

| Error | Consecuencia | Actuación |
|---|---|---|
| Generar sin filtrar o revisar | Se mezclan proyectos | Detener y revisar todas las líneas. |
| Incluir compraventa en pedido de tela | Tipo de compra incorrecto | Separar procesos. |
| Asignar un proveedor por defecto | Compra a proveedor incorrecto | Comparar ficha y tarifa. |
| Usar Marcar todo sin control | Se seleccionan líneas no revisadas | Desmarcar y revisar individualmente. |
| No comprobar cantidades agrupadas | Se pide de más o de menos | Recalcular desde el detalle. |
| Elegir modalidad no validada | Agrupación incorrecta | Pendiente de validación por Hacchi. |

---

[← 8. Revisar tarifas](/simgest/operativa/08-tarifas-proveedor) · [Índice de operativa](/simgest/operativa) · [10. Registrar una recepción →](/simgest/operativa/10-recepcion-mercancia)
