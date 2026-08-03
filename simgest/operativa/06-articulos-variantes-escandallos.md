---
title: "6. Configurar artículos, variantes y escandallos"
description: "Manual operativo SIMGEST: 6. Configurar artículos, variantes y escandallos"
published: true
tags: simgest, manual, operativa
editor: markdown
---

## 6. Revisar partes tapizables y variantes

Las partes tapizables y las variantes describen cómo cambia un modelo según la tela, el acabado, el color, las medidas u otras opciones configurables. Una modificación incorrecta puede afectar al consumo de material, al precio o a la fabricación, por lo que esta pantalla no debe tratarse como un simple listado descriptivo.

> **Objetivo**
>
> Revisar que las partes tapizables y sus variantes representan correctamente el modelo antes de utilizarlas en ofertas, pedidos, compras o producción.

## Cuándo utilizar este procedimiento

Utilícelo al revisar un artículo configurable, al preparar una referencia nueva, al investigar un precio o consumo inesperado y antes de confirmar que una variante puede utilizarse en producción.

No debe modificarse una parte tapizable únicamente para corregir el resultado de una oferta concreta sin entender el efecto sobre el resto de documentos. El perfil autorizado para realizar cambios estructurales es **Pendiente de validación por Hacchi**.

## Requisitos previos

- artículo o modelo identificado;
- ficha correcta abierta;
- datos de tela o material;
- medidas y unidades disponibles;
- documentación técnica o tarifa cuando corresponda;
- conocimiento de qué variante se está revisando;
- posibilidad de comparar el resultado con el producto real o su ficha.

## Por qué requiere una revisión específica

Una parte tapizable puede incorporar datos como tela, descripción, serie, ancho y unidades. Las variantes inferiores pueden modificar metros, acabado, color o incremento de precio. Por tanto, un valor erróneo puede producir varios efectos a la vez:

- consumo de material incorrecto;
- precio distinto al esperado;
- compra de una tela o cantidad equivocada;
- fabricación con una configuración incompleta;
- dificultad para identificar el producto final.

## Vista general

Abrir artículo o modelo
→ localizar partes tapizables
→ revisar parte principal
→ revisar tela y medidas
→ analizar variantes
→ comprobar efecto
→ guardar solo si está validado
→ volver a abrir y revisar

## Procedimiento

### Paso 1. Abrir el artículo o modelo correcto

Busque por código y descripción. No seleccione una referencia únicamente porque el nombre se parezca.

**Qué debe comprobar**

- código;
- descripción;
- familia;
- modelo;
- estado o disponibilidad cuando aparezca;
- ausencia de otra referencia similar.

La revisión de variantes sobre el artículo equivocado puede parecer coherente y, aun así, afectar a otro producto.

### Paso 2. Abrir la pantalla de partes tapizables o variantes

[![Pantalla de partes tapizables con la parte superior y las variantes inferiores señaladas](/assets/simgest/operativa/cap_05_partes_tapizables.png =70%x)](/assets/simgest/operativa/cap_05_partes_tapizables.png)

*La captura muestra la relación entre la parte principal y las variantes asociadas al modelo.*

**Qué debe identificar**

- parte o componente tapizable;
- tela o material;
- descripción;
- serie;
- ancho;
- unidades;
- tabla de variantes.

No cambie valores antes de comprender qué parte está seleccionada y qué variantes dependen de ella.

### Paso 3. Revisar la parte principal

**Qué debe hacer**

Compare la parte visible con la configuración esperada del modelo.

**Qué debe comprobar**

- nombre de la parte;
- tela o material asociado;
- descripción suficientemente clara;
- serie correcta;
- ancho;
- alto u otras medidas visibles;
- unidades o cantidad base.

**Por qué se hace**

La parte principal actúa como referencia para las variantes. Si está mal identificada, el resto de opciones pueden aplicarse a un componente incorrecto.

### Paso 4. Revisar la tela o material asociado

Compruebe que la tela o material corresponde al producto y a la variante seleccionada.

**Controles**

- referencia correcta;
- color o acabado cuando aparezca;
- ancho compatible;
- unidad de consumo;
- ausencia de una referencia de prueba;
- coherencia con la tarifa o ficha del proveedor.

Cuando el material no pueda confirmarse con las fuentes disponibles: **Pendiente de validación por Hacchi**.

### Paso 5. Revisar las variantes inferiores

Analice cada variante de forma individual.

**Puede afectar a:**

- metros de material;
- acabado;
- color;
- medidas;
- incremento de precio;
- unidades;
- condiciones de fabricación.

**Qué debe comprobar**

1. la variante tiene un nombre identificable;
2. el valor pertenece al modelo abierto;
3. la unidad es coherente;
4. el incremento o consumo está asociado a la opción correcta;
5. no existen duplicados aparentes;
6. no faltan variantes necesarias para el producto.

### Paso 6. Comprobar el impacto antes de guardar

Antes de modificar una variante, determine qué procesos pueden utilizarla:

- oferta;
- cálculo de precio;
- escandallo;
- pedido a proveedor;
- consumo de material;
- fabricación.

El material de origen advierte que una variante mal configurada puede cambiar precio, consumo o fabricación. Por tanto, no debe guardarse una corrección sin comprobar su efecto en un ejemplo controlado.

El método exacto de prueba y aprobación de variantes es **Pendiente de validación por Hacchi**.

### Paso 7. Guardar y volver a abrir

Guarde únicamente cuando los datos estén confirmados.

Después de guardar:

1. vuelva a abrir el artículo;
2. seleccione la misma parte;
3. compruebe que las variantes permanecen;
4. revise el valor modificado;
5. confirme que no se alteraron otras líneas.

## Resultado esperado

Las partes tapizables y variantes describen de forma coherente el modelo y pueden utilizarse sin introducir errores conocidos de material, medida, consumo o precio.

## Comprobación final

- [ ] El artículo y el modelo son correctos.
- [ ] La parte principal está identificada.
- [ ] Tela, serie, ancho y unidades son coherentes.
- [ ] Todas las variantes se han revisado individualmente.
- [ ] No hay referencias de prueba ni duplicados evidentes.
- [ ] Se ha comprobado el impacto antes de modificar.
- [ ] El cambio está validado o marcado como pendiente.
- [ ] La ficha se ha vuelto a abrir después de guardar.

## Errores habituales

| Error | Consecuencia | Actuación |
|---|---|---|
| Modificar la referencia equivocada | Otro producto queda alterado | Confirmar código y modelo antes de editar. |
| Revisar solo el nombre de la variante | Se ignoran unidad, consumo o incremento | Comprobar todos los campos visibles. |
| Corregir un precio desde la variante sin revisar tarifa | Se oculta el origen del error | Comparar con tarifa y ficha. |
| Guardar una variante incompleta | Oferta o fabricación puede quedar incoherente | Detener y validar. |
| Desconocer el alcance del cambio | Se afectan otros documentos | Pendiente de validación por Hacchi. |

---

[← 5. Generar el PDF](/simgest/operativa/05-generar-pdf) · [Índice de operativa](/simgest/operativa) · [7. Revisar ficha y escandallo →](/simgest/operativa/07-ficha-articulo-escandallo)
