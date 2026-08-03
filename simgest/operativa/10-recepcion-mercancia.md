---
title: "10. Recibir mercancía de proveedor"
description: "Manual operativo SIMGEST: 10. Recibir mercancía de proveedor"
published: true
tags: simgest, manual, operativa
editor: markdown
---

## 10. Registrar una recepción de proveedor

La recepción registra la mercancía que ha llegado físicamente y genera un albarán interno. Según la documentación funcional, también puede actualizar stock, asignar materiales a pedidos y modificar indicadores relacionados con la disponibilidad. Por este motivo, la cantidad introducida debe proceder de una comprobación física y no de la cantidad inicialmente pedida.

> **Objetivo**
>
> Registrar correctamente una recepción completa, parcial o superior, mantener pendientes las cantidades no recibidas y comprobar todos los efectos del albarán generado.

## Cuándo utilizar este procedimiento

Utilícelo cuando llegue mercancía asociada a un pedido de proveedor.

No registre una recepción porque haya llegado la fecha prevista ni porque el pedido aparezca pendiente. Debe existir mercancía física que pueda contarse, medirse o identificarse.

## Efectos documentados de la recepción

Al confirmar la recepción, el material funcional indica que el sistema puede:

- generar el albarán interno;
- actualizar el stock;
- crear fichas de stock con el metraje recibido;
- asignar materiales a los pedidos que los requieren;
- desmarcar el indicador **Falta tela** en el pedido de cliente;
- mostrar los materiales como asignados en el PMP;
- retirar el pedido servido de la lista de pendientes.

Estos efectos convierten la recepción en una acción crítica. Un error puede duplicar stock, cerrar un pedido con unidades pendientes o asignar material incorrecto.

## Requisitos previos

- proveedor identificado;
- pedido de proveedor localizado;
- mercancía física disponible;
- cantidades contadas o medidas;
- albarán del proveedor cuando exista;
- número de albarán;
- líneas pendientes visibles;
- posibilidad de comprobar el pedido de cliente asociado cuando corresponda.

## Vista general

Seleccionar proveedor
→ localizar pedido
→ revisar líneas pendientes
→ comparar mercancía física
→ introducir cantidad real
→ comprobar checks y estado
→ registrar número de albarán
→ generar albarán
→ confirmar asignación
→ revisar stock y pendientes

## Procedimiento principal

### Paso 1. Abrir la recepción de pedidos de proveedor

Acceda a la pantalla de recepción documentada.

[![Ventana de recepción con proveedor, pedido y líneas pendientes señalados](/assets/simgest/operativa/cap_17_recepcion_pedidos_proveedor.png =70%x)](/assets/simgest/operativa/cap_17_recepcion_pedidos_proveedor.png)

*La captura muestra la cabecera y las líneas que deben identificarse antes de introducir cantidades.*

**Qué debe comprobar**

- empresa;
- fecha;
- serie;
- proveedor;
- pedido;
- líneas pendientes;
- artículos y descripciones.

### Paso 2. Seleccionar el proveedor y localizar el pedido

La documentación indica que al seleccionar el proveedor el sistema muestra sus pedidos pendientes.

**Qué debe hacer**

1. seleccione el proveedor del albarán físico;
2. localice el pedido correspondiente;
3. compare número, fecha o referencia;
4. revise las líneas mostradas;
5. confirme que la mercancía pertenece a ese pedido.

No elija un pedido únicamente porque contiene el mismo artículo. Puede existir la misma referencia en varios pedidos o proyectos.

### Paso 3. Comprobar el indicador Falta tela cuando proceda

El material documenta una relación con el pedido de cliente asociado y el check **Falta tela**.

**Qué debe comprobar**

- que el pedido de cliente asociado muestra la falta de material antes de la recepción;
- que la línea recibida corresponde a esa necesidad;
- que el indicador se actualiza después de recibir.

El procedimiento exacto para localizar el pedido asociado en todos los casos es **Pendiente de validación por Hacchi**.

