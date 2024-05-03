from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from onecompiler.models import compiler
if TYPE_CHECKING:
    from onecompiler.client import OneCompiler

class BaseCompiler:
    
	_url = "https://onecompiler.com/api/code/exec"
    
	def _create_lang_data(self, lang, code, lang_type: str = "programming") -> dict:
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

class Compiler(BaseCompiler):
    def __init__(self, client: OneCompiler):
        self._client = client

    async def compile(self, lang: str, code: str):
        res = await self._client._client.post(self._url, json=self._create_lang_data(lang=lang, code=code))
        print(res.text)
        return compiler.ResponceModel.model_validate(res.json())