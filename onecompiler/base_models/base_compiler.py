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
		#full_name = data[lang_type][lang]
		
		finall_data = {
	    			"name": lang,
	    			"title": f"{lang} Hello World",
	    			"version": "latest",
	    			"mode": lang,
	    			#"description": None,
	    			"extension": lang,
	    			"languageType": ("programming" if lang_type != 'query' else 'database'),
	    			"active": True,
	    			"properties": {
	    				"language": lang,
	    				"docs": True,
	    				"tutorials": True,
	    				"cheatsheets": True,
	    				"files": [{"name": f"file.{lang}", "content": code}],
	    			},
	    			"visibility": "public",
		    }

		return finall_data


	def _get_full_lang_name(self, lang: str):
		full_name = None
		lang_type = None

		for langs in self.programming_langs:
			if (lang == langs) or (lang in data['programming'][langs]):
				lang_type = 'programming'
				full_name = langs

		if lang_type is None:
			for langs in self.query_langs:
				if (lang == langs) or (lang in data['query'][langs]):
					lang_type = 'query'
					full_name = langs

		if lang_type and full_name:
			return (full_name, lang_type)
		raise LangNotFound


	def _get_lang_data(self, lang: str, code: str) -> Lang:
		""" You get a language config to send a POST request to the compiler """
		lang, lang_type = self._get_full_lang_name(lang)

		lang_data = self._create_lang_data(lang, lang_type, code)
		return Lang.parse_obj(lang_data)


	def get_lang_reductions(self, lang):
		""" Gets a list of abbreviated names for a specific language """
		if lang in self.programming_langs:
			return data['programming'].get(lang)
		return data['query'].get(lang)
