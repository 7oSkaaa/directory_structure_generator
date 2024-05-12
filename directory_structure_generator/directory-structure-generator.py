import argparse
import os
import sys

from helpers.colors import colors
from helpers.icons import Icons
from helpers.utils import *

structure = []
is_sorted = False

FINAL_PATH = "├───"
FINAL_PATH_DOWN = "└───"
FINAL_PATH_UP = "───"
PATH = "│   "
EMPTY = "    "


def build_structure(path, exclude_dirs, degree, ends):
    # Get the list of directories and files in the path
    try:
        dirs = os.listdir(path)
    except PermissionError:
        print(f"{colors.red}Permission denied for {path} ❌{colors.reset}")
        exit(1)

    # Remove the directories to exclude
    dirs = [d for d in dirs if d not in exclude_dirs]

    # Sort the directories and files alphabetically
    if is_sorted:
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
            )


def folder_structure(path, exclude_dirs):
    # Build the folder structure
    build_structure(path=path, exclude_dirs=exclude_dirs, degree=0, ends=0)

    return structure


def get_args():
    parser = argparse.ArgumentParser(
        description="Generate a folder structure from a given path."
    )
    parser.add_argument(
        "--path",
        dest="path",
        default=os.getcwd(),
        help="The path to the folder to analyze.",
        required=False
    )
    parser.add_argument(
        "--language",
        dest="language",
        default="plaintext",
        help="The language to use for the folder structure.",
        required=False
    )
    parser.add_argument(
        "--sort",
        dest="sort",
        default='False',
        help="Sort the directories and files alphabetically.",
        required=False
    )
    print(f"{colors.yellow}{Icons.loading} Parsing the arguments...{colors.reset}")
    args = parser.parse_args()  # Parse the arguments

    return args.path, args.language, args.sort


def directory_structure_generator():
    # starting the program
    print(f"{colors.yellow}{Icons.loading} Starting the program...{colors.reset}")

    try:
        # Get the directories to exclude
        exclude_dirs = get_from_file("exclude_dirs.txt")
    except FileNotFoundError:
        print(f"{colors.red}The file exclude_dirs.txt was not found ❌{colors.reset}")
        sys.exit(1)

    # Get the path to the folder to analyze from the CLI
    try:
        path, language, sort = get_args()

        # Check if the sort argument is a boolean
        if sort.lower() == "true":
            global is_sorted
            is_sorted = True

        print(f"{colors.green}The arguments have been provided ✅{colors.reset}")
    except SystemExit:
        print(f"{colors.red}The arguments was not provided ❌{colors.reset}")
        sys.exit(1)

    # Check if the path exists
    if not os.path.exists(path):
        print(f"{colors.red}The path {path} does not exist. ❌{colors.reset}")
        sys.exit(1)

    global structure

    # Create the folder structure
    structure = folder_structure(path=path, exclude_dirs=exclude_dirs)

    # Remove the extras
    structure = remove_extras(structure)

    # Print the folder structure
    add_headers(
        file_name=os.path.basename(path), language=language, structure=structure
    )
    add_footers(structure)

    save_to_file("Structures.md", structure)

    print(
        f"{colors.green}The folder structure has been saved to Structures.md ✅{colors.reset}"
    )


if __name__ == "__main__":
    directory_structure_generator()
