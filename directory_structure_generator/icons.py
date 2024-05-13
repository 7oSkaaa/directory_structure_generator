class Icons:
    error: str = "❌"
    success: str = "✅"
    warning: str = "⚠️"
    info: str = "ℹ️"
    question: str = "❓"
    loading: str = "⏳"
    done: str = "🎉"
    exit: str = "👋"
    search: str = "🔍"
    settings: str = "⚙️"
    home: str = "🏠"
    folder: str = "📁"
    file: str = "📄"
    trash: str = "🗑️"

    @staticmethod
    def get_icon(icon):
        return getattr(Icons, icon)

    @staticmethod
    def get_all_icons():
        return [
            icon
            for icon in dir(Icons)
            if not icon.startswith("__") and not callable(getattr(Icons, icon))
        ]

    @staticmethod
    def print_all_icons():
        for icon in Icons.get_all_icons():
            print(f"{getattr(Icons, icon)}{icon}")
