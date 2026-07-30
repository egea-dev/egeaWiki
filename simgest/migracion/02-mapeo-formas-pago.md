---
title: 2. Mapeo de Formas de Pago
description: Migración Factusol a SIMGEST: 2. Mapeo de Formas de Pago
published: true
tags: simgest, migracion, factusol
editor: markdown
---


<!-- AÑADIR_CONTENIDO_ANTES_DEL_MODULO -->

# 2. Mapeo de Formas de Pago

[![Forma de pago y notas del cliente en la ficha del tercero](/assets/simgest/migracion/mig_03_forma_pago.png)](/assets/simgest/migracion/mig_03_forma_pago.png)

*Forma de pago y notas del cliente en la ficha del tercero. Pulsa la imagen para abrirla a tamaño completo.*

> **Problema: Los códigos de forma de pago de Factusol NO coinciden con los de Simgest. Cada sistema utiliza su propia codificación, lo que requiere un proceso de conversión manual.**


<!-- AÑADIR_CONTENIDO_ANTES_DE_PASO-1-EXTRAER-LOS-CODIGOS-DE-FORMA-DE-PAGO-DE-FACTUSOL -->

## Paso 1: Extraer los códigos de forma de pago de Factusol

1. Identificar todos los códigos de forma de pago utilizados en la base de datos de Factusol


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_1 -->

1. Listar cada código con su descripción asociada


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_2 -->

1. Verificar que no queden códigos sin documentar


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_3 -->


<!-- AÑADIR_CONTENIDO_ANTES_DE_PASO-2-CONSULTAR-LA-TABLA-DE-FORMAS-DE-PAGO-DE-SIMGEST -->

## Paso 2: Consultar la tabla de formas de pago de Simgest

1. Acceder a la tabla auxiliar de formas de pago en Simgest


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_1 -->

1. Revisar los códigos existentes y su significado


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_2 -->

1. Documentar la lista completa de formas de pago disponibles en Simgest


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_3 -->


<!-- AÑADIR_CONTENIDO_ANTES_DE_PASO-3-REALIZAR-EL-MAPEO-CODIGO-POR-CODIGO -->

## Paso 3: Realizar el mapeo código por código

1. Para cada código de Factusol, buscar su equivalente en la tabla de Simgest


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_1 -->

1. Si existe coincidencia directa → asignar el código de Simgest correspondiente


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_2 -->

1. Si NO existe equivalente → seguir el Paso 4


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_3 -->


<!-- AÑADIR_CONTENIDO_ANTES_DE_PASO-4-RESOLVER-CODIGOS-SIN-EQUIVALENCIA -->

## Paso 4: Resolver códigos sin equivalencia

Cuando un código de Factusol no tiene equivalente directo en Simgest, se tienen dos opciones:

1. Opción A: Crear la forma de pago nueva en la tabla de Simgest


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_1 -->

1. Opción B: Asignar temporalmente "Contado" como valor provisional


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_2 -->

En cualquiera de los dos casos:

1. Documentar qué códigos se asignaron temporalmente para que el equipo los actualice después


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_3 -->

1. Mantener un registro de trazabilidad: código Factusol → código Simgest asignado → estado (definitivo/provisional)


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_4 -->


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_MODULO -->

---

[← 1. Cuentas Contables: Configuración Inicial](/simgest/migracion/01-cuentas-contables) · [Índice](/simgest) · [3. Mapeo de Localidades (El proceso más complejo) →](/simgest/migracion/03-mapeo-localidades)
