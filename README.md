# Ghidra OSX Installer

This script automates the process of installing Ghidra as a self-contained OSX `.app` without contaminating your system with a separate Java installation. It is specifically designed for ARM64 architecture, making it suitable for Apple's M1, M2, M3, and other ARM-based Macs.

*notice the script will NOT copy Ghidra to your Applications directory if you run it from the command line. You can either run it from the terminal or copy the script to your Applications directory and run it from there.* 

## Requirements

- macOS running on ARM64 architecture (M1, M2, M3, etc.).
- Python 3.6 or later.
- Internet connection for downloading necessary files.


## Features

- Downloads the AppleScript template for the Ghidra launcher.
- Downloads and extracts the latest OpenJDK.
- Downloads and extracts the latest Ghidra.
- Copies the Ghidra `.app` to your Applications directory.
- Provides a colorful ASCII art banner for a fun experience.
- Displays progress bars for downloads.

## Usage

1. Clone this repository:
    ```bash
    git clone https://www.github.com/ytisf/GhidraMacOS
    ```
2. Ensure you have Python 3 installed.
3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the script:

    ```bash
    python3 install_ghidra.py
    ```

5. Enjoy. You should have a `Ghidra.app` in your `/Applications`. 

## Release Package

The released packages are built using PyInstaller. To build the package, you need to have PyInstaller installed. 
They are built for "ease" of installation. Please notice you do need to have Python 3 installed on your system to run the package.

```bash
pyinstaller --onefile --windowed launcher.py --add-data install_ghidra.py:. --add-data requirements.txt:.
```

## Acknowledgements

- Special thanks to [yifanlu](https://gist.github.com/yifanlu/e9965cdb148b550335e57899f790cad2) for providing the AppleScript template used in this script & the inspiration.
- Of course - [Ghidra](https://github.com/NationalSecurityAgency/ghidra).

## License

This project is licensed under the MIT License.
