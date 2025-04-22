from setuptools import setup

APP = ['launcher.py']
DATA_FILES = ['install_ghidra.py', 'requirements.txt']  # Include your script and requirements
OPTIONS = {
    'argv_emulation': True,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)