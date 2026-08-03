---
title: "2. Crear un presupuesto / oferta de cliente desde cero"
description: "Manual operativo SIMGEST: 2. Crear un presupuesto / oferta de cliente desde cero"
published: true
tags: simgest, manual, operativa
editor: markdown
---

## 2. Crear una oferta o presupuesto

En SIMGEST, el presupuesto se gestiona mediante una **Oferta/Proforma de Cliente**. Este documento reúne la identificación del cliente y del trabajo, las condiciones comerciales, las notas y las líneas de artículos que forman la propuesta.

La calidad del presupuesto depende de la coherencia entre cabecera y detalle. Crear líneas antes de completar la cabecera puede aplicar una tarifa, un proyecto o unas condiciones incorrectas y trasladar el error a documentos posteriores.

> **Objetivo**
>
> Crear una oferta completa, vinculada al cliente y proyecto correctos, con líneas revisables y preparada para la revisión final y la generación del PDF.

## Cuándo utilizar este procedimiento

Utilícelo para registrar una nueva propuesta comercial o para completar una oferta que aún no ha sido confirmada como pedido.

No debe utilizarse para modificar un pedido de cliente ya generado sin comprobar primero cuál es el documento vigente. El estado exacto y las acciones permitidas después de confirmar una oferta son **Pendiente de validación por Hacchi** cuando no estén visibles en el material.

## Requisitos previos

Antes de crear la oferta debe disponer de:

- cliente identificado;
- referencia clara del trabajo;
- proyecto al que se vinculará;
- fecha y condiciones aplicables;
- tarifa que corresponda;
- dirección o destino cuando sea necesario;
- forma de pago confirmada;
- relación de productos, cantidades, medidas y precios;
- notas u observaciones relevantes.

Los materiales del proyecto incluyen como ejemplos cortinas, cojines, alfombras y cuadrantes de microfibra. Cada producto puede requerir una configuración distinta y no debe tratarse como una línea genérica si depende de medidas, composición, color o acabado.

## Vista general

Abrir Ofertas
→ crear un registro
→ completar cabecera
→ revisar notas
→ añadir líneas
→ verificar cantidades y precios
→ guardar
→ volver a revisar
→ continuar con la forma de pago y la emisión

## Procedimiento

### Paso 1. Abrir la pantalla de ofertas

El material visual identifica la ventana como **Oferta/Proforma de Cliente**. La entrada puede encontrarse en el área de Ventas u Ofertas según la configuración visible.

[![Pantalla de Oferta Proforma de Cliente con la ventana principal señalada](/assets/simgest/operativa/cap_s2_abrir_oferta.png =70%x)](/assets/simgest/operativa/cap_s2_abrir_oferta.png)

*La captura muestra la ventana que debe abrirse antes de crear o consultar una oferta.*

**Qué debe hacer**

1. Acceda al área de ofertas.
2. Abra **Oferta/Proforma de Cliente**.
3. Utilice la acción de alta o creación confirmada en su entorno.
4. Compruebe que la pantalla está preparada para un registro nuevo.

**Qué debe comprobar**

- no aparecen datos de otra oferta como si fueran la nueva;
- el número o identificador se encuentra vacío o en estado de alta;
- la cabecera puede completarse;
- no se han añadido líneas antes de seleccionar al cliente.

**Resultado esperado**

La ventana está preparada para introducir una oferta nueva y no existe riesgo de sobrescribir un documento anterior.

### Paso 2. Completar la cabecera

La cabecera identifica a quién pertenece el presupuesto y cómo se relaciona con el proyecto.

[![Oferta con los campos principales de cabecera y la tabla de líneas señalados](/assets/simgest/operativa/cap_s2_cabecera_detalle.png =70%x)](/assets/simgest/operativa/cap_s2_cabecera_detalle.png)

*La imagen diferencia la zona de identificación del documento de la tabla inferior de artículos.*

#### Cliente

Seleccione el cliente correcto. No debe elegirse únicamente por similitud de nombre. Cuando existan varias fichas, compruebe CIF, dirección u otros datos disponibles.

#### Referencia

Escriba una descripción que permita reconocer el trabajo sin abrir las líneas. El material de origen muestra como ejemplo una referencia relacionada con un hotel y el tipo de trabajo.

Una referencia profesional debe evitar textos genéricos como “presupuesto”, “varios” o “prueba”.

#### Proyecto

Vincule la oferta al proyecto correspondiente. Esta relación permite localizar las ofertas del mismo proyecto y mantener la trazabilidad hacia pedidos y procesos posteriores.

Un proyecto puede tener varias ofertas o versiones. Por tanto, proyecto y referencia deben utilizarse conjuntamente para identificar el documento correcto.

#### Fecha y vigencia

Introduzca o revise las fechas visibles. El significado exacto de cada fecha debe respetar la etiqueta del campo. No se inventará el uso de una fecha que no esté confirmada.

#### Tarifa

Seleccione la tarifa aplicable antes de añadir líneas. La tarifa puede influir en los precios que se muestran o calculan.

#### Dirección

Revise la dirección relacionada con el trabajo o la entrega cuando aparezca en la pantalla. No se debe asumir que la dirección principal del cliente es siempre la dirección del proyecto.

#### Forma de pago y condiciones

Seleccione la condición pactada. El procedimiento detallado está en [Seleccionar la forma de pago](/simgest/operativa/03-formas-de-pago).

