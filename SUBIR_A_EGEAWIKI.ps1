param(
  [string]$Mensaje = "Cargar manual SIMGEST en Wiki.js"
)

$ErrorActionPreference = "Stop"
$RepoUrl = "https://github.com/egea-dev/egeaWiki.git"
$Branch = "main"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
  throw "Git no está instalado. Instala Git for Windows y vuelve a ejecutar este archivo."
}

Set-Location $PSScriptRoot

$markdown = Get-ChildItem -Path "$PSScriptRoot\simgest" -Recurse -Filter "*.md" -ErrorAction Stop
$imagenes = Get-ChildItem -Path "$PSScriptRoot\assets\simgest" -Recurse -Include "*.png","*.jpg","*.jpeg","*.webp" -ErrorAction Stop

if ($markdown.Count -lt 20) {
  throw "El paquete parece incompleto: solo se encontraron $($markdown.Count) páginas Markdown."
}
if ($imagenes.Count -lt 30) {
  throw "El paquete parece incompleto: solo se encontraron $($imagenes.Count) imágenes."
}

if (-not (Test-Path ".git")) {
  git init
  git branch -M $Branch
}

$currentRemote = git remote get-url origin 2>$null
if ($LASTEXITCODE -eq 0) {
  git remote set-url origin $RepoUrl
} else {
  git remote add origin $RepoUrl
}

# El repositorio remoto está vacío en la primera carga. En cargas posteriores,
# trae primero los cambios que haya podido escribir Wiki.js.
git ls-remote --exit-code origin $Branch *> $null
if ($LASTEXITCODE -eq 0) {
  git pull --rebase origin $Branch
}

# Configura identidad local si aún no existe.
$userName = git config user.name
if (-not $userName) { git config user.name "egea-dev" }
$userEmail = git config user.email
if (-not $userEmail) { git config user.email "egea-dev@users.noreply.github.com" }

git add -A
$changes = git status --porcelain
if ($changes) {
  git commit -m $Mensaje
} else {
  Write-Host "No hay cambios nuevos que subir."
}

git push -u origin $Branch
Write-Host ""
Write-Host "Carga terminada: https://github.com/egea-dev/egeaWiki"
Write-Host "Ahora ejecuta Import Everything en Administracion > Almacenamiento > Git de Wiki.js."
