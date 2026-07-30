---
title: 1. Cuentas Contables: Configuración Inicial
description: Migración Factusol a SIMGEST: 1. Cuentas Contables: Configuración Inicial
published: true
tags: simgest, migracion, factusol
editor: markdown
---


<!-- AÑADIR_CONTENIDO_ANTES_DEL_MODULO -->

# 1. Cuentas Contables: Configuración Inicial

[![Listado de terceros para revisar códigos y datos migrados](/assets/simgest/migracion/mig_01_listado_terceros.png)](/assets/simgest/migracion/mig_01_listado_terceros.png)

*Listado de terceros para revisar códigos y datos migrados. Pulsa la imagen para abrirla a tamaño completo.*

[![Identificación del tercero, códigos y cuenta contable](/assets/simgest/migracion/mig_02_cuentas_codigos.png)](/assets/simgest/migracion/mig_02_cuentas_codigos.png)

*Identificación del tercero, códigos y cuenta contable. Pulsa la imagen para abrirla a tamaño completo.*


<!-- AÑADIR_CONTENIDO_ANTES_DE_PASO-1-IDENTIFICAR-LAS-CUENTAS-CONTABLES-EXISTENTES -->

## Paso 1: Identificar las cuentas contables existentes

1. Tomar las cuentas contables de Factusol tal como están (códigos de cliente, proveedor, etc.)


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_1 -->

1. No modificar ninguna cuenta contable — se respetan íntegramente los valores originales


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_2 -->

1. Listar todas las cuentas utilizadas para verificar su integridad antes de la migración


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_3 -->


<!-- AÑADIR_CONTENIDO_ANTES_DE_PASO-2-CONFIRMAR-LA-ASIGNACION-DE-CUENTAS -->

## Paso 2: Confirmar la asignación de cuentas

1. Pedro respeta las cuentas que le pasa el equipo de Productivity Egea sin ninguna alteración


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_1 -->

1. Ejemplo: si un cliente tiene código 5 y cuenta 430…5 en Factusol, esos mismos valores se mantienen en Simgest


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_2 -->

1. Verificar que la cuenta 430 (clientes) y 400 (proveedores) mantengan sus últimos dígitos originales


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_3 -->

1. La correspondencia es directa: código de Factusol → mismo código en Simgest


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_4 -->


<!-- AÑADIR_CONTENIDO_ANTES_DE_PASO-3-MANEJO-DEL-CODIGO-DE-TERCERO-NUEVO-EN-SIMGEST -->

## Paso 3: Manejo del código de tercero (nuevo en Simgest)

1. Simgest requiere un código de tercero que NO existía en Factusol


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_1 -->

1. Este código es nuevo y en principio su número exacto es irrelevante para el equipo


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_2 -->

1. Pedro lo genera automáticamente durante la migración


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_3 -->

1. Al traspasar el tercero a cliente/proveedor/agente, se respeta el código original de Factusol


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_4 -->

1. El código de tercero es un identificador interno del sistema — no afecta la operativa diaria


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_5 -->


<!-- AÑADIR_CONTENIDO_ANTES_DE_CASO-ESPECIAL-MISMO-CIF-COMO-CLIENTE-Y-PROVEEDOR -->

## ⚠️ Caso especial: Mismo CIF como cliente y proveedor

1. Un mismo CIF puede existir como cliente y como proveedor con datos diferentes


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_1 -->

1. Los datos de la ficha de cliente se graban en la tabla de clientes


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_2 -->

1. Los datos de la ficha de proveedor se graban en la tabla de proveedores


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_3 -->

1. NO se mezclan en la tabla de terceros — cada rol mantiene sus datos independientes


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_4 -->

1. Las notas de cada tabla se insertan en su correspondiente tipo de tercero


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_PUNTO_5 -->


<!-- AÑADIR_CONTENIDO_DESPUES_DEL_MODULO -->

---

[← 15. Errores habituales y cómo evitarlos](/assets/simgest/operativa/15-errores-habituales) · [Índice](/simgest) · [2. Mapeo de Formas de Pago →](/simgest/00-migracion-factusol/02-mapeo-formas-pago)
