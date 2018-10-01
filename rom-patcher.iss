#define MyAppName "ROM Patcher"
#define MyAppPublisher "Shane Rice"
#define MyAppURL "https://shane.pw/"
#define MyAppExeName "rom-patcher.exe"
#define AppVersion GetEnv("RELEASE_TAG")

[Setup]
AppId={{7709E5BB-08E2-46AA-BF4E-F899C35E5D53}
AppName={#MyAppName}
AppVersion={#AppVersion}
;AppVerName={#MyAppName} {#AppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
UninstallDisplayIcon={app}\{#MyAppExeName},1

OutputDir=.\dist\
OutputBaseFilename=rom-patcher-installer
SetupIconFile=dist\rom-patcher\icon.ico
Compression=lzma
SolidCompression=yes
DisableProgramGroupPage=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "dist\rom-patcher\rom-patcher.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\rom-patcher\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{commonprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
