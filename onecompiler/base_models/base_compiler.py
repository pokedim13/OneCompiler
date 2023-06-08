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

	programming_langs = data['programming'].keys()
	query_langs = data['query'].keys()

	all_languages = {i: list(data[i]) for i in data}


	def _create_lang_data(self, lang, lang_type, code) -> dict:
		full_name, extension = data[lang_type][lang]
		
		finall_data = {
	    			"name": full_name,
	    			"title": f"{full_name} Hello World",
	    			"version": "latest",
	    			"mode": full_name,
	    			#"description": None,
	    			"extension": extension,
	    			"languageType": ("programming" if lang_type != 'query' else 'database'),
	    			"active": True,
	    			"properties": {
	    				"language": full_name,
	    				"docs": True,
	    				"tutorials": True,
	    				"cheatsheets": True,
	    				"files": [{"name": f"file.{extension}", "content": code}],
	    			},
	    			"visibility": "public",
    		    }

		return finall_data


	def _get_lang_data(self, lang: str, code: str) -> Lang:
		""" You get a language config to send a POST request to the compiler """
		lang_type = None
		
		for lang_types in self.all_languages:
			if lang in self.all_languages[lang_types]:
				lang_type = lang_types

		if lang_type is None:
			raise LangNotFound

		lang_data = self._create_lang_data(lang, lang_type, code)#data[lang_type][lang]
		return Lang.parse_obj(lang_data)
