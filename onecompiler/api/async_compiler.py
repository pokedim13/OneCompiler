from httpx import AsyncClient
from onecompiler.base_models import BaseCompiler
from onecompiler.pydantic_models import Response
import asyncio

class ToLang:
	def __init__(self, compiler):
			self.compiler = compiler

	async def __getattr__(self, lang: str):
		async def func(code: str):
			return await self.compiler.compiler(lang, code) 
		return await func

class AsyncCompiler(BaseCompiler):
    def __init__(self) -> None:
        super().__init__()
        self._client = AsyncClient()
        self.to = ToLang(self)
	
    async def compiler(self, lang: str, code: str) -> Response:
        """ compiles your code """
        lang_data = self._get_lang_data(lang, code)
        lang_data.properties.files[0].content = code
        return Response.parse_obj(await self._client.post(self._url, json=lang_data.dict(), headers=self._headers).json())
    
async def main():
	compiler = AsyncCompiler()
	print(compiler.to.py())
	
asyncio.run(main())