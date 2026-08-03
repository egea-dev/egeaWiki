---
title: "12. Configurar columnas visibles"
description: "Manual operativo SIMGEST: 12. Configurar columnas visibles"
published: true
tags: simgest, manual, operativa
editor: markdown
---

## 12. Configurar las columnas visibles

Las tablas de SIMGEST pueden contener más campos de los que aparecen inicialmente en pantalla. Antes de concluir que un dato no existe, debe comprobarse si la columna está oculta. La configuración debe utilizarse para mejorar la revisión, no para eliminar controles necesarios.

> **Objetivo**
>
> Mostrar las columnas necesarias para una tarea concreta y organizar la vista sin ocultar información crítica ni alterar de forma no controlada la configuración de otros usuarios.

## Cuándo utilizar este procedimiento

Utilícelo cuando:

- un procedimiento menciona un campo que no aparece;
- la tabla contiene demasiadas columnas y dificulta la revisión;
- necesita comparar precio, stock, IVA, descuento, entrega u otro dato disponible;
- una captura no coincide con la vista actual.

No debe asumirse que la configuración es personal. El alcance de los cambios sobre otros usuarios es **Pendiente de validación por Hacchi** hasta comprobarlo.

## Requisitos previos

- pantalla y tabla correctas abiertas;
- conocimiento del dato que necesita revisar;
- permiso para modificar la vista si corresponde;
- posibilidad de restaurar la configuración anterior.

## Vista general

Identificar el dato necesario
→ abrir el menú de columnas
→ localizar el campo
→ activar o desactivar
→ revisar la tabla
→ comprobar el alcance
→ continuar con el proceso principal

## Procedimiento

### Paso 1. Confirmar que está en la tabla correcta

Antes de modificar columnas, compruebe:

- módulo;
- documento o listado;
- tabla superior o inferior;
- registro seleccionado;
- objetivo de la revisión.

Una misma pantalla puede incluir varias tablas con configuraciones diferentes.

### Paso 2. Abrir el menú de columnas visibles

[![Menú de columnas visibles con las opciones de activación señaladas](/assets/simgest/operativa/cap_23_columnas_visibles.png =70%x)](/assets/simgest/operativa/cap_23_columnas_visibles.png)

*La captura muestra el menú utilizado para mostrar u ocultar campos de la tabla.*

Localice la opción de configuración de columnas y abra el listado.

### Paso 3. Activar las columnas necesarias

Busque el campo por su nombre visible.

**Ejemplos mencionados en el material:**

- precio;
- stock;
- IVA;
- descuento;
- entrega.

Active únicamente las columnas necesarias para la tarea. Si el nombre no coincide exactamente con el manual, no seleccione una opción parecida sin comprenderla.

### Paso 4. Ordenar la revisión

Cuando el sistema permita mover o redimensionar columnas, coloque juntas las que deban compararse.

Ejemplos:

- pedido, recibido y pendiente;
- artículo, descripción y variante;
- cantidad, precio e importe;
- fecha prevista y estado.

El modo de guardar el orden o ancho de columnas no está confirmado para todas las pantallas.

### Paso 5. Reducir el ruido visual

Puede ocultar columnas que no aporten información a la tarea, siempre que:

- no elimine un control necesario;
- pueda restaurarlas;
- conozca el alcance de la configuración;
- no afecte a otros usuarios.

No oculte campos para evitar revisar una incidencia.

### Paso 6. Comprobar el alcance del cambio

Después de modificar la vista:

1. cierre y vuelva a abrir la pantalla si el proceso lo permite;
2. compruebe si la configuración se mantiene;
3. revise si afecta solo al usuario o a todo el entorno;
4. documente cualquier comportamiento compartido.

Si el alcance no puede confirmarse, no guarde la vista como configuración general.

### Paso 7. Volver al procedimiento principal

Una vez visible el dato, retome el procedimiento que originó la consulta y realice la comprobación pendiente.

La configuración de columnas no es el resultado final; es una herramienta para completar otra tarea.

## Criterio de uso corporativo

La configuración de columnas debe responder a una necesidad concreta de revisión. No se debe crear una vista distinta para cada usuario sin criterio común, porque después las capturas y los procedimientos pueden dejar de coincidir con la pantalla real. Cuando una columna sea imprescindible para un control habitual, conviene mantenerla visible de forma estable una vez confirmado el alcance de la configuración.

## Resultado esperado

La tabla muestra los datos necesarios para la revisión y el usuario conoce si el cambio es temporal, personal o compartido.

## Comprobación final

- [ ] Se modificó la tabla correcta.
- [ ] La columna activada corresponde al dato necesario.
- [ ] No se ocultaron controles críticos.
- [ ] La vista sigue siendo legible.
- [ ] Se comprobó el alcance de la configuración.
- [ ] Se retomó el procedimiento principal.
- [ ] Las dudas sobre persistencia o permisos están registradas.

## Errores habituales

| Error | Consecuencia | Actuación |
|---|---|---|
| Concluir que un dato no existe | Se omite una revisión disponible | Comprobar columnas ocultas. |
| Activar una columna de nombre parecido | Se interpreta otro dato | Confirmar la etiqueta exacta. |
| Ocultar demasiados campos | Se pierde contexto | Restaurar la vista necesaria. |
| Guardar una vista compartida sin saberlo | Se afecta a otros usuarios | Pendiente de validación por Hacchi. |
| No volver al proceso principal | La tarea queda incompleta | Retomar la comprobación original. |

---

[← 11. Consultar pedidos de cliente](/simgest/operativa/11-pedidos-cliente) · [Índice de operativa](/simgest/operativa) · [13. Revisar gestión de carga →](/simgest/operativa/13-gestion-carga)