### Paso 4. Comparar la pantalla con la mercancía física

Antes de escribir una cantidad:

- identifique artículo y descripción;
- revise color, variante o lote cuando aparezcan;
- compruebe unidad;
- revise cantidad pedida;
- revise cantidad pendiente;
- cuente o mida lo recibido;
- compare con el albarán del proveedor.

**Regla principal**

La columna **Recibir** debe contener únicamente la cantidad física que ha llegado.

### Paso 5. Introducir la cantidad real

[![Tabla de recepción con la columna Recibir y los checks de estado señalados](/assets/simgest/operativa/cap_18_introducir_recibir.png =70%x)](/assets/simgest/operativa/cap_18_introducir_recibir.png)

*La captura muestra la zona donde se registra la cantidad y los indicadores que cambian según el valor introducido.*

Introduzca la cantidad en la línea correcta.

**Qué debe comprobar**

- artículo correcto;
- unidad correcta;
- cantidad física;
- ausencia de un valor copiado de otra línea;
- efecto de la cantidad sobre los checks.

### Paso 6. Interpretar Procesar albarán y Pedido servido

La documentación funcional establece:

- si la cantidad recibida es igual o superior a la pedida, el sistema marca **Procesar albarán** y **Pedido servido**;
- si la cantidad recibida es inferior, se marca **Procesar albarán** y el pedido permanece pendiente;
- si se marca **Servido** manualmente, el pedido se cierra aunque falten unidades.

**Advertencia**

No marque **Servido** para eliminar una línea pendiente sin una decisión funcional confirmada. El criterio corporativo para forzar el cierre es **Pendiente de validación por Hacchi**.

### Paso 7. Registrar el número de albarán del proveedor

El número puede introducirse durante la recepción o posteriormente en el albarán, según la documentación.

**Opción A. Durante la recepción**

1. localice el campo **Nº albarán**;
2. escriba el número exacto del documento del proveedor;
3. revíselo antes de generar;
4. continúe con el albarán.

**Opción B. Después de la recepción**

1. abra la lista de albaranes;
2. localice el albarán interno generado;
3. edite el campo del número de proveedor;
4. guarde;
5. vuelva a comprobar.

**Riesgo de duplicado**

La documentación indica que el sistema avisa si el número ya existe, pero permite continuar. Forzar un duplicado puede duplicar el stock. Ante el aviso, no continúe hasta comprobar el documento y la recepción anterior.

### Paso 8. Generar el albarán

Pulse la acción **Generar albarán** documentada.

El sistema puede preguntar si debe asignar los materiales a todos los pedidos relacionados. La demostración responde afirmativamente.

El criterio aplicable cuando existan excepciones o materiales que no deban asignarse es **Pendiente de validación por Hacchi**.

### Paso 9. Revisar el albarán generado

[![Albarán generado con número interno, proveedor y líneas recibidas señalados](/assets/simgest/operativa/cap_21_albaran_generado.png =70%x)](/assets/simgest/operativa/cap_21_albaran_generado.png)

*La captura muestra el documento interno producido por la recepción.*

Abra el albarán y revise:

- número interno;
- número del proveedor;
- proveedor;
- fecha;
- artículos;
- cantidades;
- unidades;
- líneas incluidas.

[![Ficha de albarán con cabecera y detalle de líneas señalados](/assets/simgest/operativa/cap_22_revision_albaran.png =70%x)](/assets/simgest/operativa/cap_22_revision_albaran.png)

*La imagen muestra la comprobación final del documento guardado.*

### Paso 10. Comprobar efectos posteriores

Después de generar:

- revise que el pedido servido desaparece de pendientes cuando corresponda;
- compruebe que las cantidades parciales permanecen abiertas;
- verifique el stock creado;
- compruebe la asignación de material;
- revise el indicador **Falta tela**;
- confirme que no existe un albarán duplicado.

## Escenarios de recepción

### Escenario A. Recepción completa

