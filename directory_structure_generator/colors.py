class Colors:
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"
    reset = "\033[0m"

    @staticmethod
    def get_color(color):
        return getattr(Colors, color)

    @staticmethod
    def get_all_colors():
        return [
            color
            for color in dir(Colors)
            if not color.startswith("__") and not callable(getattr(Colors, color))
        ]

    @staticmethod
    def print_all_colors():
        for color in Colors.get_all_colors():
            print(f"{getattr(Colors, color)}{color}{Colors.reset}")
