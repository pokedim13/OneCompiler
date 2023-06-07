from httpx import Client
from onecompiler.base_models import BaseCompiler
from onecompiler.pydantic_models import Response
from pydantic.error_wrappers import ValidationError

class ToLang:
		def __init__(self, compiler):
			self.compiler = compiler

		def __getattr__(self, lang: str):
			def func(code: str):
				return self.compiler.compiler(lang, code) 
			return func

class Compiler(BaseCompiler):
    def __init__(self) -> None:
        super().__init__()
        self._client = Client()
        self.to = ToLang(self)
	
    def compiler(self, lang: str, code: str) -> Response:
        """ compiles your code """
        lang_data = self._get_lang_data(lang, code)
        lang_data.properties.files[0].content = code
        res = self._client.post(self._url, json=lang_data.dict(), headers=self._headers).json()
        return Response.parse_obj(res)