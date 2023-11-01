import subprocess

def execute_command_in_kali(command):
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Command failed with error code {e.returncode}: {e.stderr}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
