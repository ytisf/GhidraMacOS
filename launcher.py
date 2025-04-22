import subprocess
import os

# Assuming install_ghidra.py is in the same directory within the .app
script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "install_ghidra.py")

try:
    subprocess.run(["python3", script_path], check=True)
    # Optionally display a success message
except subprocess.CalledProcessError as e:
    # Optionally display an error message
    print(f"Error during installation: {e}")
except FileNotFoundError:
    print(f"Error: {script_path} not found.")
