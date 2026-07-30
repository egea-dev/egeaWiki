# Configuración exacta para egea-dev/egeaWiki

Repositorio preparado:

- Repositorio: `https://github.com/egea-dev/egeaWiki.git`
- Rama: `main`
- Carpeta de páginas: `/simgest`
- Carpeta de imágenes: `/assets/simgest`

## Primera subida desde Windows

1. Descomprime el ZIP.
2. Entra en la carpeta `egeaWiki_preparado`.
3. Haz doble clic en `SUBIR_A_EGEAWIKI.bat`.
4. GitHub abrirá el navegador o Git Credential Manager para iniciar sesión.
5. Autoriza la cuenta que tenga permiso de escritura sobre `egea-dev/egeaWiki`.

El script valida el paquete, crea el repositorio Git local, registra los archivos y ejecuta el primer `push` a `main`.

## Configuración inicial en Wiki.js 2.x

Abre:

`Administración > Almacenamiento > Git`

Configura:

- URL del repositorio: `https://github.com/egea-dev/egeaWiki.git`
- Rama: `main`
- Dirección: `Sync / Bidirectional` si quieres conservar también las ediciones hechas dentro de Wiki.js.
- Ruta local: una carpeta persistente y escribible por Wiki.js.

### Lectura solamente

Como el repositorio es público, Wiki.js puede clonarlo por HTTPS sin credenciales para una importación de solo lectura.

### Sincronización bidireccional

Para que Wiki.js pueda subir a GitHub las ediciones realizadas desde la propia wiki, utiliza una de estas opciones:

1. SSH con una Deploy Key que tenga permiso de escritura.
2. HTTPS con un Fine-grained Personal Access Token limitado al repositorio `egeaWiki`, con permiso `Contents: Read and write`.

Después de guardar la configuración, ejecuta:

`Import Everything`

## Actualizaciones posteriores

Modifica los archivos Markdown o sustituye imágenes dentro de esta carpeta y ejecuta:

`ACTUALIZAR_EGEAWIKI.bat`

El script hace `git pull --rebase`, registra los cambios y los envía a `main`.

## Precaución

No edites simultáneamente la misma página desde Git y Wiki.js. Si vas a trabajar principalmente desde Wiki.js, deja la sincronización bidireccional activada y ejecuta siempre el script de actualización antes y después de cambios locales importantes.
