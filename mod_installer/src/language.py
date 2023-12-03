import json
import os
import sys
from enum import Enum
import locale


class Locale(Enum):
    UNKNOWN, EN, ZH_TW = range(3)

    def __str__(self):
        return str(self.name)


class Lang:

    def __init__(self, language_pack=None, loc=Locale.UNKNOWN):
        self.language_pack = language_pack
        self.loc = loc
        if not self.language_pack:
            self.language_pack = {
                "EN": {
                    "welcome": "Welcome to the simple RPGMV mod installation script, this script can compare the "
                               "folder structure of the mod and the game, and quickly install the mod, "
                               "it is recommended to use with git, in order to achieve better mod management effect. "
                               "You can press ctrl+C (Windows) to exit the program.\n",
                    "input_game_folder": "Please input the game folder, which contains the www, locales and "
                                         "swiftshader folders: ",
                    "game_folder_selected": "Game folder selected: ",
                    "input_install_mod_number": "Please enter the number of mods you wish to install: ",
                    "input_install_mods": "Please enter the mods path in the desired order of installation, with each "
                                          "mod separated by a line break: ",
                    "mod_eq_game_error": "The mod folder cannot be the same as the game folder.",
                    "installing_mod": "Installing mod '{mod}', total {total_files} files...",
                    "mod_install_progress": "Progress: {count}/{total_files} files ({progress}%)",
                    "mod_install_success": "installed successfully!",
                    "save_copy": "Copy '{file}' to '{dest_path}'",
                    "illegal_dir": "is not a directory.",
                    "cannot_find": "cannot find '{file}' under '{root}'.",
                    "overwrite_save": "Whether to overwrite save files (rpgsave files must exist in the mod folder, "
                                      "Y/N, default is N): ",
                    "fin": "All mods installed, press any key to exit program.",
                    "fin_error": "An error has occurred. Press any key to exit the program."
                },
                "ZH_TW": {
                    "welcome": "歡迎使用簡易RPGMV Mod安裝腳本，此腳本能比對mod與遊戲的資料夾結構，快速安裝mod，建議搭配git一起使用，以達到更好的mod管理效果。你可以按下ctrl+C"
                               "（Windows）以離開程序。\n",
                    "input_game_folder": "請輸入遊戲資料夾，遊戲資料夾包含www、locales及swiftshader資料夾： ",
                    "game_folder_selected": "已輸入遊戲資料夾： ",
                    "input_install_mod_number": "請輸入希望安裝的mod數量： ",
                    "input_install_mods": "請按照希望的安裝順序輸入mod路徑，每個mod以換行符號分隔： ",
                    "mod_eq_game_error": "mod資料夾不能與遊戲資料夾一樣。",
                    "installing_mod": "正在安裝 mod '{mod}'， 總共 {total_files} 個檔案...",
                    "mod_install_progress": "進度： {count}/{total_files} 個檔案 ({progress}%)",
                    "mod_install_success": "安裝成功!",
                    "save_copy": "複製 '{file}' 至 '{dest_path}'",
                    "illegal_dir": "不是一個資料夾。",
                    "cannot_find": "在 '{root}' 之下找不到 '{file}'。",
                    "overwrite_save": "是否覆蓋存檔（rpgsave檔案必須存在mod資料夾下，Y/N，預設為N）： ",
                    "fin": "所有mod安裝完成，按任一按鍵退出程序。",
                    "fin_error": "發生錯誤，請按任一鍵退出程序。"
                }
            }
        if self.loc == Locale.UNKNOWN:
            loc_str = locale.getdefaultlocale()[0].upper()
            if "ZH_TW" in loc_str:
                self.loc = Locale.ZH_TW
            else:
                self.loc = Locale.EN

    def get(self, key: str) -> str:
        return self.language_pack[str(self.loc)][key]

    def get_and_replace(self, key: str, replace_dict: dict[str:str]) -> str:
        res = self.language_pack[str(self.loc)][key]
        for keyword, substitution in replace_dict.items():
            keyword = "{" + keyword + "}"
            res = res.replace(keyword, str(substitution), 1)
        return res
