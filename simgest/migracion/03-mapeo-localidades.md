---
title: "3. Mapeo de Localidades (El proceso más complejo)"
description: "Migración Factusol a SIMGEST: 3. Mapeo de Localidades (El proceso más complejo)"
published: true
tags:
  - simgest
  - migracion
  - factusol
editor: markdown
---

<!-- AÑADIR_CONTENIDO_ANTES_DEL_MODULO -->


<a href="/assets/simgest/migracion/mig_04_ruta_tablas_auxiliares.png"><img src="/assets/simgest/migracion/mig_04_ruta_tablas_auxiliares.png" alt="Ruta de acceso a países, provincias y localidades" style="width: 80%; height: auto;" /></a>

*Ruta de acceso a países, provincias y localidades. Pulsa la imagen para abrirla a tamaño completo.*

> **⛔ Problema principal:**

1. Factusol solo tiene código postal + nombre de localidad


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_1 -->

1. Simgest requiere un código de localidad de su propia tabla jerárquica


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_2 -->

1. Sin código de localidad, NO se puede grabar un tercero en Simgest


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_3 -->


<!-- AÑADIR_CONTENIDO_ANTES_DE_DIFERENCIA-DE-ESTRUCTURA-ENTRE-AMBOS-SISTEMAS -->

## Diferencia de estructura entre ambos sistemas

| Aspecto | Factusol | Simgest |
| --- | --- | --- |
| Datos disponibles | Solo código postal + nombre de localidad | Tabla auxiliar jerárquica: País → Provincia/Región → Localidad → Código postal |
| Código de localidad | No existe | Cada localidad tiene un código único asignado automáticamente por el sistema |
| Requisito para grabar tercero | No requiere código de localidad | Obligatorio insertar un código de localidad |


<!-- AÑADIR_CONTENIDO_ANTES_DE_PASO-1-PREPARAR-LOS-DATOS-DE-ORIGEN -->

## Paso 1: Preparar los datos de origen

1. Extraer de Factusol: código postal + nombre de localidad de cada tercero


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_1 -->

1. Listar todas las combinaciones únicas de código postal + localidad


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_2 -->

1. Ordenar la lista para facilitar la búsqueda (por código postal ascendente)


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_3 -->


<!-- AÑADIR_CONTENIDO_ANTES_DE_PASO-2-CONSULTAR-LA-TABLA-DE-LOCALIDADES-DE-SIMGEST -->

## Paso 2: Consultar la tabla de localidades de Simgest

1. La tabla de Simgest tiene estructura jerárquica: País → Provincia/Región → Localidad → Código postal


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_1 -->

1. Cada localidad tiene un código único asignado automáticamente por el sistema


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_2 -->

1. Buscar cada combinación de código postal + localidad en la tabla


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_3 -->


<!-- AÑADIR_CONTENIDO_ANTES_DE_PASO-3-INTENTAR-MATCH-DIRECTO -->

## Paso 3: Intentar match directo

1. Si el código postal y la localidad existen en Simgest → asignar ese código de localidad


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_1 -->

1. Verificar que la provincia y el país también coincidan


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_2 -->

1. Si hay match completo → el mapeo es correcto, pasar al siguiente registro


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_3 -->


<!-- AÑADIR_CONTENIDO_ANTES_DE_PASO-4-MATCH-POR-CODIGO-POSTAL-CON-NOMBRES-DIFERENTES -->

## Paso 4: Match por código postal (con nombres diferentes)

1. Si el código postal coincide pero el nombre de la localidad es diferente (ej. parroquias de Galicia o Asturias con mismo CP)


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_1 -->

1. Simgest capturará la primera localidad que encuentre para ese código postal


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_2 -->

1. Puede no coincidir el nombre exacto de la parroquia/barrio con el de Factusol


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_3 -->

1. Asignar el código de todas formas y señalarlo para revisión posterior


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_4 -->


<!-- AÑADIR_CONTENIDO_ANTES_DE_ATENCION-ESPECIAL-PARA-MALLORCA -->

## ⚠️ Atención especial para Mallorca

1. Palma tiene múltiples barrios, cada uno con su código postal


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_1 -->

1. Un mismo código postal puede corresponder a múltiples entidades (barrios, distritos, parroquias)


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_2 -->

1. Verificar cuidadosamente que la localidad asignada corresponda a la dirección real del tercero


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_3 -->


<!-- AÑADIR_CONTENIDO_ANTES_DE_PASO-5-LOCALIDADES-SIN-MATCH-EN-SIMGEST -->

## Paso 5: Localidades sin match en Simgest

1. Si la localidad NO existe en la tabla de Simgest, hay que crearla (ver Sección 4)


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_1 -->

1. Si no se puede crear en ese momento, usar código "desconocida" como fallback (ver Sección 5)


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_2 -->


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_MODULO -->

---

[← 2. Mapeo de Formas de Pago](/simgest/migracion/02-mapeo-formas-pago) · [Índice](/simgest) · [4. Creación de una Nueva Localidad en Simgest (Paso a paso) →](/simgest/migracion/04-crear-localidad)
