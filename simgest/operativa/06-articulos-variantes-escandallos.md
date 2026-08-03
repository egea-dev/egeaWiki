---
title: "6. Configurar artículos, variantes y escandallos"
description: "Manual operativo SIMGEST: 6. Configurar artículos, variantes y escandallos"
published: true
tags: simgest, manual, operativa
editor: markdown
---

## 6. Revisar partes tapizables y variantes

> **Objetivo**
>
> Comprobar la configuración de las partes tapizables y las variantes de un modelo antes de utilizarlo en presupuestos, compras o fabricación.

## Cuándo utilizar este procedimiento

Utilízalo cuando un artículo dependa de tela, material, medida, acabado, color, unidades o incrementos asociados a una variante.

La modificación de esta configuración puede afectar a consumos, precios o fabricación. Debe realizarla personal formado.

**Perfiles autorizados y permisos concretos:** Pendiente de validación por Hacchi

## Requisitos previos

- Artículo o modelo identificado.
- Parte tapizable que debe revisarse.
- Tela o material confirmado.
- Medidas y unidades disponibles.
- Criterio comercial o productivo para las variantes.

## Vista general

Abrir modelo
→ seleccionar parte tapizable
→ revisar material y medidas
→ revisar variantes
→ comprobar impacto
→ guardar solo si está confirmado

## Procedimiento

### Paso 1. Abrir el artículo o modelo

Localiza la ficha correcta por código o descripción. Comprueba que no estás trabajando sobre una referencia similar.

### Paso 2. Abrir las partes tapizables o variantes

Accede a la pantalla donde aparecen la parte, la tela, la descripción, la serie, el ancho, las unidades y la tabla inferior de variantes.

[![Pantalla de partes tapizables con datos de la parte y variantes inferiores señalados](/assets/simgest/operativa/cap_05_partes_tapizables.png =70%x)](/assets/simgest/operativa/cap_05_partes_tapizables.png)

*Configuración de una parte tapizable y de las variantes relacionadas con el modelo. Pulsa la imagen para abrirla a tamaño completo.*

### Paso 3. Revisar la parte principal

Comprueba:

- parte tapizable;
- tela o material;
- descripción;
- serie;
- ancho y alto cuando aparezcan;
- unidades;
- otras medidas visibles.

### Paso 4. Revisar las variantes inferiores

Cada variante puede modificar el comportamiento del artículo. Revisa los campos visibles relacionados con:

- metros o consumo;
- acabado;
- color;
- medida;
- incremento de precio;
- estado activo cuando aparezca.

No copies una variante de otro modelo sin comprobar que material, medida y unidad coinciden.

### Paso 5. Comprobar el impacto

Antes de guardar, determina si el cambio puede afectar:

- precio de venta;
- consumo de material;
- escandallo;
- pedido a proveedor;
- fabricación.

**Reglas exactas de recálculo automático:** Pendiente de validación por Hacchi

### Paso 6. Guardar y volver a abrir

Guarda únicamente cuando todos los datos estén confirmados. Vuelve a abrir la ficha y comprueba que la variante aparece asociada al modelo correcto.

## Resultado esperado

El modelo mantiene partes, materiales, medidas y variantes coherentes con el producto que se va a presupuestar o fabricar.

## Comprobación final

- [ ] Artículo o modelo correcto.
- [ ] Parte tapizable correcta.
- [ ] Tela o material confirmado.
- [ ] Medidas y unidades revisadas.
- [ ] Variantes completas.
- [ ] Impacto sobre precio y consumo evaluado.
- [ ] Cambios guardados y comprobados.

## Errores habituales

| Error | Riesgo | Actuación |
|---|---|---|
| Modificar un modelo parecido | Cambiar otro artículo | Verificar código y descripción. |
| Cambiar una variante sin revisar unidades | Consumo o precio incorrectos | Comparar material, medida y unidad. |
| No conocer el efecto del cambio | Alterar presupuesto o fabricación | Pendiente de validación por Hacchi |

---

[← 5. Generar y comprobar el PDF](/simgest/operativa/05-generar-pdf) · [Índice de operativa](/simgest/operativa) · [7. Revisar ficha y escandallo →](/simgest/operativa/07-ficha-articulo-escandallo)
