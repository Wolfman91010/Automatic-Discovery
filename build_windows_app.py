#!/usr/bin/env python3
import platform
import subprocess
import sys


def ensure_pyinstaller():
    try:
        import PyInstaller  # noqa: F401
        return True
    except ImportError:
        print("PyInstaller is not installed. Installing requirements...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=False,
        )
        if result.returncode != 0:
            return False
        return True


def main():
    if platform.system() != "Windows":
        print(
            "This packaging script is intended for Windows because it produces a .exe. "
            f"Current platform: {platform.system()}.",
            file=sys.stderr,
        )
        print("On Windows, run: py -3 build_windows_app.py", file=sys.stderr)
        return 1

    if not ensure_pyinstaller():
        print("Unable to install PyInstaller. Aborting build.", file=sys.stderr)
        return 1

    command = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconsole",
        "--onefile",
        "--name=CosmicOracle",
        "cosmic_oracle_app.py",
    ]

    print("Building Cosmic Oracle Windows Executable...")
    result = subprocess.run(command, check=False)
    if result.returncode == 0:
        print("\n[SUCCESS] Build complete! Check the 'dist' folder for CosmicOracle.exe")
        return 0

    print("\n[ERROR] PyInstaller build failed.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
