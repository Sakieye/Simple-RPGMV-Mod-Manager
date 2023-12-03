import filecmp
import os
import traceback

if __name__ == '__main__':
    try:
        source_dir = input("Please enter the path of the source directory: ")
        target_dir = input("Please enter the path of the target directory: ")

        source_dir = os.path.abspath(source_dir)
        target_dir = os.path.abspath(target_dir)

        comparison = filecmp.dircmp(source_dir, target_dir)


        def report_diff(dcmp):
            for name in dcmp.diff_files:
                print(f"Different file found: {os.path.join(dcmp.left, name)}")
            for name in dcmp.left_only:
                print(f"File or directory only in {source_dir}: {os.path.join(dcmp.left, name)}")
            for name in dcmp.right_only:
                print(f"File or directory only in {target_dir}: {os.path.join(dcmp.right, name)}")
            for sub_dcmp in dcmp.subdirs.values():
                report_diff(sub_dcmp)


        report_diff(comparison)
        input("Comparison finish, please press any key to exit the program.")
    except Exception as e:
        print(traceback.format_exc())
        input("An error has occurred. Press any key to exit the program.")