**Control de cabecera**

Antes de continuar, confirme:

- cliente;
- referencia;
- proyecto;
- fechas;
- tarifa;
- dirección;
- forma de pago.

### Paso 3. Revisar las notas

[![Oferta con el panel de notas y la tabla inferior señalados](/assets/simgest/operativa/cap_s2_notas_lineas.png =70%x)](/assets/simgest/operativa/cap_s2_notas_lineas.png)

*La captura muestra el panel utilizado para observaciones y la zona donde se registran las líneas con importe.*

El panel de notas puede contener información del cliente, ubicaciones, habitaciones, aclaraciones u observaciones internas.

**Qué debe hacer**

- revise si ya existen notas cargadas;
- mantenga la información histórica salvo indicación expresa;
- añada solo observaciones necesarias y comprensibles;
- diferencie una nota de una línea presupuestable.

**Regla de control**

Si un elemento tiene artículo, cantidad, precio o importe, debe registrarse también en las líneas. Una nota no sustituye un concepto económico.

### Paso 4. Añadir las líneas de artículos

La parte inferior contiene los productos y servicios que forman la oferta.

**Para cada línea debe comprobarse, cuando los campos estén disponibles:**

- artículo o referencia;
- descripción;
- cantidad;
- unidad;
- medidas;
- precio;
- IVA;
- descuentos;
- color, acabado o variante;
- relación con el proyecto o estancia cuando proceda.

**Secuencia recomendada para cada línea**

1. Seleccione el artículo real.
2. Compruebe la descripción.
3. Introduzca cantidad y medidas.
4. Revise variante, color o acabado.
5. Compruebe el precio y la unidad.
6. Revise IVA y descuento.
7. Confirme el importe de la línea.
8. Continúe con la siguiente.

No utilice artículos de prueba en producción. El material visual contiene referencias de demostración, pero la oferta final debe utilizar las referencias validadas.

### Paso 5. Tratar los productos configurables

#### Cortinas

La documentación las describe como productos configurables por composición de material y medidas, con cálculo relacionado con metros cuadrados y variantes de tela.

#### Cojines

Pueden depender de dimensiones, composición y componentes internos como cuadrantes de microfibra.

#### Alfombras

Se tratan como artículos de compraventa y pueden depender de medidas, color y acabado.

#### Cuadrantes de microfibra

Aparecen como componentes relacionados con cojines y como artículos adquiridos a proveedor.

La forma exacta de introducir cada configuración debe seguir la ficha de artículo y el escandallo. No se debe completar una variante por semejanza con otra referencia.

### Paso 6. Guardar y revisar la oferta

Guarde cuando cabecera, notas y líneas estén completas.

Después de guardar:

1. compruebe que el registro conserva cliente, proyecto y referencia;
2. revise que todas las líneas siguen presentes;
3. compare importes y totales;
4. confirme la forma de pago;
5. verifique que no se ha creado un duplicado;
6. continúe con la revisión previa a emisión.

[![Oferta Proforma de Cliente con cabecera, notas y líneas de artículos visibles](/assets/simgest/operativa/cap_01_oferta_proforma.png =70%x)](/assets/simgest/operativa/cap_01_oferta_proforma.png)

*Vista completa utilizada para la comprobación del documento antes de emitirlo.*

## Resultado esperado

La oferta queda guardada con el cliente y proyecto correctos, una referencia reconocible, condiciones revisadas y líneas completas. El documento está preparado para la revisión comercial y la generación del PDF, pero no debe confirmarse todavía si existen dudas o datos pendientes.

## Comprobación final

- [ ] La oferta corresponde al cliente correcto.
- [ ] La referencia identifica el trabajo.
- [ ] El proyecto está informado.
- [ ] Fechas, tarifa y dirección se han revisado.
- [ ] La forma de pago corresponde a la condición pactada.
- [ ] Las notas necesarias se conservan.
- [ ] Cada concepto con importe está en una línea.
- [ ] Artículos, cantidades, medidas, precios, IVA y descuentos son coherentes.
- [ ] Los productos configurables tienen sus variantes revisadas.
- [ ] La oferta se ha guardado y vuelto a comprobar.

## Errores habituales

| Error | Efecto posterior | Prevención | Actuación |
|---|---|---|---|
| Crear líneas antes de la cabecera | Se aplican tarifa o proyecto incorrectos | Completar cabecera primero | Revisar todas las líneas. |
| Seleccionar un cliente parecido | El presupuesto queda asociado a otra ficha | Comprobar datos identificativos | Corregir antes de emitir. |
| Usar una referencia genérica | Dificulta localizar versiones | Describir cliente, zona o trabajo | Renombrar de forma clara. |
| Escribir un concepto solo en notas | No aparece correctamente como importe | Crear una línea de artículo | Añadir la línea correspondiente. |
| Usar un artículo de prueba | Compra o fabricación incorrecta | Seleccionar referencia validada | Sustituir antes de guardar. |
| Confirmar con datos pendientes | El error se traslada al pedido | Aplicar la revisión completa | Detener y corregir. |

---

[← 1. Comprender el entorno](/simgest/operativa/01-introduccion) · [Índice de operativa](/simgest/operativa) · [3. Seleccionar forma de pago →](/simgest/operativa/03-formas-de-pago)
