from httpx import Client
from onecompiler.base_models import BaseCompiler
from onecompiler.pydantic_models import Response
from onecompiler.base_errors import LangNotFound
from onecompiler import data


class ToLang:
    """Wrapper wrapper, for requests, programming languages type, when the request is known"""
    def __init__(self, compiler, lang_type: str) -> None:
        self.compiler: Compiler = compiler
        self.lang_type = lang_type

    def __getattr__(self, lang: str):
        def func(code: str) -> Response:
            _, lang_type = self.compiler._get_full_lang_name(lang)
            
            if lang_type is None:
                raise LangNotFound
            
            if lang_type == self.lang_type:
                return self.compiler.compile(lang, code)
        return func


class Compiler(BaseCompiler):
    """Synchronous compiler execution"""
    def __init__(self) -> None:
        super().__init__()

        self._client = Client()
        self.to = ToLang(self, 'programming')
        self.query = ToLang(self, 'query')


    def compile(self, lang: str, code: str) -> Response:
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
    