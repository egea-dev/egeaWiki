---
title: "15. Errores habituales y cómo evitarlos"
description: "Manual operativo SIMGEST: 15. Errores habituales y cómo evitarlos"
published: true
tags: simgest, manual, operativa
editor: markdown
---

## 15. Errores habituales y actuación recomendada

Esta entrada reúne errores repetibles identificados en los materiales. Su finalidad no es sustituir el procedimiento correspondiente, sino ayudar a reconocer el problema, detener el proceso y volver al punto correcto de revisión.

> **Objetivo**
>
> Evitar que un error inicial se traslade a documentos posteriores y establecer una actuación segura cuando el usuario detecta una diferencia.

## Regla general de actuación

Ante un error:

1. detenga la confirmación o emisión;
2. identifique el documento y la línea afectados;
3. compruebe el dato de origen;
4. determine si el error está en cabecera, línea, tarifa, mapeo o configuración;
5. corrija solo el dato confirmado;
6. guarde;
7. vuelva a abrir y revisar;
8. repita los controles posteriores;
9. registre la incidencia si puede repetirse.

No debe corregirse un documento posterior para ocultar un error que continúa en el origen.

## Ofertas y presupuestos

### Crear líneas antes de completar la cabecera

**Qué ocurre**

Las líneas pueden heredar tarifa, proyecto, cliente o condiciones que no corresponden.

**Cómo detectarlo**

- precios inesperados;
- proyecto vacío o incorrecto;
- cliente equivocado;
- forma de pago no prevista.

**Actuación**

Complete la cabecera y revise todas las líneas. No asuma que se recalculan automáticamente.

### Seleccionar el cliente equivocado

**Cómo detectarlo**

El nombre se parece, pero CIF, dirección o referencia no coinciden.

**Actuación**

Detenga la emisión, seleccione la ficha correcta y vuelva a revisar cabecera, notas y condiciones.

### Usar una referencia genérica

**Consecuencia**

Dificulta distinguir versiones o trabajos del mismo cliente.

**Actuación**

Utilice una descripción relacionada con cliente, ubicación, proyecto o tipo de trabajo.

### Utilizar una forma de pago incorrecta

**Consecuencia**

El presupuesto presenta una condición comercial distinta.

**Actuación**

Abra el selector, compare con lo pactado, guarde y genere un nuevo PDF.

### Dejar un concepto solo en notas

**Consecuencia**

El concepto no forma parte del cálculo ni aparece como línea económica.

**Actuación**

Registre el artículo, cantidad y precio en el detalle y mantenga la nota solo como explicación.

### Enviar el PDF sin revisarlo

**Consecuencia**

Puede contener líneas omitidas, totales diferentes o textos cortados.

**Actuación**

Compare todas las páginas con la oferta. Si existe una diferencia, corrija SIMGEST y regenere.

## Artículos, variantes y escandallos

### Modificar una variante sin comprender el efecto

**Consecuencia**

Puede cambiar consumo, precio, compra o fabricación.

**Actuación**

Identifique la parte, unidad, material y procesos dependientes. Si el impacto no puede confirmarse: **Pendiente de validación por Hacchi**.

### Confundir la ficha con el escandallo

**Consecuencia**

Se corrige el artículo cuando el error está en un componente o a la inversa.

**Actuación**

Determine si el dato describe el producto o su composición.

### Utilizar unidades incompatibles

**Ejemplos**

- metros frente a unidades;
- metros cuadrados frente a metros lineales;
- cantidad por producto frente a total.

**Actuación**

Compare la unidad de ficha, componente y tarifa antes de guardar.

### Seleccionar un componente sin identificación suficiente

La documentación señala que algunas descripciones de cuadrantes no incluyen medidas.

**Actuación**

No seleccione por aproximación. Registre la falta de información y solicite validación.

## Tarifas de proveedor

### Copiar un precio desde una columna equivocada

**Cómo detectarlo**

El acabado, ancho o unidad no coincide con el artículo.

**Actuación**

Volver a la tarifa oficial y comprobar encabezados.

### Duplicar un artículo heredando proveedor o tarifa incorrectos

**Consecuencia**

El nuevo artículo queda relacionado con condiciones de otro producto.

**Actuación**

Revisar código, familia, unidad, proveedor, tarifa y variantes después de duplicar.

### Mantener tarifas heredadas obsoletas

**Consecuencia**

Los precios de compra se calculan con datos antiguos o duplicados.

**Actuación**

Comparar con fuente oficial. Las eliminaciones masivas requieren validación y no deben ejecutarse desde este manual.

### Completar un dato faltante por estimación

**Consecuencia**

La tarifa parece completa, pero no tiene respaldo del proveedor.

**Actuación**

Mantener la configuración pendiente y registrar la pregunta.

## Pedidos a proveedor

### Generar sin revisar proyecto o filtros

