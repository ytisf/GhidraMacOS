import os
import shutil
import subprocess
import urllib.request
import zipfile
import tarfile
from colorama import Fore, Style, init
from tqdm import tqdm

# Initialize colorama
init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.MAGENTA}
  _____                _____ _
 / ____|              / ____| |
| (___  _ __ ___  ___| (___ | | ___
 \\___ \\| '__/ _ \\/ _ \\\\___ \\| |/ _ \\
 ____) | | |  __/  __/____) | |  __/
|_____/|_|  \\___|\\___|_____/|_|\\___|

{Fore.CYAN}
    .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.
   (_  )   (_  )   (_  )   (_  )   (_  )   (_  )   (_  )   (_  )   (_  )
     /       /       /       /       /       /       /       /       /
    (       (       (       (       (       (       (       (       (
     `-'     `-'     `-'     `-'     `-'     `-'     `-'     `-'     `-'
{Style.RESET_ALL}
"""
    print(banner)

# URLs
java_url = "https://download.java.net/java/GA/jdk22.0.1/c7ec1332f7bb44aeba2eb341ae18aca4/8/GPL/openjdk-22.0.1_macos-aarch64_bin.tar.gz"
ghidra_url = "https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_11.0.3_build/ghidra_11.0.3_PUBLIC_20240410.zip"

# Paths
cwd = os.getcwd()
temp_dir = os.path.join(cwd, "ghidra_install")
applet_path = os.path.join(temp_dir, "Ghidra-OSX-Launcher-Script.scpt")
app_dir = os.path.join(temp_dir, "Ghidra.app")
jdk_dir = os.path.join(temp_dir, "jdk")
ghidra_dir = os.path.join(temp_dir, "ghidra")
applications_dir = "/Applications"

# Names
launch_script_path = os.path.join(temp_dir,'Ghidra.app/Contents/Resources/ghidra/support/launch.sh')
ghidra_run_path = os.path.join(temp_dir, 'Ghidra.app/Contents/Resources/ghidra/ghidraRun')


# Create temporary directory
os.makedirs(temp_dir, exist_ok=True)


def add_execute_permissions(file_path):
    try:
        subprocess.run(["chmod", "+x", file_path], check=True)
        print(f"{Fore.GREEN}Added execute permissions to {file_path}{Style.RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error adding execute permissions to {file_path}: {e}{Style.RESET_ALL}")
        raise

def download_file(url, dest):
    if os.path.exists(dest):
        print(f"{Fore.YELLOW}{dest} already exists, skipping download{Style.RESET_ALL}")
        return
    try:
        print(f"{Fore.YELLOW}Downloading {url} to {dest}{Style.RESET_ALL}")

        with tqdm(unit='B', unit_scale=True, miniters=1, desc=url.split('/')[-1]) as t:
            def reporthook(blocknum, blocksize, totalsize):
                t.total = totalsize
                t.update(blocknum * blocksize - t.n)

            urllib.request.urlretrieve(url, dest, reporthook)
    except Exception as e:
        print(f"{Fore.RED}Error downloading {url}: {e}{Style.RESET_ALL}")
        raise

def extract_zip(file_path, dest_dir):
    try:
        print(f"{Fore.YELLOW}Extracting {file_path} to {dest_dir}{Style.RESET_ALL}")
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(dest_dir)
    except Exception as e:
        print(f"{Fore.RED}Error extracting {file_path}: {e}{Style.RESET_ALL}")
        raise

def extract_tar_gz(file_path, dest_dir):
    try:
        print(f"{Fore.YELLOW}Extracting {file_path} to {dest_dir}{Style.RESET_ALL}")
        with tarfile.open(file_path, 'r:gz') as tar_ref:
            tar_ref.extractall(dest_dir)
    except Exception as e:
        print(f"{Fore.RED}Error extracting {file_path}: {e}{Style.RESET_ALL}")
        raise

def main():
    try:
        # Create Ghidra.app as an empty directory first.
        subprocess.run(["osacompile", "-o", app_dir, applet_path], check=True)
        print(f"{Fore.GREEN}Created Ghidra.app at {app_dir}{Style.RESET_ALL}")

        # Step 2: Download and extract the latest OpenJDK
        jdk_tar_path = os.path.join(temp_dir, "openjdk.tar.gz")
        download_file(java_url, jdk_tar_path)
        extract_tar_gz(jdk_tar_path, jdk_dir)
        jdk_extracted_dir = os.path.join(jdk_dir, os.listdir(jdk_dir)[0])
        # Place JDK in the correct location within the app bundle
        jdk_final_app_dir = os.path.join(app_dir, "Contents", "Resources", "jdk")
        shutil.copytree(jdk_extracted_dir, jdk_final_app_dir)

    except Exception as e:
        print(f"{Fore.RED}Installation failed: {e}{Style.RESET_ALL}")
        exit()

    try:
        # Step 3: Download and extract the latest Ghidra
        ghidra_zip_path = os.path.join(temp_dir, "ghidra.zip")
        download_file(ghidra_url, ghidra_zip_path)
        extract_zip(ghidra_zip_path, ghidra_dir)
        ghidra_extracted_dir = os.path.join(ghidra_dir, os.listdir(ghidra_dir)[0])
        # Place Ghidra in the correct location within the app bundle
        ghidra_final_app_dir = os.path.join(app_dir, "Contents", "Resources", "ghidra")
        shutil.copytree(ghidra_extracted_dir, ghidra_final_app_dir)

        # Step 5: Add execute permissions to the Ghidra launcher script
        add_execute_permissions(launch_script_path)
        add_execute_permissions(ghidra_run_path)

        print(f"{Fore.GREEN}Ghidra installation completed successfully!{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}Installation failed: {e}{Style.RESET_ALL}")
        exit()

if __name__ == "__main__":
    print_banner()
    main()