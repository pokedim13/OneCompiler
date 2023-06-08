from httpx import Client
from onecompiler.base_models import BaseCompiler
from onecompiler.pydantic_models import Response


class ToLang:
    """Wrapper wrapper, for requests, programming languages type, when the request is known"""
    def __init__(self, compiler) -> None:
        self.compiler: Compiler = compiler

    def __getattr__(self, lang: str):
        def func(code: str) -> Response:
            if lang in self.compiler.programming_langs:
                return self.compiler.compiler(lang, code)
        return func

class QueryLang:
    """Wrapper wrapper, for requests, database languages type, when the request is known"""
    def __init__(self, compiler) -> None:
        self.compiler = compiler

    def __getattr__(self, lang: str):
        def func(code: str) -> Response:
            if lang in self.compiler.query_langs:
                return self.compiler.compiler(lang, code)
        return func

class Compiler(BaseCompiler):
    """Synchronous compiler execution"""
    def __init__(self) -> None:
        super().__init__()

        self._client = Client()
        self.to = ToLang(self)
        self.query = QueryLang(self)

    def compiler(self, lang: str, code: str) -> Response:
        """
        compiles your code

        Args:
            lang (str): Programing language
            code (str): Сode that will be sent for compilation

        Returns:
            Response: Pydantic model
        """
        lang_data = self._get_lang_data(lang, code)        
        res = self._client.post(self._url, json=lang_data.dict(), headers=self._headers).json()
        return Response.parse_obj(res)
    