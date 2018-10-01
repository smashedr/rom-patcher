$directory = "gui"
Get-ChildItem "$directory" -Filter *.ui |
    Foreach-Object {
        $name = $_.BaseName
        pyuic5.exe $_.FullName | Out-File -Encoding UTF8 ".\$directory\$name.py"
    }
