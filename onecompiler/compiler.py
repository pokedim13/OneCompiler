from httpx import Client
from base_compiler import BaseCompiler


class Compiler(BaseCompiler):
	"""
		Synchronous compiler
	"""
	def __init__(self):

		self._client = Client()
		self.to = self.ToLang(self)


	def compiler(self, lang: str, code: str) -> dict:
		""" compiles your code """
		lang_data = self._get_lang_data(lang, code)

		if lang_data is None:
			raise Exception('no lang')

		response = self._client.post(self._url, json=lang_data, headers=self._headers)
		return response.text


	class ToLang:
		def __init__(self, compiler):
			self.compiler = compiler


		def __getattr__(self, lang: str):
			if lang in self.compiler.languages:
				def func(code: str):
					return self.compiler.compiler(lang, code)
				
				return func
