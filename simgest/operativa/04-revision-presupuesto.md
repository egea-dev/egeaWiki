---
title: "4. Revisar el presupuesto antes de emitirlo"
description: "Manual operativo SIMGEST: 4. Revisar el presupuesto antes de emitirlo"
published: true
tags: simgest, manual, operativa
editor: markdown
---

## 4. Revisar una oferta antes de emitirla

La revisión previa es el control que separa una oferta guardada de una oferta preparada para presentarse al cliente o convertirse en pedido. Debe realizarse sobre la cabecera, las notas, las líneas y los totales, no únicamente sobre el aspecto general de la pantalla.

> **Objetivo**
>
> Detectar y corregir errores de identificación, proyecto, condiciones, artículos, cantidades, precios, impuestos y notas antes de generar el PDF o confirmar la oferta.

## Cuándo utilizar este procedimiento

Debe realizarse:

- después de crear la oferta;
- después de modificar artículos, cantidades o precios;
- después de cambiar la forma de pago;
- antes de generar el PDF;
- antes de confirmar la oferta como pedido.

Si la oferta se modifica después de generar el PDF, la revisión y la generación deben repetirse.

## Requisitos previos

- oferta guardada;
- información comercial disponible;
- cliente y proyecto identificados;
- líneas completas;
- precios y condiciones preparados;
- posibilidad de comparar con notas, mediciones o documentación de origen.

## Vista general

Identificar el documento
→ revisar cabecera
→ revisar condiciones
→ revisar notas
→ comprobar línea por línea
→ revisar totales
→ corregir
→ guardar
→ repetir el control

## Procedimiento

### Paso 1. Confirmar la identidad del documento

Antes de revisar importes, confirme que se trata de la oferta correcta.

**Revise:**

- cliente;
- número o identificador;
- referencia;
- proyecto;
- fecha;
- estado.

[![Oferta con los datos principales de cabecera y las líneas inferiores señalados](/assets/simgest/operativa/cap_03_revision_presupuesto.png =70%x)](/assets/simgest/operativa/cap_03_revision_presupuesto.png)

*La captura muestra las zonas que deben comprobarse antes de emitir el documento.*

**Por qué se hace**

Un documento puede ser internamente coherente y pertenecer al cliente, proyecto o versión equivocados. La identidad debe validarse antes de analizar el detalle.

### Paso 2. Revisar la cabecera completa

Compruebe:

- referencia clara y relacionada con el trabajo;
- proyecto informado;
- tarifa correcta;
- fechas coherentes;
- dirección o destino cuando proceda;
- forma de pago;
- otros campos visibles relevantes.

No dé por válido un campo únicamente porque contiene un valor. Debe ser el valor correcto para esa oferta.

### Paso 3. Revisar las condiciones comerciales

Abra o consulte el bloque de condiciones y confirme:

- forma de pago;
- descuentos generales si aparecen;
- tarifa;
- impuestos;
- cualquier condición visible que afecte al importe o al documento.

Los descuentos, recargos o condiciones no demostrados en las fuentes no deben añadirse a este manual como funciones disponibles.

### Paso 4. Revisar las notas

Lea las notas del cliente y las observaciones de la oferta.

**Qué debe comprobar**

- no se han borrado notas necesarias;
- las observaciones corresponden a esta oferta;
- no hay instrucciones contradictorias;
- los conceptos con precio también están en las líneas;
- no se ha copiado información de otro proyecto.

### Paso 5. Revisar cada línea de artículo

La revisión debe hacerse línea por línea, no solo sobre el total.

Para cada línea, compruebe:

1. artículo correcto;
2. descripción comprensible;
3. cantidad;
4. unidad;
5. medidas;
6. variante, color o acabado;
7. precio unitario;
8. descuento;
9. IVA;
10. importe resultante.

**Control específico de productos configurables**

- En cortinas, revise composición, medidas y tela.
- En cojines, revise dimensiones y componentes.
- En alfombras, revise medidas, acabado y color.
- En componentes, compruebe que la referencia corresponde al producto principal.

Cuando una línea depende de un escandallo o tarifa, la revisión comercial no sustituye la revisión técnica de la ficha.

### Paso 6. Revisar agrupaciones y versiones

Un mismo proyecto puede contener varias ofertas. Compruebe que las líneas corresponden a la versión que se va a emitir.

La documentación menciona la necesidad futura de agrupar artículos por estancia o planta mediante una plantilla estandarizada. Esa plantilla está pendiente de desarrollo; no debe presentarse como disponible.

Si la oferta contiene grupos manuales, confirme que no se han duplicado artículos entre secciones.

### Paso 7. Revisar totales

Compare:

- suma de líneas;
- descuentos;
- impuestos;
- total final;
- coherencia entre cantidades y precios.

El cálculo debe revisarse también en el PDF, porque la representación imprimible puede revelar cortes, omisiones o diferencias que no se perciben en pantalla.

### Paso 8. Interpretar colores y estados con precaución

Si la pantalla muestra colores, marcas o estados:

- utilice solo el significado documentado;
- no considere que un color confirma por sí solo la validez de la oferta;
- revise siempre los datos que representa.

El significado exacto de cualquier color no documentado es **Pendiente de validación por Hacchi**.

### Paso 9. Corregir y repetir la revisión

Cuando detecte un error:

1. corrija el dato;
2. guarde la oferta;
3. vuelva a abrir o actualizar la vista;
4. repita el control de la zona afectada;
5. revise el total si el cambio modifica importes;
6. genere un nuevo PDF si ya existía uno anterior.

No debe considerarse revisada una oferta que ha cambiado después del control.

## Resultado esperado

La oferta está completa, coherente y preparada para generar el PDF. No existen dudas abiertas sobre cliente, proyecto, condiciones, líneas o totales.

## Comprobación final

- [ ] Cliente, referencia, proyecto, fecha y estado correctos.
- [ ] Tarifa, dirección y forma de pago revisadas.
- [ ] Notas correctas y no contradictorias.
- [ ] Todas las líneas se han comprobado individualmente.
- [ ] Artículos configurables tienen medidas y variantes revisadas.
- [ ] Cantidades, precios, descuentos e IVA son correctos.
- [ ] El total coincide con el detalle.
- [ ] No hay líneas duplicadas ni de otra versión.
- [ ] La oferta se ha guardado después de las correcciones.
- [ ] La revisión se ha repetido tras el último cambio.

## Errores habituales

| Error | Por qué ocurre | Riesgo | Actuación |
|---|---|---|---|
| Revisar solo el total | Las líneas pueden contener referencias o cantidades erróneas | Se emite un documento incorrecto | Revisar línea por línea. |
| No comparar proyecto y versión | Se utiliza otra oferta del mismo cliente | Confusión comercial | Confirmar referencia y estado. |
| Dejar una nota como único registro de un concepto | El importe no se refleja correctamente | Oferta incompleta | Crear la línea correspondiente. |
| Corregir después de revisar y no repetir | El documento final no ha sido validado | Error no detectado | Repetir control completo. |
| Interpretar un color no documentado | Se da por válido un estado incorrecto | Decisión sin respaldo | Pendiente de validación por Hacchi. |

---

[← 3. Seleccionar forma de pago](/simgest/operativa/03-formas-de-pago) · [Índice de operativa](/simgest/operativa) · [5. Generar el PDF →](/simgest/operativa/05-generar-pdf)
