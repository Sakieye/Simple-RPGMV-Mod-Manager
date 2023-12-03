import os
import shutil

from mod_installer.src.language import Lang


class FileService:
    def __init__(self, lang: Lang):
        self.lang = lang

    def dir_abspath(self, path: str) -> str:
        if not os.path.isdir(path):
            raise NotADirectoryError(f"'{path}' {self.lang.get('illegal_dir')}")
        return os.path.abspath(path)

    def find(self, f: str, root: str, only_first_layer: bool = False) -> str:
        if only_first_layer and f in os.listdir(root):
            return os.path.join(root, f)
        for path, dirs, files in os.walk(root):
            if f in dirs:
                return os.path.join(path, f)
        raise FileNotFoundError(self.lang.get_and_replace("cannot_find", {"file": f, "root": root}))

    def copy_mod_files(self, game_folder, mod_folder):
        game_www = self.find('www', game_folder, True)
        mod_www = self.find('www', mod_folder)
        mod_files = [os.path.join(root, file) for root, dirs, files in os.walk(mod_www) for file in files]
        total_files = len(mod_files)
        count = 0

        print(self.lang.get_and_replace("installing_mod", {"mod": mod_folder, "total_files": total_files}))

        for file in mod_files:
            dest_path = file.replace(mod_www, game_www)
            dest_dir = os.path.dirname(dest_path)
            os.makedirs(dest_dir, exist_ok=True)  # if the destination directory doesn't exist, create it
            shutil.copy(file, dest_path)  # overwrite if it exists

            count += 1
            progress = count / total_files * 100
            print(self.lang.get_and_replace("mod_install_progress",
                                            {
                                                "count": count,
                                                "total_files": total_files,
                                                "progress": f"{progress:.2f}"
                                            }),
                  end='\r')
        print(f"'{mod_folder}' {self.lang.get('mod_install_success')}\n")

    def copy_save_files(self, game_folder, mod_folder):
        game_www = self.find('www', game_folder, True)
        game_save_folder = os.path.join(game_www, 'save')
        for root, dirs, files in os.walk(mod_folder):
            for file in files:
                if file.endswith('.rpgsave'):
                    src_path = os.path.join(root, file)
                    dest_path = os.path.join(game_save_folder, file)
                    dest_dir = os.path.dirname(dest_path)
                    print(self.lang.get_and_replace("save_copy", {"file": file, "dest_path": dest_path}))
                    os.makedirs(dest_dir, exist_ok=True)
                    shutil.copy(src_path, dest_path)
