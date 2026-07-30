# Despliegue en Wiki.js 2.x

## Configuración recomendada

En **Administración → Almacenamiento**, añada el destino Git para `https://github.com/egea-dev/egeaWiki.git`, rama `main`, con una carpeta local persistente y escribible por Wiki.js. Configure la sincronización bidireccional solo si Wiki.js debe enviar sus cambios al repositorio.

Para escritura, use una Deploy Key SSH con permiso de escritura o un token de acceso fino limitado a este repositorio y a `Contents: Read and write`. No guarde credenciales en este repositorio.

## Primera importación

1. Configure y guarde el destino Git.
2. Compruebe que las páginas previstas son las de `simgest/` y que los assets se leen desde `assets/simgest/`. Wiki.js importa el repositorio completo; los documentos de soporte están en `.txt` para que no se publiquen como páginas.
3. Ejecute **Import Everything**. Las páginas de entrada se publican en `/simgest`, `/simgest/migracion` y `/simgest/operativa`.
4. Verifique `/simgest`, `/simgest/migracion` y `/simgest/operativa`, incluidas sus capturas y enlaces de navegación.

## Force Sync y recuperación

Use **Force Sync** solo tras decidir cuál es la copia autorizada. Antes, descargue o haga commit de los cambios pendientes. Ante un conflicto, conserve ambas versiones fuera de Wiki.js, resuelva el Markdown y los assets en Git, ejecute los tres validadores y sincronice de nuevo. No edite simultáneamente la misma página en Git y en Wiki.js.
