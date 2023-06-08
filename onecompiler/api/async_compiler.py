from typing import Coroutine, Any
from httpx import AsyncClient
from onecompiler.base_models import BaseCompiler
from onecompiler.pydantic_models import Response


class ToLang:
    """Wrapper wrapper, for requests, programming languages type, when the request is known"""
    def __init__(self, compiler) -> None:
        self.compiler = compiler

    def __getattr__(self, lang: str):
        async def func(code: str) -> Coroutine[Any, Any, Response]:
            return await self.compiler.compiler(lang, code) 
        return func
	
class QueryLang:
    """Wrapper wrapper, for requests, database languages type, when the request is known"""
    def __init__(self, compiler)  -> None:
        self.compiler = compiler

    def __getattr__(self, lang: str):
        async def func(code: str) -> Coroutine[Any, Any, Response]:
            if lang in self.compiler.query_langs:
                return await self.compiler.compiler(lang, code) 
        return func

class AsyncCompiler(BaseCompiler):
    """Asynchronous compiler execution"""
    def __init__(self) -> None:
        super().__init__()
        self._client = AsyncClient()
        self.to = ToLang(self)
        self.query = QueryLang(self)
	
    async def compiler(self, lang: str, code: str) -> Response:
        """
        compiles your code

        Args:
            lang (str): Programing language
            code (str): Сode that will be sent for compilation

        Returns:
            Response: Pydantic model
        """
        lang_data = self._get_lang_data(lang, code)
        lang_data.properties.files[0].content = code
        res = await self._client.post(self._url, json=lang_data.dict(), headers=self._headers)
        return Response.parse_obj(res.json())
    