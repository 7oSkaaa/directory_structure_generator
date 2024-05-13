import sys

from .utils import *

structure = []

FINAL_PATH = "├───"
FINAL_PATH_DOWN = "└───"
FINAL_PATH_UP = "───"
PATH = "│   "
EMPTY = "    "


def build_structure(path, exclude_dirs, degree, ends, sort=False):
    # Get the list of directories and files in the path
    try:
        dirs = os.listdir(path)
    except PermissionError:
        print(f"{Colors.red}Permission denied for {path} ❌{Colors.reset}")
        exit(1)

    # Remove the directories to exclude
    dirs = [d for d in dirs if d.lower() not in exclude_dirs]

    # Sort the directories and files alphabetically
    if sort:
        dirs.sort()

    # Create the path to add
    to_add = PATH * degree

    # add the files to the structure
    for i, f in enumerate(dirs):
        icon = Icons.file if os.path.isfile(os.path.join(path, f)) else Icons.folder
        if i == len(dirs) - 1:
            structure.append(f"{to_add}{FINAL_PATH_DOWN}{icon} {f}")
        else:
            structure.append(f"{to_add}{FINAL_PATH}{icon} {f}")

        # check if the file is a directory
        if os.path.isdir(os.path.join(path, f)):
            # do a recursive call to build the structure
            build_structure(
                path=os.path.join(path, f),
                exclude_dirs=exclude_dirs,
                degree=degree + 1,
                ends=ends + (i == len(dirs) - 1),
                sort=sort,
            )


def folder_structure(path, exclude_dirs, sort=False):
    # Build the folder structure
    build_structure(path=path, exclude_dirs=exclude_dirs, degree=0, ends=0, sort=sort)

    return structure


def directory_structure_generator(
    path=None, exclude_dirs=None, language=None, sort=False
):
    # starting the program
    print(f"{Colors.yellow}{Icons.loading} Starting the program...{Colors.reset}")

    global structure

    # Create the folder structure
    structure = folder_structure(path=path, exclude_dirs=exclude_dirs, sort=sort)

    # Remove the extras
    structure = remove_extras(structure)

    # Print the folder structure
    add_headers(
        file_name=os.path.basename(path), language=language, structure=structure
    )
    add_footers(structure)

    save_to_file(f"{path}/Structures.md", structure)

    print(
        f"{Colors.green}The folder structure has been saved to Structures.md ✅{Colors.reset}"
    )
