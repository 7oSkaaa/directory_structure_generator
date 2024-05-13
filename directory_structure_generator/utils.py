import argparse
import os

from .colors import Colors
from .icons import Icons


def get_from_file(file_name):
    with open(file_name, "r") as file:
        return file.read().splitlines()


def save_to_file(file_name, data):
    with open(file_name, "w") as file:
        for line in data:
            file.write(line + "\n")


def add_headers(file_name, structure, language):
    structure.insert(0, f"# {file_name} folder structure\n")
    structure.insert(1, f"```{language}")
    structure.insert(2, f"{Icons.folder} {file_name}")


def add_footers(structure):
    structure.append(f"```")


def get_max_column_length(structure):
    max_length = 0
    for line in structure:
        if len(line) > max_length:
            max_length = len(line)
    return max_length


def remove_extras(structure):
    reversed_structure = structure[::-1]
    max_column_width = get_max_column_length(structure)
    for column in range(max_column_width):
        for line in reversed_structure:
            line_list = list(line)
            # if the current column is empty, skip it
            if column >= len(line_list):
                continue

            # make sure the line is not the last one
            if line_list[column] != "│":
                break
            else:
                line_list[column] = " "

            # update the line
            reversed_structure[reversed_structure.index(line)] = "".join(line_list)

    return reversed_structure[::-1]


def get_args():
    parser = argparse.ArgumentParser(
        description="Generate a folder structure from a given path."
    )
    parser.add_argument(
        "--path",
        dest="path",
        default=os.getcwd(),
        help="The path to the folder to analyze.",
        required=False,
    )
    parser.add_argument(
        "--language",
        dest="language",
        default="plaintext",
        help="The language to use for the folder structure.",
        required=False,
    )
    parser.add_argument(
        "--sort",
        dest="sort",
        default="False",
        help="Sort the directories and files alphabetically.",
        required=False,
    )
    print(f"{Colors.yellow}{Icons.loading} Parsing the arguments...{Colors.reset}")
    args = parser.parse_args()  # Parse the arguments

    return args.path, args.language, args.sort
