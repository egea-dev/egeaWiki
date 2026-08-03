---
title: "8. Trabajar con tarifas de proveedor"
description: "Manual operativo SIMGEST: 8. Trabajar con tarifas de proveedor"
published: true
tags: simgest, manual, operativa
editor: markdown
---

## 8. Revisar tarifas de proveedor

Las tarifas de proveedor relacionan artículos, variantes, unidades y precios. La revisión debe partir de la documentación oficial del proveedor y terminar con una comparación en SIMGEST. Copiar un precio sin verificar acabado, ancho, unidad o vigencia puede introducir un valor correcto en la línea equivocada.

> **Objetivo**
>
> Comprobar que las tarifas internas de SIMGEST reproducen los datos oficiales del proveedor y que los artículos utilizan la referencia, unidad, variante y precio adecuados.

## Cuándo utilizar este procedimiento

Utilícelo al crear o actualizar una tarifa, al revisar un artículo duplicado, cuando un precio calculado no coincide con la documentación y antes de generar pedidos de compra basados en esas tarifas.

## Contexto documentado

La documentación funcional indica que las tarifas heredadas contienen datos obsoletos, duplicados o mal configurados y que se plantea reconstruirlas desde información oficial, conservando únicamente artículos base validados.

Ese contexto no autoriza a eliminar datos desde este manual. La decisión, alcance y ejecución de una limpieza masiva son **Pendiente de validación por Hacchi**.

## Requisitos previos

- tarifa oficial vigente;
- proveedor identificado;
- artículo o familia;
- unidad de precio;
- acabado, color, ancho o variante;
- fecha de vigencia;
- moneda;
- ficha de compras y ventas del artículo;
- acceso a la tarifa interna de SIMGEST.

## Vista general

Abrir tarifa oficial
→ identificar producto y unidad
→ localizar artículo en SIMGEST
→ revisar proveedor habitual
→ revisar duplicación si aplica
→ comparar tarifa interna
→ resolver diferencias
→ guardar y comprobar

## Procedimiento

### Paso 1. Revisar la tarifa oficial

[![Tarifa oficial de proveedor en PDF con columnas de producto, acabado y precio señaladas](/assets/simgest/operativa/cap_08_tarifa_pdf.png =70%x)](/assets/simgest/operativa/cap_08_tarifa_pdf.png)

*La captura muestra el documento de origen que debe utilizarse para validar la tarifa interna.*

**Qué debe identificar**

- proveedor;
- fecha o versión;
- producto o familia;
- acabado;
- color;
- ancho;
- precio;
- suplemento;
- unidad de cálculo;
- moneda.

**Control crítico**

No copie un precio hasta confirmar si corresponde a pieza, metro, metro cuadrado u otra unidad. Tampoco utilice una columna de acabado diferente aunque el importe parezca razonable.

### Paso 2. Localizar el artículo correcto en SIMGEST

Abra la ficha del artículo y revise el bloque de compras y ventas.

[![Ficha de compras y ventas con proveedor, tarifa y datos de artículo señalados](/assets/simgest/operativa/cap_10_ficha_compras_ventas.png =70%x)](/assets/simgest/operativa/cap_10_ficha_compras_ventas.png)

*La imagen muestra la zona donde debe comprobarse la relación del artículo con el proveedor y la tarifa.*

**Qué debe comprobar**

- código y descripción;
- proveedor habitual;
- unidad de compra;
- tarifa asociada;
- moneda;
- fechas;
- variantes;
- ausencia de una referencia duplicada o heredada sin validar.

### Paso 3. Revisar artículos duplicados

Cuando se duplica un artículo, el sistema puede preguntar si también debe duplicar la información de tarifa y proveedor habitual.

[![Mensaje de confirmación para duplicar tarifa y proveedor habitual señalado](/assets/simgest/operativa/cap_09_confirmacion_duplicado.png =70%x)](/assets/simgest/operativa/cap_09_confirmacion_duplicado.png)

*La captura muestra el aviso que debe leerse antes de aceptar la herencia de datos.*

**Acepte únicamente cuando:**

- el nuevo artículo utiliza el mismo proveedor;
- la unidad es la misma;
- la tarifa es aplicable;
- el precio o estructura puede heredarse;
- las variantes no cambian la condición.

