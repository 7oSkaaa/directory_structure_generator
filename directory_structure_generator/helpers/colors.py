class colors:
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
        return getattr(colors, color)
    
    @staticmethod
    def get_all_colors():
        return [color for color in dir(colors) if not color.startswith("__") and not callable(getattr(colors, color))]
    
    @staticmethod
    def print_all_colors():
        for color in colors.get_all_colors():
            print(f"{getattr(colors, color)}{color}{colors.reset}")