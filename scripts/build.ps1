$py_name = "rom-patcher-gui.py"
$spec_name = $($args[0])

$ErrorActionPreference = "Stop"

if ( ! $spec_name ) { $spec_name = "main.spec" }

if (!( Test-Path -Path ".\$spec_name" )) {Throw "Unable to stat spec file: $spec_name"}

if (!( Test-Path -Path ".\$py_name" )) {Throw "You are in the wrong directory..."}
if (!( Test-Path -Path ".\bin" )) {Throw "You do not have the required bin directory..."}

if (( Test-Path -Path ".\build" )) {Remove-Item ".\build" -Recurse -Force}
if (( Test-Path -Path ".\dist" )) {Remove-Item ".\dist" -Recurse -Force}
if (( Test-Path -Path ".\__pycache__" )) {Remove-Item ".\__pycache__" -Recurse -Force}

pyinstaller.exe --clean ".\$spec_name"
if ( ! $lastExitCode -eq 0 ) { Throw "Error running pyinstaller.exe" }
