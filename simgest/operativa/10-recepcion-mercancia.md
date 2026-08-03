---
title: "10. Recibir mercancía de proveedor"
description: "Manual operativo SIMGEST: 10. Recibir mercancía de proveedor"
published: true
tags: simgest, manual, operativa
editor: markdown
---

## 10. Registrar una recepción de proveedor

> **Objetivo**
>
> Registrar en SIMGEST la mercancía que ha llegado físicamente, mantener pendiente lo que no se ha recibido y revisar el albarán generado.

## Cuándo utilizar este procedimiento

Utilízalo cuando llegue mercancía asociada a un pedido de proveedor. No registres una recepción únicamente porque la fecha prevista haya llegado.

## Requisitos previos

- Pedido de proveedor identificado.
- Proveedor confirmado.
- Mercancía física disponible para contar o medir.
- Albarán del proveedor cuando forme parte del proceso.
- Cantidades pendientes visibles en SIMGEST.

## Vista general

Localizar pedido
→ revisar líneas pendientes
→ introducir cantidades reales
→ tratar recepciones parciales
→ confirmar
→ generar albarán
→ revisar documento

## Procedimiento

### Paso 1. Abrir la recepción y localizar el pedido

Abre la recepción de pedidos de proveedor y selecciona el pedido correspondiente. Revisa fecha, serie, proveedor y líneas pendientes.

[![Ventana de recepción con cabecera del pedido y líneas pendientes señaladas](/assets/simgest/operativa/cap_17_recepcion_pedidos_proveedor.png =70%x)](/assets/simgest/operativa/cap_17_recepcion_pedidos_proveedor.png)

*Selección del pedido de proveedor que se va a recepcionar. Pulsa la imagen para abrirla a tamaño completo.*

### Paso 2. Comparar pantalla y mercancía física

Antes de introducir cantidades:

1. identifica el artículo;
2. compara la descripción;
3. revisa la cantidad pedida;
4. revisa la cantidad pendiente;
5. cuenta o mide la mercancía recibida;
6. comprueba el número de albarán cuando proceda.

No utilices la cantidad pedida como cantidad recibida sin comprobar la mercancía física.

### Paso 3. Introducir la cantidad real

Registra en la columna **Recibir** únicamente la cantidad que ha llegado.

[![Tabla de recepción con la columna Recibir y el estado de las líneas señalados](/assets/simgest/operativa/cap_18_introducir_recibir.png =70%x)](/assets/simgest/operativa/cap_18_introducir_recibir.png)

*Registro de las cantidades físicas en las líneas del pedido. Pulsa la imagen para abrirla a tamaño completo.*

**Qué debe comprobar:** la cantidad introducida no debe superar lo que ha llegado y debe corresponder a la línea correcta.

### Paso 4. Registrar una recepción parcial

Cuando no llegue todo el pedido:

1. introduce solo la cantidad recibida;
2. deja el resto pendiente;
3. revisa el estado de la línea después de confirmar;
4. no marques el pedido como servido si queda material por recibir.

[![Recepción parcial con la cantidad recibida y la cantidad pendiente señaladas](/assets/simgest/operativa/cap_19_recepcion_parcial.png =70%x)](/assets/simgest/operativa/cap_19_recepcion_parcial.png)

*Ejemplo de una línea en la que una parte del pedido continúa pendiente. Pulsa la imagen para abrirla a tamaño completo.*

**Criterio exacto para marcar una línea como servida:** Pendiente de validación por Hacchi

### Paso 5. Revisar pedidos pendientes o fuera de plazo

La documentación visual incluye una pantalla de reclamación de pedidos con líneas pendientes.

[![Pantalla de reclamación con pedidos pendientes y datos de entrega señalados](/assets/simgest/operativa/cap_20_reclamacion_pedido.png =70%x)](/assets/simgest/operativa/cap_20_reclamacion_pedido.png)

*Consulta utilizada para localizar pedidos pendientes o fuera de plazo. Pulsa la imagen para abrirla a tamaño completo.*

Esta vista puede utilizarse para identificar pedidos que requieren seguimiento. El procedimiento corporativo para emitir o enviar una reclamación es **Pendiente de validación por Hacchi**.

### Paso 6. Confirmar la recepción

Confirma únicamente cuando:

- proveedor y pedido son correctos;
- todas las líneas recibidas están revisadas;
- las cantidades físicas coinciden;
- el número de albarán está introducido cuando corresponde;
- las líneas parciales mantienen el resto pendiente.

### Paso 7. Revisar el albarán generado

Después de confirmar, comprueba que SIMGEST ha generado el albarán con las líneas recibidas.

[![Albarán generado con su cabecera y líneas recibidas señaladas](/assets/simgest/operativa/cap_21_albaran_generado.png =70%x)](/assets/simgest/operativa/cap_21_albaran_generado.png)

*Resultado documental de la recepción registrada. Pulsa la imagen para abrirla a tamaño completo.*

Abre el documento y revisa cabecera, proveedor, número de albarán, artículos y cantidades.

[![Ficha del albarán de proveedor con cabecera y líneas inferiores señaladas](/assets/simgest/operativa/cap_22_revision_albaran.png =70%x)](/assets/simgest/operativa/cap_22_revision_albaran.png)

*Comprobación final del documento generado después de la recepción. Pulsa la imagen para abrirla a tamaño completo.*

## Resultado esperado

El albarán registra únicamente la mercancía recibida. Las cantidades no entregadas permanecen pendientes y el documento puede compararse con el albarán físico del proveedor.

## Comprobación final

- [ ] Pedido y proveedor correctos.
- [ ] Mercancía física contada o medida.
- [ ] Cantidad Recibir introducida línea por línea.
- [ ] Recepciones parciales mantienen el resto pendiente.
- [ ] Número de albarán revisado.
- [ ] Recepción confirmada solo después del control.
- [ ] Albarán generado abierto y comparado.

## Errores habituales

| Error | Riesgo | Actuación |
|---|---|---|
| Copiar la cantidad pedida en Recibir | Registrar mercancía no entregada | Introducir solo la cantidad física. |
| Marcar como servido un pedido parcial | Cerrar unidades pendientes | Revisar el estado antes de confirmar. |
| Introducir la cantidad en otra línea | Stock o albarán incorrectos | Comparar artículo y descripción. |
| Confirmar sin revisar el albarán | No detectar errores de recepción | Abrir el documento generado. |

---

[← 9. Generar pedidos a proveedor](/simgest/operativa/09-pedidos-proveedor) · [Índice de operativa](/simgest/operativa) · [11. Consultar pedidos de cliente →](/simgest/operativa/11-pedidos-cliente)
