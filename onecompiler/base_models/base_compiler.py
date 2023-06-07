from httpx._client import BaseClient
from onecompiler import data
from onecompiler.base_errors import LangNotFound
from onecompiler.pydantic_models import Lang

class BaseCompiler:
	""" 
	Base class for synchronous and asynchronous compiler
	"""
	
	_client = BaseClient

	_url = "https://onecompiler.com/api/code/exec"
	_headers = {
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.5.710 Yowser/2.5 Safari/537.36"
	}

	languages = data.keys()


	def _get_lang_data(self, lang: str, code: str) -> Lang:
		""" You get a language config to send a POST request to the compiler """
		if lang not in self.languages:
			raise LangNotFound
		d = data.get(lang)
		return Lang.parse_obj(d) 
