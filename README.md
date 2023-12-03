# Simple-RPGMV-Mod-Script

## Mod Installer

A RPGMV mod script helps you install mods quickly, and is recommended to be used with git.

### Download

[See the latest release](https://github.com/Sakieye/Simple-RPGMV-Mod-Script/releases)

### How to use

1. Before using this script, it is recommended that you make a copy of the game files just in case, or use the script
   with [**git**](https://git-scm.com/). If you have many mods, it is highly recommended to use git for version control.
2. Click `mod_installer.exe` and enter a rpgmv game path, e.g. `D:/A_RPGMV_GAME`
3. Enter the number of mods you wish to install, e.g. `3`
4. Enter the path of the mod you want to install in order, e.g.

   ```
   D:/A_RPGMV_GAME_MOD1
   D:/A_RPGMV_GAME_MOD2
   D:/A_RPGMV_GAME_MOD3
   ```

5. Enter whether you want to overwrite save files, e.g. `Y`
6. Wait patiently for the copy to finish

### How to run with Python (for developer)

Execute `python -m 'mod_installer.src.main'` in project root

### How to create the executable file (for developer)

1. You must have Python 3.10 or above installed. You can check the version with `python -V`.
2. Installation dependencies from requirements.txt `pip install -r requirements.txt`
3. Run `pyinstaller -F mod_installer/src/main.py -n mod_installer.exe`

## File diff

A script that finds and compares two folder files.

### Download

[See the latest release](https://github.com/Sakieye/Simple-RPGMV-Mod-Script/releases)

### How to use

1. Click `file_diff.exe`
2. Enter the source directory, e.g. `D:/A_RPGMV_GAME_1.0`
3. Enter the target directory, e.g. `D:/A_RPGMV_GAME_1.1`
4. Wait patiently for the result of the comparison, finally a message "please press any key to exit the program" will be
   printed, if you want to interrupt earlier, please press ctrl+C.

### How to run with Python (for developer)

Execute `python -m 'file_diff.src.main'` in project root

### How to create the executable file (for developer)

1. You must have Python 3 installed. You can check the version with `python -V`.
2. Run `pyinstaller -F file_diff/src/main.py -n file_diff.exe`