Introduzca la cantidad total recibida. Si coincide con la pedida, el sistema marca procesamiento y pedido servido según el comportamiento documentado.

**Resultado esperado**

El pedido se cierra, se genera el albarán y el stock refleja la cantidad recibida.

### Escenario B. Recepción parcial

[![Recepción parcial con cantidad recibida y cantidad pendiente señaladas](/assets/simgest/operativa/cap_19_recepcion_parcial.png =70%x)](/assets/simgest/operativa/cap_19_recepcion_parcial.png)

*La captura muestra una línea en la que parte de la cantidad permanece pendiente.*

1. introduzca solo la cantidad recibida;
2. compruebe que **Pedido servido** no queda marcado;
3. genere el albarán parcial;
4. revise la cantidad restante;
5. mantenga el pedido pendiente.

Se permiten varias recepciones parciales del mismo pedido según la documentación.

### Escenario C. Recepción superior a lo pedido

El material indica que el sistema acepta una cantidad superior, marca ambos checks y aumenta el stock con la cantidad real.

**Control obligatorio**

No introduzca una cantidad superior sin verificar que realmente ha llegado y que debe aceptarse. El criterio comercial o logístico para aceptar exceso es **Pendiente de validación por Hacchi**.

### Escenario D. Cierre manual con unidades pendientes

Marcar **Servido** manualmente cierra el pedido aunque falten unidades.

Esta acción debe considerarse excepcional. No debe utilizarse para limpiar pendientes. La autorización y motivo válido son **Pendiente de validación por Hacchi**.

## Seguimiento y reclamación

[![Pantalla de reclamación con pedidos fuera de plazo señalados](/assets/simgest/operativa/cap_20_reclamacion_pedido.png =70%x)](/assets/simgest/operativa/cap_20_reclamacion_pedido.png)

*La captura muestra pedidos pendientes o fuera de plazo utilizados para seguimiento.*

La documentación indica que los pedidos fuera de plazo aparecen en rojo y que existe una acción **Reclamación de pedido** que genera un documento. El usuario debe revisar y modificar el texto cuando sea necesario y realizar el envío manualmente.

La reclamación no se envía automáticamente.

## Resultado esperado

El albarán registra exactamente la mercancía física recibida. Las cantidades parciales permanecen pendientes, el stock y la asignación corresponden al material real y cualquier número de albarán duplicado se detiene antes de confirmar.

## Comprobación final

- [ ] Proveedor y pedido correctos.
- [ ] Mercancía física contada o medida.
- [ ] Artículo, variante y unidad revisados.
- [ ] Cantidad Recibir introducida línea por línea.
- [ ] Checks interpretados según el escenario.
- [ ] Recepciones parciales mantienen el resto pendiente.
- [ ] Número de albarán introducido y comprobado.
- [ ] No se forzó un duplicado.
- [ ] Albarán interno abierto y comparado.
- [ ] Stock y asignación revisados.
- [ ] Indicadores y pedidos pendientes actualizados correctamente.

## Errores habituales

| Error | Consecuencia | Actuación |
|---|---|---|
| Copiar la cantidad pedida | Se registra mercancía no recibida | Introducir solo lo físico. |
| Escribir en otra línea | Stock y albarán incorrectos | Comparar artículo y descripción. |
| Marcar Servido en una parcial | Se cierra el resto pendiente | Desmarcar y validar el criterio. |
| Forzar un número duplicado | Puede duplicarse el stock | Detener y localizar el albarán anterior. |
| No revisar efectos posteriores | El error queda oculto | Comprobar stock, pendientes y asignación. |
| Aceptar exceso sin autorización | Se registra material no previsto | Pendiente de validación por Hacchi. |

---

[← 9. Generar pedidos a proveedor](/simgest/operativa/09-pedidos-proveedor) · [Índice de operativa](/simgest/operativa) · [11. Consultar pedidos de cliente →](/simgest/operativa/11-pedidos-cliente)
