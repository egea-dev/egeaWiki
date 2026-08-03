---
title: "9. Generar pedidos a proveedor"
description: "Manual operativo SIMGEST: 9. Generar pedidos a proveedor"
published: true
tags: simgest, manual, operativa
editor: markdown
---

## 9. Generar pedidos a proveedor

> **Objetivo**
>
> Revisar las necesidades detectadas por SIMGEST y generar pedidos a proveedor únicamente para las líneas, cantidades y proyectos correctos.

## Cuándo utilizar este procedimiento

Utilízalo cuando los pedidos de cliente o la planificación generen necesidades de material o artículos de compra.

## Requisitos previos

- Proyecto identificado.
- Pedidos de cliente disponibles.
- Artículos y escandallos revisados cuando correspondan.
- Tarifas de proveedor validadas.
- Proveedor y fechas de entrega conocidos.

## Vista general

Abrir generación de pedidos
→ definir filtros
→ recalcular si procede
→ revisar necesidades
→ seleccionar líneas
→ revisar oferta o proveedor
→ generar pedido
→ comprobar resultado

## Procedimiento

### Paso 1. Abrir la generación de pedidos

Abre la pantalla documentada como **Pedidos a Proveedor según Pedidos Clientes**.

[![Pantalla de pedidos a proveedor con filtros y tabla de necesidades señalados](/assets/simgest/operativa/cap_12_pedidos_proveedor.png =70%x)](/assets/simgest/operativa/cap_12_pedidos_proveedor.png)

*Vista principal para filtrar las necesidades antes de generar compras. Pulsa la imagen para abrirla a tamaño completo.*

### Paso 2. Configurar los filtros

Revisa los campos visibles:

- serie;
- almacén;
- canal cuando aplique;
- tipo de filtro;
- número de proyecto;
- tipo o proveedor;
- fecha de entrega;
- opciones relativas a pedidos trabajados, falta de tela o líneas anuladas cuando aparezcan.

Para trabajar con Proyecto Catorce, utiliza el filtro de proyecto y comprueba el número antes de buscar.

No dejes un filtro vacío por comodidad si eso puede mezclar necesidades de otros proyectos.

### Paso 3. Resolver el aviso de recálculo

SIMGEST puede mostrar una confirmación para recalcular necesidades de materia prima.

[![Diálogo de confirmación para recalcular las necesidades de materia prima](/assets/simgest/operativa/cap_11_recalcular_materia_prima.png =70%x)](/assets/simgest/operativa/cap_11_recalcular_materia_prima.png)

*Aviso que aparece antes de actualizar el cálculo de necesidades. Pulsa la imagen para abrirla a tamaño completo.*

**Cuándo debe aceptarse o cancelarse el recálculo:** Pendiente de validación por Hacchi

No confirmes el diálogo sin conocer el efecto sobre las líneas ya revisadas.

### Paso 4. Revisar las necesidades detectadas

Comprueba en cada línea:

- proyecto;
- artículo y descripción;
- proveedor;
- unidades necesarias;
- unidades ya pedidas;
- fecha de entrega;
- estado visible;
- oferta o precio disponible en el bloque inferior.

Si aparece una línea de otro proyecto, corrige los filtros antes de seleccionar.

### Paso 5. Seleccionar las líneas

La pantalla permite seleccionar líneas individualmente y muestra una opción para marcar el conjunto.

[![Tabla de necesidades con las líneas seleccionadas y la opción Marcar todo señalada](/assets/simgest/operativa/cap_13_marcar_todo.png =70%x)](/assets/simgest/operativa/cap_13_marcar_todo.png)

*Selección de líneas que se incluirán en la generación del pedido. Pulsa la imagen para abrirla a tamaño completo.*

Utiliza **Marcar todo** únicamente cuando hayas comprobado que todas las líneas visibles deben procesarse. De lo contrario, selecciona solo las necesarias.

### Paso 6. Realizar la revisión final

Antes de generar, vuelve a comprobar proveedor, artículos, cantidades, fechas y proyecto.

[![Pantalla de revisión final con las necesidades y ofertas de proveedor señaladas](/assets/simgest/operativa/cap_14_revision_final_pedido_prov.png =70%x)](/assets/simgest/operativa/cap_14_revision_final_pedido_prov.png)

*Control final de las líneas antes de crear el pedido a proveedor. Pulsa la imagen para abrirla a tamaño completo.*

### Paso 7. Generar y comprobar el pedido

Ejecuta la acción de generación únicamente cuando las líneas sean correctas. Después, abre el pedido creado y compara sus líneas con la selección anterior.

**Nombre exacto del botón de generación y criterio de autorización:** Pendiente de validación por Hacchi

## Resultado esperado

Se crea un pedido para el proveedor correcto, limitado al proyecto y a las líneas revisadas, con cantidades y fechas coherentes.

## Comprobación final

- [ ] Proyecto y filtros correctos.
- [ ] Recálculo tratado con criterio confirmado.
- [ ] No hay líneas ajenas al proyecto.
- [ ] Artículos y cantidades revisados.
- [ ] Proveedor y tarifa validados.
- [ ] Selección final comprobada.
- [ ] Pedido generado abierto y comparado.

## Errores habituales

| Error | Riesgo | Actuación |
|---|---|---|
| Filtrar por proyecto incorrecto | Comprar para otro trabajo | Corregir el filtro y repetir la búsqueda. |
| Usar Marcar todo sin revisar | Incluir líneas no deseadas | Desmarcar y seleccionar individualmente. |
| Recalcular sin conocer el efecto | Cambiar necesidades revisadas | Pendiente de validación por Hacchi |
| No comprobar el pedido generado | Mantener errores de selección | Abrir y comparar las líneas creadas. |

---

[← 8. Revisar tarifas de proveedor](/simgest/operativa/08-tarifas-proveedor) · [Índice de operativa](/simgest/operativa) · [10. Registrar una recepción →](/simgest/operativa/10-recepcion-mercancia)
