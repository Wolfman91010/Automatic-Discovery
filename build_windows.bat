@echo off
python -m pip install -r requirements.txt
python -m PyInstaller --onefile --windowed --name Cosmic-Oracle cosmic_oracle_app.py
if exist dist\Cosmic-Oracle.exe (
  echo.
  echo Windows app created: dist\Cosmic-Oracle.exe
) else (
  echo.
  echo Build failed. Check Python and PyInstaller installation.
)
pause
