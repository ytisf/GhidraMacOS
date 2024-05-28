# Ghidra OSX Installer

This script automates the process of installing Ghidra as a self-contained OSX `.app` without contaminating your system with a separate Java installation. It is specifically designed for ARM64 architecture, making it suitable for Apple's M1, M2, M3, and other ARM-based Macs.

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

## Acknowledgements

- Special thanks to [yifanlu](https://gist.github.com/yifanlu/e9965cdb148b550335e57899f790cad2) for providing the AppleScript template used in this script & the inspiration.
- Of course - [Ghidra](https://github.com/NationalSecurityAgency/ghidra).

## License

This project is licensed under the MIT License.
