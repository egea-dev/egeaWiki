param(
  [string]$Mensaje = "Actualizar manual SIMGEST"
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not (Test-Path ".git")) {
  throw "Esta carpeta todavía no está inicializada. Ejecuta primero SUBIR_A_EGEAWIKI.bat."
}

git pull --rebase origin main
git add -A
$changes = git status --porcelain
if ($changes) {
  git commit -m $Mensaje
  git push origin main
  Write-Host "Actualización enviada correctamente."
} else {
  Write-Host "No hay cambios nuevos que subir."
}