**Consecuencia**

Se incluyen necesidades de otros proyectos.

**Actuación**

Detener, revisar cada línea y generar de nuevo el documento correcto.

### Mezclar tela y compraventa

**Consecuencia**

Artículos con procesos y datos diferentes terminan en un mismo pedido.

**Actuación**

Separar las líneas según su tipo de compra.

### Dejar líneas sin proveedor

**Consecuencia**

El pedido no puede generarse correctamente o se asigna manualmente sin criterio.

**Actuación**

Revisar ficha, proveedor habitual y tarifa.

### Usar Marcar todo sin comprobar el listado

**Consecuencia**

Se seleccionan líneas ajenas, incorrectas o no revisadas.

**Actuación**

Desmarcar y validar el alcance antes de seleccionar en masa.

### No comprobar cantidades agrupadas

**Consecuencia**

Se compra una cantidad incorrecta aunque la suma se haya realizado automáticamente.

**Actuación**

Comparar el total con el detalle, variantes y unidades.

### Elegir una modalidad de generación no validada

**Consecuencia**

Las líneas pueden agruparse de forma distinta a la requerida.

**Actuación**

Utilizar solo la modalidad demostrada para el caso o marcar **Pendiente de validación por Hacchi**.

## Recepción

### Registrar la cantidad pedida en lugar de la recibida

**Consecuencia**

Stock, albarán y pedidos pendientes dejan de reflejar la mercancía real.

**Actuación**

Contar o medir físicamente e introducir solo lo recibido.

### Introducir la cantidad en otra línea

**Consecuencia**

Se actualiza el artículo equivocado.

**Actuación**

Comparar referencia, descripción, variante y unidad antes de escribir.

### Marcar Pedido servido en una recepción parcial

**Consecuencia**

El pedido se cierra aunque falten unidades.

**Actuación**

No forzar el cierre. El criterio excepcional requiere validación.

### Forzar un número de albarán duplicado

**Consecuencia**

La documentación advierte que puede duplicarse el stock.

**Actuación**

Detener, localizar el albarán anterior y comprobar si la mercancía ya fue recibida.

### Aceptar una cantidad superior sin autorización

**Consecuencia**

El stock aumenta por encima de lo pedido.

**Actuación**

Comprobar la mercancía y solicitar criterio funcional.

### No revisar los efectos posteriores

**Consecuencia**

Un error puede quedar oculto en stock, asignación o pendientes.

**Actuación**

Abrir el albarán, revisar stock, pedido pendiente e indicadores asociados.

## Consultas, columnas y carga

### Concluir que un campo no existe

**Causa habitual**

La columna está oculta.

**Actuación**

Abrir el menú de columnas visibles antes de modificar el procedimiento.

### Cambiar una vista compartida

**Consecuencia**

Otros usuarios pueden perder columnas necesarias.

**Actuación**

Comprobar el alcance antes de guardar. Si no se conoce: **Pendiente de validación por Hacchi**.

### Revisar una carga solo por totales

**Consecuencia**

Pueden faltar líneas o bultos aunque el total parezca correcto.

**Actuación**

Comparar detalle y mercancía física.

### Cerrar una carga sin criterio confirmado

**Consecuencia**

Se avanza con una preparación incompleta.

**Actuación**

Detener y validar el procedimiento de cierre.

## Migración

### Usar una versión antigua de los archivos

**Consecuencia**

Se pierden fichas o cambios recientes.

**Actuación**

Registrar y utilizar la última entrega confirmada.

### Renumerar códigos o cuentas

**Consecuencia**

Se pierde la correspondencia con Factusol.

**Actuación**

Restaurar los valores originales.

### Aceptar la primera localidad del código postal

**Consecuencia**

Puede asignarse otro barrio, parroquia o entidad.

**Actuación**

Revisar nombre, dirección, provincia y país.

### Utilizar Desconocida sin registrar incidencia

**Consecuencia**

El valor provisional queda como definitivo.

**Actuación**

Añadir el tercero al control y corregir posteriormente.

## Regla de detención

Detenga el proceso cuando:

- el documento no puede identificarse;
- existe una diferencia entre pantalla y fuente;
- el campo o botón no está confirmado;
- una acción puede cerrar, generar o duplicar información;
- no se conoce el efecto sobre documentos posteriores;
- falta autorización funcional;
- el sistema muestra un aviso de duplicado;
- la cantidad física no coincide.

En esos casos debe indicarse exactamente: **Pendiente de validación por Hacchi**.

## Resultado esperado

Los errores se detectan antes de confirmar o emitir, se corrigen en el punto de origen y las incidencias repetibles quedan documentadas para mejorar el manual y el proceso.

---

[← 14. Listas de comprobación](/simgest/operativa/14-checklists) · [Índice de operativa](/simgest/operativa) · [Manual SIMGEST](/simgest)
