import os
import sys

from .colors import Colors
from .generator import directory_structure_generator
from .utils import get_args


def main():
    # Get the path to the folder to analyze from the CLI
    try:
        path, language, sort = get_args()

        # Check if the sort argument is a boolean
        sort = True if sort.lower() == "true" else False

        print(f"{Colors.green}The arguments have been provided ✅{Colors.reset}")
    except SystemExit:
        print(f"{Colors.red}The arguments was not provided ❌{Colors.reset}")
        sys.exit(1)

    # Check if the path exists
    if not os.path.exists(path):
        print(f"{Colors.red}The path {path} does not exist. ❌{Colors.reset}")
        sys.exit(1)

    # Generate the folder structure and print it
    directory_structure_generator(path=path, language=language, sort=sort)


if __name__ == "__main__":
    main()
