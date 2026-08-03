---
title: "1. Qué es este programa y para qué lo usarán los trabajadores"
description: "Manual operativo SIMGEST: 1. Qué es este programa y para qué lo usarán los trabajadores"
published: true
tags: simgest, manual, operativa
editor: markdown
---

## 1. Comprender el entorno y el flujo de trabajo

SIMGEST integra en un mismo entorno la información comercial, las compras, la recepción de materiales, la producción, el inventario y la entrega. Trabajar correctamente no consiste solo en localizar una pantalla: es necesario comprender qué documento se está editando, de dónde procede y qué procesos puede activar después.

> **Objetivo**
>
> Reconocer la estructura general de SIMGEST y comprender la secuencia documentada del Proyecto Catorce antes de crear, modificar o confirmar documentos.

## A quién va dirigida esta entrada

El material funcional identifica como usuarios del proceso a:

- personal operativo encargado de la gestión del proyecto;
- personal de compras y aprovisionamiento;
- equipos relacionados con corte, confección, tapizado y embalaje;
- consultores o administradores que revisan la configuración.

Esta entrada no define permisos. El acceso exacto de cada perfil es **Pendiente de validación por Hacchi**.

## Qué debe comprender antes de operar

Cada módulo trabaja con documentos relacionados:

- la **oferta o proforma** contiene la propuesta comercial;
- el **pedido de cliente** recoge la oferta confirmada;
- las **necesidades de compra** derivan de los artículos y materiales requeridos;
- el **pedido a proveedor** formaliza el aprovisionamiento;
- la **recepción o albarán de proveedor** registra lo que ha llegado;
- el **stock y la asignación** reflejan la disponibilidad de materiales;
- la **planificación y fabricación** utilizan esa información para organizar el trabajo;
- la **gestión de carga** prepara la salida o entrega.

Modificar un documento sin revisar su origen puede alterar las fases siguientes. Por ejemplo, una cantidad incorrecta en una oferta puede terminar generando una necesidad de compra incorrecta; una recepción superior a la mercancía física puede aumentar el stock de forma indebida.

## Reconocer la pantalla general

[![Entorno general de SIMGEST con menú superior, barra de acciones y área de trabajo señalados](/assets/simgest/operativa/cap_s1_entorno_general.png =70%x)](/assets/simgest/operativa/cap_s1_entorno_general.png)

*La captura muestra la organización general observada en SIMGEST. Ábrala a tamaño completo para identificar las zonas señaladas.*

### Menú y módulos

El menú permite acceder a las áreas de trabajo. La posición exacta puede variar según la configuración, pero el usuario debe identificar primero el módulo funcional: ventas u ofertas, compras, recepción, artículos, producción, inventario o carga.

No debe abrirse una pantalla por similitud de nombre sin comprobar el tipo de documento que contiene.

### Barra de acciones

Las pantallas suelen incluir acciones para crear, guardar, buscar, editar, confirmar, imprimir o navegar entre registros. Cuando el icono no tenga texto visible, no debe asumirse su función por la forma del símbolo. La identificación exacta de un icono no confirmado es **Pendiente de validación por Hacchi**.

### Cabecera y detalle

Muchos documentos se dividen en:

- una cabecera con cliente, proveedor, referencia, proyecto, fechas o condiciones;
- una tabla inferior con artículos, materiales, cantidades, precios o estados.

La cabecera define el contexto del documento. El detalle desarrolla lo que se va a presupuestar, comprar, recibir o entregar.

### Estados y colores

Algunas pantallas muestran colores, marcas o checks para representar estados. Deben interpretarse únicamente cuando el material funcional lo confirma. Un color visible no debe convertirse en una regla general del ERP sin validación.

## Flujo general documentado

[![Diagrama del flujo desde oferta hasta entrega con las etapas principales señaladas](/assets/simgest/operativa/cap_s1_flujo_trabajo.png =70%x)](/assets/simgest/operativa/cap_s1_flujo_trabajo.png)

*La imagen resume la relación entre los principales documentos y procesos del Proyecto Catorce.*

### 1. Oferta o presupuesto

Se crea una oferta con el cliente, la referencia, el proyecto, las condiciones y las líneas de producto. Los materiales disponibles mencionan cortinas, cojines, alfombras y cuadrantes de microfibra como ejemplos del proyecto.

### 2. Pedido de cliente

Cuando la oferta se confirma, el sistema genera un pedido de cliente vinculado al proyecto. El pedido conserva productos, cantidades y precios procedentes de la oferta.

La confirmación no debe ejecutarse hasta completar la revisión comercial, porque el documento deja de ser únicamente una propuesta y pasa a formar parte del flujo operativo.

### 3. Compras y aprovisionamiento

Los artículos o materiales necesarios se preparan para compra. El sistema diferencia, según la documentación, entre materiales como telas y artículos de compraventa como alfombras. Estas categorías no deben mezclarse en el mismo procedimiento de pedido.

### 4. Recepción de mercancía

Cuando llega material, se registra la cantidad real recibida. La recepción genera un albarán interno y produce efectos sobre stock, pedidos pendientes y asignación de materiales según el escenario documentado.

### 5. Planificación y fabricación

El Plan Maestro de Producción utiliza pedidos, materiales y capacidad para organizar el trabajo. Las fases mencionadas incluyen corte, confección, tapizado y embalaje.

Los procedimientos detallados de planificación y fabricación no disponen todavía de todas las capturas y validaciones necesarias en esta versión del manual. Su desarrollo completo es **Pendiente de validación por Hacchi**.

### 6. Entrega y carga

Los productos terminados pueden prepararse para carga y entrega. La documentación funcional menciona la posibilidad de entregas parciales basadas en fases completadas, pero el criterio operativo completo debe revisarse en el módulo correspondiente antes de incorporarlo como procedimiento definitivo.

## Reglas de trabajo antes de modificar un documento

1. Confirme la empresa y el módulo.
2. Localice el documento por cliente, proveedor, referencia, proyecto o número.
3. Compruebe que no está editando un registro parecido.
4. Revise la cabecera antes de las líneas.
5. Determine si la acción genera otro documento o cambia un estado.
6. Guarde solo después de revisar los datos modificados.
7. Vuelva a abrir o consultar el resultado cuando el proceso tenga efectos posteriores.

## Cómo leer los procedimientos de este manual

Cada procedimiento incluye:

- objetivo;
- momento de uso;
- requisitos previos;
- secuencia general;
- pasos explicados;
- comprobaciones;
- resultado esperado;
- errores habituales.

Las capturas se colocan junto al paso correspondiente y muestran únicamente la zona del programa necesaria para orientarse.

## Resultado esperado

El usuario puede identificar qué documento está utilizando, relacionarlo con la fase anterior y la siguiente y reconocer cuándo debe revisar antes de confirmar o guardar.

## Comprobación final

- [ ] Distingo oferta, pedido de cliente, pedido a proveedor y recepción.
- [ ] Comprendo la diferencia entre cabecera y líneas.
- [ ] Sé que una confirmación puede generar efectos posteriores.
- [ ] No interpreto iconos, colores o permisos no documentados.
- [ ] Conozco el flujo general del Proyecto Catorce.
- [ ] Sé dónde encontrar el procedimiento específico antes de realizar una tarea.

---

[← Índice de operativa](/simgest/operativa) · [2. Crear una oferta →](/simgest/operativa/02-presupuestos)
