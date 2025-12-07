# Ghidra for macOS (Apple Silicon)

## Overview

Ghidra is a powerful reverse‑engineering platform from the NSA.  
On Apple Silicon (M1, M2, M3, …) the official releases require a
Java runtime that is not pre‑installed, and setting up a clean
environment can be tedious.

This project bundles a recent **OpenJDK** and **Ghidra** into a single
`Ghidra.app` that behaves like a native macOS application.  
All required resources are isolated inside the bundle, so you can
install the app in your **Applications** folder and run it with a
single click – no additional Java, no `PATH` tricks, no hidden
settings.

---

## Features

| Feature | Description |
|---------|-------------|
| **Self‑contained** | The bundle contains a recent JDK (`openjdk-25`) and the latest version of Ghidra. |
| **Apple‑Silicon optimized** | Runs natively on M1/M2/M3 devices. |
| **No system changes** | The JDK lives inside the app, so your system Java is untouched. |
| **Easy installation** | One command or a pre‑built binary. |
| **User‑friendly UI** | Launch the app from the **Applications** folder with a macOS‑style icon. |
| **Progress bars & ASCII art** | The installer shows a colorful progress bar while downloading and extracting. |

---

## Requirements

- macOS **12.3 or newer** (M1, M2, M3, or later)
- Python **3.6+** (used only for the optional script)
- Internet connection for downloading the JDK and Ghidra

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/sh4tteredd/GhidraMacOS
cd GhidraMacOS
```

### 2. Install the optional Python dependencies

```bash
pip install -r requirements.txt
```

> The installer is pure Python and only needs `colorama`, `tqdm`,
> and `urllib`. If you don’t want to use the script, skip this step.

### 3. Run the installer

```bash
python3 install_ghidra.py
```

The script will:

1. Download the latest OpenJDK and Ghidra releases.
2. Extract them into a temporary folder.
3. Build a `Ghidra.app` bundle with all files in place.
4. Copy the bundle to `/Applications`.

After the script finishes, you can launch Ghidra by double‑clicking
the icon in the **Applications** folder.

---

## Using a Pre‑built Release

If you prefer not to run the Python script, download the latest
pre‑built `.app` from the **Releases** page:

- <https://github.com/ytisf/GhidraMacOS/releases>

Drop the downloaded `Ghidra.app` into the **Applications** folder
and launch it as you would any other macOS app.

---

## Building the Installer Yourself

The installer is created with **PyInstaller**.  
If you want to build a custom version (e.g., different JDK or Ghidra
release), clone the repo and run:

```bash
pyinstaller launcher.spec
```

The `launcher.spec` file bundles the installer script and the icon
into a single executable.  Adjust the spec file to change the
download URLs or add additional resources.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Installer fails with `Permission denied` | The temporary directory is not writable | Run the script with `sudo` or change the temp directory path |
| Ghidra opens but crashes | Java version mismatch | Make sure the JDK in the bundle matches the Ghidra release |
| Missing icon | Icon not bundled | Verify the `icon.icns` is present in `Ghidra.app/Contents/Resources/` |
| `python3: command not found` | Python not installed | Install Python 3.6+ from <https://www.python.org> or via Homebrew: `brew install python` |

---

## License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- **National Security Agency (NSA)** – [Ghidra](https://github.com/NationalSecurityAgency/ghidra) reverse‑engineering platform  
- **Ryan Kurtz** – Ghidra logo [(Apache License 2.0)](https://commons.wikimedia.org/wiki/File:Ghidra_logo.svg).
- **AppleScript template** – inspired by yifanlu’s AppleScript work  
- **PyInstaller** – packaging Python scripts into macOS apps

---

## Contributing

Feel free to open issues or submit pull requests.  
Pull requests that:

- improve the installer script,
- add support for newer Ghidra releases,
- or add additional platforms (e.g., Windows/Mac ARM)  
are welcome.

---
