from httpx import AsyncClient
from base_compiler import BaseCompiler


class AsyncCompiler(BaseCompiler):
	"""
	Asynchronous compiler
	"""
	def __init__(self):

		self._client = AsyncClient()
		self.to = self.ToLang(self)


	async def compiler(self, lang: str, code: str) -> dict:
		""" compiles your code """
		lang_data = self._get_lang_data(lang, code)

		if lang_data is None:
			raise Exception('no lang')

		response = await self._client.post(self._url, json=lang_data, headers=self._headers)
		return response.text


	class ToLang:
		def __init__(self, compiler):
			self.compiler = compiler


		def __getattr__(self, lang: str):
			if lang in self.compiler.languages:
				async def func(code: str):
					return await self.compiler.compiler(lang, code)
				
				return func


import asyncio 

async def main():
	compiler = AsyncCompiler()

	data = await compiler.to.bash('echo 1')
	print(data)


asyncio.run(main())