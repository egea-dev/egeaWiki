---
title: "8. Trabajar con tarifas de proveedor"
description: "Manual operativo SIMGEST: 8. Trabajar con tarifas de proveedor"
published: true
tags: simgest, manual, operativa
editor: markdown
---

## 8. Revisar tarifas de proveedor

> **Objetivo**
>
> Comparar la tarifa oficial del proveedor con la información registrada en SIMGEST y evitar que se utilice un precio, acabado o unidad incorrectos.

## Cuándo utilizar este procedimiento

Utilízalo al crear o revisar artículos, al actualizar precios de compra, al duplicar referencias o antes de generar pedidos a proveedor.

## Requisitos previos

- Tarifa oficial vigente del proveedor.
- Proveedor identificado.
- Producto, familia o referencia que debe revisarse.
- Unidad de compra confirmada.
- Acabado, ancho o suplemento aplicable.

## Vista general

Localizar tarifa oficial
→ identificar producto y columna
→ comprobar unidad
→ revisar duplicación de datos
→ comparar con tarifa interna
→ guardar y verificar

## Procedimiento

### Paso 1. Revisar la tarifa oficial

Abre el documento oficial y localiza el producto o familia. Revisa la tabla completa antes de copiar un precio.

[![Tarifa oficial de proveedor en PDF con la tabla de precios señalada](/assets/simgest/operativa/cap_08_tarifa_pdf.png =70%x)](/assets/simgest/operativa/cap_08_tarifa_pdf.png)

*Documento de origen utilizado para identificar acabado, ancho, precio o suplemento. Pulsa la imagen para abrirla a tamaño completo.*

Comprueba:

- nombre del producto;
- acabado;
- ancho o medida;
- precio;
- suplemento;
- unidad de aplicación;
- vigencia del documento cuando aparezca.

No interpretes una cifra como precio por pieza si la tarifa trabaja por metro, metro cuadrado u otra unidad.

### Paso 2. Revisar la ficha de compras y ventas

La ficha del artículo contiene bloques relacionados con compras y ventas. Comprueba que proveedor, tarifa y unidad corresponden a la referencia.

[![Ficha de artículo con los datos generales y el bloque de compras y ventas señalados](/assets/simgest/operativa/cap_10_ficha_compras_ventas.png =70%x)](/assets/simgest/operativa/cap_10_ficha_compras_ventas.png)

*Vista utilizada para comprobar la relación del artículo con proveedor y tarifa. Pulsa la imagen para abrirla a tamaño completo.*

### Paso 3. Decidir qué ocurre al duplicar un artículo

Al duplicar, SIMGEST puede preguntar si debe copiar también la información de tarifa de proveedor y proveedor habitual.

[![Mensaje de confirmación para duplicar la información de tarifa y proveedor habitual](/assets/simgest/operativa/cap_09_confirmacion_duplicado.png =70%x)](/assets/simgest/operativa/cap_09_confirmacion_duplicado.png)

*Diálogo que debe leerse antes de heredar datos de compra en un artículo nuevo. Pulsa la imagen para abrirla a tamaño completo.*

- Acepta únicamente cuando el artículo nuevo deba mantener el mismo proveedor, tarifa y unidad.
- Cancela cuando cualquiera de esos datos vaya a cambiar.
- Después de duplicar, revisa código, nombre, familia, ancho, unidad, tarifa y proveedor.

### Paso 4. Revisar la tarifa interna

Abre **Mantenimiento de Tarifas de Proveedor**, selecciona el proveedor y la tarifa, y revisa moneda y fechas de vigencia.

[![Mantenimiento de tarifa interna con proveedor, tarifa y líneas de artículos señalados](/assets/simgest/operativa/cap_15_tarifa_interna.png =70%x)](/assets/simgest/operativa/cap_15_tarifa_interna.png)

*Pantalla utilizada para localizar y comparar el precio interno de una referencia. Pulsa la imagen para abrirla a tamaño completo.*

Utiliza el filtro por artículo cuando haya muchas líneas. Modifica solo la línea que corresponda a la referencia comprobada.

### Paso 5. Comparar antes de guardar

La tarifa interna debe coincidir con la fuente oficial en producto, acabado, ancho, unidad y precio. Si existen dos valores posibles y la fuente no permite decidir, no elijas uno por aproximación.

**Criterio para resolver discrepancias de tarifa:** Pendiente de validación por Hacchi

### Paso 6. Guardar y volver a comprobar

Guarda el cambio y localiza nuevamente la línea. Confirma que el precio y la vigencia permanecen asociados al artículo y proveedor correctos.

## Resultado esperado

La tarifa interna refleja el valor oficial aplicable a la referencia, con proveedor, unidad, acabado y vigencia correctos.

## Comprobación final

- [ ] Tarifa oficial vigente.
- [ ] Producto y acabado correctos.
- [ ] Ancho o medida correcta.
- [ ] Unidad de compra confirmada.
- [ ] Proveedor y tarifa interna correctos.
- [ ] Duplicación revisada.
- [ ] Precio comparado y comprobado después de guardar.

## Errores habituales

| Error | Riesgo | Actuación |
|---|---|---|
| Copiar la columna equivocada | Precio de otro acabado | Revisar encabezado y producto. |
| Confundir unidad de tarifa | Coste multiplicado o dividido incorrectamente | Confirmar pieza, metro o superficie. |
| Heredar proveedor al duplicar | Asociar la referencia al proveedor incorrecto | Revisar el diálogo y la ficha nueva. |
| Elegir entre dos precios sin criterio | Tarifa no validada | Pendiente de validación por Hacchi |

---

[← 7. Ficha de artículo y escandallo](/simgest/operativa/07-ficha-articulo-escandallo) · [Índice de operativa](/simgest/operativa) · [9. Generar pedidos a proveedor →](/simgest/operativa/09-pedidos-proveedor)
