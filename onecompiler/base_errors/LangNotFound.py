class LangNotFound(Exception):
    """Базовый класс для других исключений"""
    def __init__(self, message: str = "Langueges not found from data.keys()") -> None:
        super().__init__(message)