; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Don Juan & Dragon"
#define MyAppVersion "0.1"
#define MyAppPublisher "Faurie Thibaud/Derouet Lucien"
#define MyAppExeName "main.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{AE51B989-BEAA-491E-92B3-180A0B8EF425}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={pf}\{#MyAppName}
DisableProgramGroupPage=yes
InfoAfterFile=C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\patch_note_v0.1.txt
OutputDir=C:\Users\Thibaud\Desktop
OutputBaseFilename=DJ&D_setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "french"; MessagesFile: "compiler:Languages\French.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\_bz2.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\_ctypes.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\_hashlib.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\_lzma.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\_multiprocessing.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\_socket.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\_ssl.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\libfreetype-6.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\libgcc_s_sjlj-1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\libjpeg-8.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\libmpg123-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\libogg-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\libpng16-16.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\library.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\libtiff-5.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\libvorbis-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\libvorbisfile-3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\libwebp-5.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pyexpat.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame._freetype.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.base.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.bufferproxy.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.cdrom.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.color.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.constants.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.display.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.draw.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.event.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.fastevent.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.font.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.image.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.imageext.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.joystick.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.key.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.mask.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.math.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.mixer.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.mixer_music.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.mouse.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.overlay.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.pixelarray.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.pixelcopy.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.rect.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.rwobject.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.scrap.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.surface.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.surflock.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.time.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\pygame.transform.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\python34.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\SDL.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\SDL_image.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\SDL_mixer.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\SDL_ttf.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\select.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\zlib1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Thibaud\Downloads\PYTHON\Programme\DJ&D\img\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

