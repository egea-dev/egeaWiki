---
title: "5. Generar el PDF del presupuesto"
description: "Manual operativo SIMGEST: 5. Generar el PDF del presupuesto"
published: true
tags: simgest, manual, operativa
editor: markdown
---

## 5. Generar y comprobar el PDF

El PDF es la representación imprimible de la oferta. No debe considerarse correcto únicamente porque el archivo se haya generado: es necesario compararlo con la oferta guardada y revisar que la maquetación no oculte información.

> **Objetivo**
>
> Generar un PDF que reproduzca fielmente los datos de la oferta y comprobar su contenido antes de guardarlo, compartirlo o utilizarlo como documento de referencia.

## Cuándo utilizar este procedimiento

Debe realizarse después de completar la revisión de la oferta y cada vez que se modifique cualquier dato que aparezca en el documento.

No se debe reutilizar un PDF anterior después de cambiar cliente, referencia, forma de pago, líneas, cantidades, precios, notas o impuestos.

## Requisitos previos

- oferta guardada;
- revisión previa completada;
- cliente y referencia correctos;
- líneas e importes revisados;
- forma de pago confirmada;
- acceso a la opción de impresión o generación de documento.

La ruta exacta o el nombre del botón puede variar según la pantalla. Solo debe utilizarse la acción visible y confirmada en el entorno.

## Vista general

Abrir oferta revisada
→ generar documento
→ abrir PDF
→ revisar cabecera
→ revisar líneas
→ revisar totales
→ revisar maquetación
→ comparar con SIMGEST
→ corregir y regenerar si es necesario

## Procedimiento

### Paso 1. Confirmar que la oferta no tiene cambios pendientes

Antes de generar el documento:

- guarde la oferta;
- compruebe que la última modificación está visible;
- confirme cliente, referencia y proyecto;
- revise la forma de pago;
- confirme que no hay líneas en edición.

**Por qué se hace**

Si la generación utiliza la última versión guardada, un cambio no guardado podría no aparecer en el PDF.

### Paso 2. Generar el documento

Utilice la opción de imprimir, listar o generar documento observada en la oferta.

**Qué debe comprobar**

- que la acción corresponde al presupuesto y no a otro listado;
- que se genera un archivo o vista previa;
- que el documento pertenece a la oferta abierta;
- que no aparece un error de generación.

### Paso 3. Abrir el PDF generado

[![Presupuesto en PDF con cabecera, líneas y totales visibles](/assets/simgest/operativa/cap_04_pdf_presupuesto.png =70%x)](/assets/simgest/operativa/cap_04_pdf_presupuesto.png)

*La captura muestra el documento imprimible que debe compararse con la oferta.*

No revise el PDF únicamente en una miniatura. Amplíelo hasta que textos, cantidades y precios sean legibles.

### Paso 4. Revisar la cabecera del PDF

Compruebe:

- empresa emisora;
- cliente;
- número del documento;
- fecha;
- referencia;
- dirección cuando se muestre;
- proyecto si forma parte del formato;
- número de página.

**Control clave**

La cabecera debe corresponder a la oferta abierta. Si el cliente o la referencia no coinciden, no continúe revisando el detalle: cierre el documento, corrija la oferta y genere de nuevo.

### Paso 5. Revisar el detalle de artículos

Compare el PDF con las líneas de SIMGEST.

Para cada concepto, revise:

- orden de aparición;
- descripción;
- cantidad;
- unidad;
- precio;
- descuento;
- IVA;
- importe;
- medidas o variantes cuando se impriman.

**Qué debe comprobar**

- no faltan líneas;
- no aparecen líneas duplicadas;
- no se han cortado descripciones relevantes;
- el texto sigue siendo comprensible;
- los importes coinciden con la oferta.

### Paso 6. Revisar totales y condiciones

Compruebe:

- subtotal;
- descuentos;
- impuestos;
- total;
- forma de pago;
- observaciones visibles;
- cualquier condición incluida en el formato.

El total del PDF debe coincidir con el total revisado en SIMGEST.

### Paso 7. Revisar la maquetación

Una maquetación defectuosa puede convertir un dato correcto en información ilegible.

Revise:

- cortes de texto;
- saltos de página;
- líneas partidas de forma confusa;
- columnas superpuestas;
- páginas en blanco;
- cabeceras o pies fuera de posición;
- caracteres no legibles;
- totales separados de sus conceptos.

La revisión debe hacerse en todas las páginas, no solo en la primera.

### Paso 8. Corregir discrepancias

Si el PDF no coincide con la oferta:

1. identifique la diferencia;
2. vuelva a SIMGEST;
3. corrija el dato de origen;
4. guarde;
5. repita la revisión de la oferta;
6. genere un nuevo PDF;
7. descarte o diferencie claramente la versión anterior.

No debe editarse manualmente el PDF para ocultar una diferencia que sigue existiendo en SIMGEST.

### Paso 9. Guardar el documento correcto

Guarde el PDF con un nombre que permita identificarlo. El mini manual propone una estructura similar a:

`Presupuesto_[Cliente]_[Proyecto]_[Fecha].pdf`

Adapte el nombre a las reglas internas de almacenamiento cuando estén confirmadas. La carpeta o repositorio oficial de destino es **Pendiente de validación por Hacchi** si no se ha definido.

### Paso 10. Enviar o compartir

El procedimiento de envío, destinatarios, aprobación y registro de comunicaciones no aparece completamente confirmado en los materiales. Antes de enviar, debe verificarse el canal y la persona responsable. Cuando no esté definido: **Pendiente de validación por Hacchi**.

## Resultado esperado

El PDF reproduce la oferta guardada, puede leerse correctamente y no contiene diferencias de cliente, referencia, líneas, cantidades, precios, impuestos o condiciones.

## Comprobación final

- [ ] La oferta estaba guardada antes de generar.
- [ ] El PDF corresponde al documento correcto.
- [ ] Cabecera y referencia coinciden.
- [ ] Todas las líneas aparecen una sola vez.
- [ ] Cantidades, precios, descuentos e IVA coinciden.
- [ ] Totales y forma de pago son correctos.
- [ ] Todas las páginas se han revisado.
- [ ] No hay texto cortado ni columnas superpuestas.
- [ ] Las discrepancias se corrigieron en SIMGEST.
- [ ] El archivo guardado es la versión validada.

## Errores habituales

| Error | Consecuencia | Actuación |
|---|---|---|
| Generar antes de guardar | El PDF no incluye el último cambio | Guardar y regenerar. |
| Revisar solo la primera página | Se omiten errores del detalle | Revisar todas las páginas. |
| Enviar un PDF antiguo | El cliente recibe una versión incorrecta | Identificar y conservar solo la versión válida. |
| Corregir el PDF manualmente | SIMGEST mantiene el dato erróneo | Corregir el origen y regenerar. |
| No comparar totales | Puede existir una diferencia de cálculo o línea | Comparar con la oferta. |
| No revisar forma de pago | Se envía una condición incorrecta | Verificar antes de compartir. |

---

[← 4. Revisar la oferta](/simgest/operativa/04-revision-presupuesto) · [Índice de operativa](/simgest/operativa) · [6. Revisar partes y variantes →](/simgest/operativa/06-articulos-variantes-escandallos)