**Cancele cuando:**

- cambia proveedor;
- cambia unidad;
- cambia acabado o familia;
- el nuevo artículo tendrá otra tarifa;
- no existe evidencia suficiente.

Después de duplicar, revise siempre código, nombre, familia, ancho, unidad, tarifa y proveedor.

### Paso 4. Abrir el mantenimiento de tarifa interna

[![Mantenimiento de tarifa interna con proveedor, tarifa, vigencia y líneas señalados](/assets/simgest/operativa/cap_15_tarifa_interna.png =70%x)](/assets/simgest/operativa/cap_15_tarifa_interna.png)

*La captura muestra la pantalla donde se comparan y mantienen los precios internos.*

Seleccione:

- proveedor;
- tarifa;
- moneda;
- fechas de vigencia;
- artículo o filtro necesario.

No edite una línea hasta confirmar que pertenece al artículo y variante correctos.

### Paso 5. Comparar tarifa oficial e interna

Realice la comparación campo por campo:

| Elemento | Tarifa oficial | SIMGEST | Resultado |
|---|---|---|---|
| Artículo o familia | Valor de proveedor | Referencia interna | Coincide / No coincide |
| Unidad | Pieza, metro, m², etc. | Unidad interna | Coincide / No coincide |
| Acabado | Opción oficial | Variante interna | Coincide / No coincide |
| Ancho o medida | Valor oficial | Campo interno | Coincide / No coincide |
| Precio | Importe oficial | Importe interno | Coincide / No coincide |
| Vigencia | Fecha o versión | Fechas internas | Coincide / No coincide |

**Qué debe hacer ante una diferencia**

No elija manualmente el valor que parezca más probable. Determine si la diferencia procede de:

- otra unidad;
- otra columna de acabado;
- una tarifa antigua;
- un artículo duplicado;
- una variante no configurada;
- una actualización del proveedor;
- un error de carga.

El criterio de resolución y aprobación de discrepancias es **Pendiente de validación por Hacchi**.

### Paso 6. Revisar estructuras de precio específicas

La documentación menciona que las alfombras pueden calcularse a partir de un precio base por metro cuadrado más incrementos por acabado. También identifica una pregunta abierta sobre el ancho y tamaño máximo de rollo de una referencia concreta.

Cuando falte un dato del proveedor, no debe completarse la tarifa por estimación. Debe registrarse la pregunta y mantener la configuración pendiente.

### Paso 7. Guardar y volver a comprobar

Guarde únicamente la línea revisada.

Después:

1. aplique el mismo filtro;
2. vuelva a localizar el artículo;
3. compare el valor guardado;
4. revise unidad y variante;
5. compruebe que no se modificaron otras líneas;
6. registre la fuente utilizada.

## Resultado esperado

La tarifa interna puede relacionarse con una fuente oficial y cada importe está asociado al artículo, proveedor, unidad, variante y vigencia correctos.

## Comprobación final

- [ ] Se utilizó la tarifa oficial vigente.
- [ ] Proveedor y artículo están identificados.
- [ ] Unidad y moneda coinciden.
- [ ] Acabado, color y ancho son correctos.
- [ ] Se revisó la herencia en artículos duplicados.
- [ ] No se eligió un precio por aproximación.
- [ ] Las diferencias están resueltas o registradas.
- [ ] La línea se volvió a comprobar después de guardar.
- [ ] La fuente y versión de la tarifa están documentadas.

## Errores habituales

| Error | Consecuencia | Actuación |
|---|---|---|
| Copiar la columna equivocada | Precio incorrecto | Revisar acabado y encabezado. |
| Confundir metro con metro cuadrado | Importe desproporcionado | Confirmar unidad. |
| Aceptar herencia al duplicar sin revisar | Proveedor o tarifa incorrectos | Corregir ficha y tarifa. |
| Mantener una tarifa heredada obsoleta | Compra calculada con precios antiguos | Comparar con fuente oficial. |
| Completar un dato faltante por estimación | Configuración no validada | Pendiente de validación por Hacchi. |

---

[← 7. Revisar ficha y escandallo](/simgest/operativa/07-ficha-articulo-escandallo) · [Índice de operativa](/simgest/operativa) · [9. Generar pedidos a proveedor →](/simgest/operativa/09-pedidos-proveedor)
