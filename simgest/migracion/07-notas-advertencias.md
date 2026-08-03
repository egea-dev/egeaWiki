---
title: "7. Notas y Advertencias Importantes"
description: "Migración Factusol a SIMGEST: 7. Notas y Advertencias Importantes"
published: true
tags: simgest, migracion, factusol
editor: markdown
---

## 7. Controles y advertencias de migración

> **Objetivo**
>
> Reunir los controles que deben aplicarse durante toda la migración para evitar trabajar con datos antiguos, perder trazabilidad o dar por definitivos valores provisionales.

## Cuándo utilizar esta entrada

Consulta esta página antes de preparar los archivos, durante el mapeo y antes de cerrar la revisión posterior.

## Controles sobre los archivos de origen

### Utilizar la versión más reciente

La fuente indica que desde las primeras entregas se produjeron cambios en cuentas bancarias, correos, teléfonos y fichas de clientes y proveedores. Antes de ejecutar una migración, confirma la fecha y versión de los archivos.

### Excel y Access

El procedimiento describe que ambos formatos contienen la misma información con estructuras distintas: Access distribuye los datos en varias tablas relacionadas y Excel los presenta de forma integrada.

**Formato oficial que debe utilizarse como fuente definitiva:** Pendiente de validación por Hacchi

No combines valores de dos versiones diferentes sin documentar cuál prevalece.

## Controles sobre localidades

- Verifica dirección, código postal, localidad, provincia y país.
- No confirmes automáticamente la primera coincidencia por código postal.
- Revisa con especial cuidado barrios, parroquias o distritos.
- Mantén una lista de valores Desconocida.
- Para países con tablas incompletas, crea primero país y provincia cuando esté confirmado.

## Controles sobre códigos

- El código interno de tercero es nuevo en SIMGEST.
- El código original de cliente, proveedor o agente debe conservarse según el mapeo documentado.
- Las cuentas contables deben mantener el valor de origen.
- Las formas de pago deben mapearse por significado y no por coincidencia numérica.

## Controles sobre roles

Un mismo CIF puede tener datos diferentes como cliente y como proveedor. Revisa de forma separada:

- datos comerciales;
- cuenta contable;
- forma de pago;
- notas;
- direcciones asociadas;
- información específica del rol.

## Registro mínimo de incidencias

| Dato | Contenido |
|---|---|
| Tercero | Código y razón social |
| Área | Cuenta, forma de pago, localidad u otro dato |
| Valor de origen | Dato de Factusol |
| Valor migrado | Dato visible en SIMGEST |
| Estado | Pendiente, provisional o resuelto |
| Acción | Corrección necesaria |
| Validación | Persona o criterio que confirma el cierre |

## Comprobación de cierre

- [ ] Se ha utilizado una única versión de datos identificada.
- [ ] Las cuentas y códigos se han comparado con el origen.
- [ ] Las formas de pago provisionales siguen controladas.
- [ ] Las localidades dudosas están señaladas.
- [ ] Los terceros con varios roles se han revisado por separado.
- [ ] No quedan incidencias cerradas sin una comprobación posterior.

## Regla de seguridad

Cuando el documento, el vídeo o la captura no permitan confirmar una acción, no completes el procedimiento por deducción. Utiliza exactamente:

**Pendiente de validación por Hacchi**

---

[← 6. Revisar la migración](/simgest/migracion/06-revision-post-migracion) · [Índice de migración](/simgest/migracion) · [Operativa diaria →](/simgest/operativa)
