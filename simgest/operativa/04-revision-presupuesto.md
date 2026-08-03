---
title: "4. Revisar el presupuesto antes de emitirlo"
description: "Manual operativo SIMGEST: 4. Revisar el presupuesto antes de emitirlo"
published: true
tags: simgest, manual, operativa
editor: markdown
---

## 4. Revisar una oferta antes de emitirla

> **Objetivo**
>
> Detectar errores de cliente, proyecto, condiciones, artículos, cantidades, precios e impuestos antes de generar el documento que verá el cliente.

## Cuándo utilizar este procedimiento

Realiza esta revisión después de guardar la oferta y antes de generar el PDF o ejecutar una confirmación que cambie su estado.

## Requisitos previos

- Oferta guardada.
- Información comercial disponible.
- Artículos y cantidades introducidos.
- Forma de pago revisada.
- Acceso a las notas y a la tabla de líneas.

## Vista general

Revisar cabecera
→ revisar condiciones
→ revisar notas
→ revisar líneas
→ comprobar estados visuales
→ guardar correcciones
→ repetir la revisión

## Procedimiento

### Paso 1. Confirmar la identidad del documento

Revisa:

- cliente;
- referencia;
- dirección y localidad;
- proyecto;
- fechas;
- tarifa;
- agente o transportista cuando el proceso lo utilice.

[![Oferta con los datos de cabecera, proyecto, fechas y tabla de líneas señalados](/assets/simgest/operativa/cap_03_revision_presupuesto.png =70%x)](/assets/simgest/operativa/cap_03_revision_presupuesto.png)

*Vista de revisión previa a la emisión del presupuesto. Pulsa la imagen para abrirla a tamaño completo.*

### Paso 2. Confirmar las condiciones comerciales

Comprueba la forma de pago y los porcentajes visibles que afecten al documento. No modifiques margen, transporte, descuento o comisión sin un criterio confirmado.

### Paso 3. Revisar las notas

Lee el panel de notas y confirma que:

- las observaciones pertenecen al cliente o trabajo correcto;
- no hay instrucciones contradictorias;
- la información que deba aparecer en el documento está en el campo adecuado;
- no se han incluido datos innecesarios.

**Campo exacto desde el que una nota se imprime en el PDF:** Pendiente de validación por Hacchi

### Paso 4. Revisar cada línea

Para cada artículo, comprueba:

| Dato | Control |
|---|---|
| Artículo | Es la referencia solicitada |
| Descripción | Permite entender el concepto |
| Unidades | Coinciden con la solicitud |
| Precio | Procede de la tarifa o está validado |
| Descuento | Es el autorizado |
| IVA | Está informado correctamente |
| Acabado o variante | Corresponde al producto real |
| Aclaración | No contradice la descripción |

### Paso 5. Interpretar colores y estados con precaución

Si una línea o celda aparece en rojo o con otro color, detén la emisión y revisa el dato. La fuente visual muestra estados coloreados, pero no confirma el significado general de todos ellos.

**Significado exacto de cada color o estado:** Pendiente de validación por Hacchi

### Paso 6. Corregir y repetir la revisión

Después de cualquier cambio:

1. guarda la oferta;
2. vuelve a abrir o refrescar el documento;
3. comprueba el dato modificado;
4. repite el control de cabecera y líneas afectadas.

## Resultado esperado

La oferta queda completa, coherente y preparada para generar el PDF sin errores conocidos.

## Comprobación final

- [ ] Cliente, referencia y proyecto correctos.
- [ ] Fechas, tarifa y forma de pago revisadas.
- [ ] Notas correspondientes al trabajo.
- [ ] Todas las líneas revisadas individualmente.
- [ ] Precios, descuentos e IVA comprobados.
- [ ] No quedan colores o estados sin interpretar.
- [ ] Correcciones guardadas y verificadas.

## Errores habituales

| Error | Cómo detectarlo | Actuación |
|---|---|---|
| Revisar solo el total | Una línea puede tener precio o cantidad incorrectos | Comprobar línea por línea. |
| Dar por válido un color | Se desconoce su significado | Detener la emisión y validar. |
| Corregir sin volver a comprobar | El cambio puede no quedar guardado | Reabrir o refrescar la oferta. |

---

[← 3. Seleccionar la forma de pago](/simgest/operativa/03-formas-de-pago) · [Índice de operativa](/simgest/operativa) · [5. Generar y comprobar el PDF →](/simgest/operativa/05-generar-pdf)
