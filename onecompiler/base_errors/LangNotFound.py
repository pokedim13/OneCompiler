class LangNotFound(Exception):
    """Базовый класс для других исключений"""
    def __init__(self, message: str = "Langueges not found from Compiler.all_languages") -> None:
        super().__init__(message)