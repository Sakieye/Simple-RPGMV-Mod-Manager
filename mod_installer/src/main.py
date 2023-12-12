import traceback

from mod_installer.src.file_service import FileService
from mod_installer.src.language import Lang

if __name__ == '__main__':
    lang = Lang()
    try:
        fs = FileService(lang)
        # 1. input the game folder
        print(lang.get("welcome"))
        game_folder = fs.dir_abspath(input(lang.get("input_game_folder")))
        game_www = fs.find('www', game_folder, True)  # check www is located in the first layer of the game folder
        print(lang.get("game_folder_selected"), game_folder, "\n")
        # 2. input mods
        n = int(input(lang.get("input_install_mod_number")))
        print("\n" + lang.get("input_install_mods"))
        mods = [""] * n
        for i in range(n):
            mod = input().strip()
            if mod:
                mod = fs.dir_abspath(mod)
                mod_www = fs.find('www', mod)  # check www is under the mod folder
                if mod_www == game_www:
                    raise RuntimeError(lang.get("mod_eq_game_error"))
                mods[i] = mod
        # 3. overwrite save option
        overwrite_save = input("\n" + lang.get("overwrite_save")).strip().upper() == "Y"
        print("Y" if overwrite_save else "N", "\n")
        # 4. install mods
        for mod in mods:
            fs.copy_mod_files(game_folder, mod)
            if overwrite_save:
                fs.copy_save_files(game_folder, mod)
        input(lang.get("fin"))
    except Exception as e:
        print(traceback.format_exc())
        input(lang.get("fin_error"))
