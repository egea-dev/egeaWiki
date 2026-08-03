---
title: "3. Mapeo de Localidades (El proceso más complejo)"
description: "Migración Factusol a SIMGEST: 3. Mapeo de Localidades (El proceso más complejo)"
published: true
tags: simgest, migracion, factusol
editor: markdown
---

## 3. Mapear localidades

> **Objetivo**
>
> Relacionar el código postal y el nombre de localidad de Factusol con el código interno de localidad que SIMGEST necesita para guardar un tercero.

## Cuándo utilizar este procedimiento

Utilízalo durante la preparación de terceros, antes de guardar o validar sus direcciones en SIMGEST. La localidad es un dato crítico porque SIMGEST trabaja con una tabla jerárquica propia.

## Diferencia entre los sistemas

| Aspecto | Factusol | SIMGEST |
|---|---|---|
| Datos de origen | Código postal y nombre de localidad | Código interno de localidad |
| Estructura | Información directa en la ficha | País → provincia o región → localidad → código postal |
| Condición para guardar | La fuente no documenta un código interno | El procedimiento indica que el tercero necesita un código de localidad válido |

## Requisitos previos

- Código postal y localidad de cada tercero.
- Dirección completa para resolver coincidencias dudosas.
- Acceso a las tablas auxiliares de países, provincias y localidades.
- Registro de incidencias para los casos sin coincidencia.

## Vista general

Preparar combinaciones únicas
→ consultar la tabla de SIMGEST
→ comprobar coincidencia completa
→ revisar coincidencias solo por código postal
→ crear o asignar un valor provisional

## Procedimiento

### Paso 1. Preparar las combinaciones de origen

Extrae de Factusol el código postal y el nombre de localidad de cada tercero. Después:

1. elimina duplicados exactos para trabajar con combinaciones únicas;
2. ordénalas por código postal;
3. conserva la relación con los terceros afectados;
4. separa los registros con datos incompletos.

**Resultado esperado:** existe una lista manejable de combinaciones que puede compararse con SIMGEST.

### Paso 2. Abrir las tablas auxiliares

La demostración muestra el acceso a países, provincias y localidades desde el área de tablas auxiliares.

[![Menú auxiliar con los accesos a países, provincias y localidades señalados](/assets/simgest/migracion/mig_04_ruta_tablas_auxiliares.png =70%x)](/assets/simgest/migracion/mig_04_ruta_tablas_auxiliares.png)

*Zona de SIMGEST desde la que se consultan las tablas geográficas auxiliares. Pulsa la imagen para abrirla a tamaño completo.*

**Qué debe comprobar:** antes de seleccionar una localidad, confirma también el país y la provincia o región asociada.

### Paso 3. Resolver una coincidencia completa

Cuando código postal y nombre de localidad coincidan:

1. selecciona el código interno correspondiente;
2. comprueba país y provincia;
3. registra el mapeo como confirmado;
4. continúa con el siguiente valor.

**Resultado esperado:** la localidad queda asociada sin necesidad de crear registros nuevos.

### Paso 4. Revisar coincidencias por código postal

Un código postal puede devolver un nombre diferente al de Factusol. La fuente señala casos de parroquias, barrios o distritos y advierte que SIMGEST puede tomar la primera localidad encontrada para ese código postal.

No confirmes la asignación solo porque coincida el código postal. Compara:

- nombre de la localidad;
- dirección completa;
- provincia;
- país;
- tercero afectado.

Si el nombre no coincide exactamente pero se asigna de forma provisional, registra el caso para revisión posterior.

### Paso 5. Aplicar el control especial de Mallorca

En Palma y otras zonas puede haber barrios o entidades diferentes relacionados con códigos postales próximos o compartidos. Verifica que la localidad seleccionada corresponda a la dirección real del tercero.

**Criterio cuando la dirección no permita decidir:** Pendiente de validación por Hacchi

### Paso 6. Tratar una localidad inexistente

- Si la localidad no existe, utiliza el procedimiento [Crear una localidad](/simgest/migracion/04-crear-localidad).
- Si no puede crearse en ese momento, utiliza el procedimiento [Localidad Desconocida](/simgest/migracion/05-localidad-desconocida) y registra la incidencia.

## Resultado esperado

Cada tercero tiene asignado un código de localidad confirmado o figura expresamente en la lista de incidencias con un valor provisional.

## Comprobación final

- [ ] Código postal y localidad de origen están disponibles.
- [ ] País y provincia coinciden con la dirección.
- [ ] Las coincidencias solo por código postal se han revisado manualmente.
- [ ] Los casos de Mallorca, Galicia, Asturias u otras zonas ambiguas están controlados.
- [ ] Las localidades inexistentes se han creado o registrado como provisionales.

## Errores habituales

| Error | Cómo detectarlo | Actuación |
|---|---|---|
| Aceptar la primera coincidencia del código postal | El nombre o la provincia no coincide | Revisar la dirección completa. |
| Perder la relación con el tercero afectado | El mapeo no indica dónde se utiliza | Añadir el código del tercero al control. |
| Usar una localidad provisional sin incidencia | No existe seguimiento posterior | Registrar el caso antes de continuar. |

---

[← 2. Mapear formas de pago](/simgest/migracion/02-mapeo-formas-pago) · [Índice de migración](/simgest/migracion) · [4. Crear una localidad →](/simgest/migracion/04-crear-localidad)
