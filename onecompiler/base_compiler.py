from httpx._client import BaseClient


class BaseCompiler:
	""" 
	Base class for synchronous and asynchronous compiler
	"""
	
	client = BaseClient

	_url = "https://onecompiler.com/api/code/exec"
	_headers = {
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.5.710 Yowser/2.5 Safari/537.36"
	}

	languages = ['python', 'js', 'brainfk', 'cpp', 'bash', 'c', 'php', 'java', 'rust', 'haskell', 'cs', 'pascal', 'go']


	def _get_lang_data(self, lang: str, code: str) -> dict:
		""" You get a language config to send a POST request to the compiler """
		_lang_configs = {
			"python": {
				"name": "Python",
				"title": "Python Hello World",
				"version": "3.7",
				"mode": "python",
				"description": None,
				"extension": "py",
				"concurrentJobs": 10,
				"languageType": "programming",
				"active": True,
				"properties": {
					"language": "python",
					"docs": True,
					"tutorials": True,
					"cheatsheets": True,
					"filesEditable": True,
					"filesDeletable": True,
					"files": [{"name": "main.py", "content": code}],
					"newFileOptions": [
						{
							"helpText": "New Python file",
							"name": "script${i}.py",
							"content": "# In main file\n# import script${i}\n# print(script${i}.sum(1, 3))\n\ndef sum(a, b):\n	return a + b",
						}
					],
				},
				"visibility": "public",
			},
			"js": {
				"name": "JavaScript",
				"title": "JavaScript Hello World",
				"version": "ES6",
				"mode": "javascript",
				"description": None,
				"extension": "js",
				"languageType": "programming",
				"active": True,
				"properties": {
					"language": "javascript",
					"docs": True,
					"tutorials": True,
					"cheatsheets": True,
					"filesEditable": True,
					"filesDeletable": True,
					"files": [{"name": "index.js", "content": code}],
					"newFileOptions": [
						{
							"helpText": "New JS file",
							"name": "script${i}.js",
							"content": "/**\n *  In main file\n *  let script${i} = require('./script${i}');\n *  console.log(script${i}.sum(1, 2));\n */\n\nfunction sum(a, b) {\n	return a + b;\n}\n\nmodule.exports = { sum };",
						},
						{
							"helpText": "Add Dependencies",
							"name": "package.json",
							"content": '{\n  "name": "main_app",\n  "version": "1.0.0",\n  "description": "",\n  "main": "HelloWorld.js",\n  "dependencies": {\n	"lodash": "^4.17.21"\n  }\n}',
						},
					],
					"result": {"success": True, "output": "Hello, World!\n"},
				},
				"visibility": "public",
			},
			"brainfk": {
				"name": "BrainFK",
				"title": "BrainFK Hello World!",
				"mode": "text",
				"description": None,
				"extension": "bf",
				"languageType": "programming",
				"active": True,
				"worker": "s",
				"properties": {
					"language": "brainfk",
					"docs": False,
					"tutorials": False,
					"cheatsheets": False,
					"files": [{"name": "helloworld.bf", "content": code}],
				},
				"visibility": "public",
			},
			"cpp": {
				"name": "C++",
				"title": "C++ Hello World",
				"version": "latest",
				"mode": "c_cpp",
				"description": None,
				"extension": "cpp",
				"languageType": "programming",
				"active": True,
				"properties": {
					"language": "cpp",
					"docs": True,
					"tutorials": True,
					"cheatsheets": True,
					"files": [{"name": "Main.cpp", "content": code}],
				},
				"visibility": "public",
			},
			"bash": {
				"name": "Bash",
				"title": "Bash Hello World!",
				"mode": "tcl",
				"description": None,
				"extension": "sh",
				"languageType": "programming",
				"active": True,
				"worker": "j",
				"workerId": 46,
				"properties": {
					"language": "bash",
					"docs": False,
					"tutorials": False,
					"cheatsheets": False,
					"files": [{"name": "HelloWorld.sh", "content": code}],
				},
				"visibility": "public",
			},
			"c": {
				"name": "C",
				"title": "C Language Hello World",
				"version": "latest",
				"mode": "c_cpp",
				"description": None,
				"extension": "c",
				"languageType": "programming",
				"active": True,
				"properties": {
					"language": "c",
					"docs": True,
					"tutorials": True,
					"cheatsheets": True,
					"filesEditable": True,
					"filesDeletable": True,
					"files": [{"name": "Main.c", "content": code}],
					"newFileOptions": [
						{
							"helpText": "New Text file",
							"name": "sample${i}.txt",
							"content": "Sample text file!",
						}
					],
				},
				"visibility": "public",
			},
			"php": {
				"name": "PHP",
				"title": "Php Hello World!",
				"mode": "java",
				"description": None,
				"extension": "php",
				"languageType": "programming",
				"active": True,
				"properties": {
					"language": "php",
					"docs": True,
					"tutorials": True,
					"cheatsheets": True,
					"files": [{"name": "HelloWorld.php", "content": code}],
				},
				"visibility": "public",
			},
			"java": {
				"name": "Java",
				"title": "Java Hello World",
				"version": "11",
				"mode": "java",
				"description": None,
				"extension": "java",
				"concurrentJobs": 2,
				"languageType": "programming",
				"active": True,
				"properties": {
					"language": "java",
					"docs": True,
					"tutorials": False,
					"cheatsheets": True,
					"filesEditable": True,
					"filesDeletable": True,
					"files": [
						{"name": "Main.java", "content": code},
						{
							"helpText": "Add Dependencies",
							"name": "build.gradle",
							"content": "apply plugin:'application'\nmainClassName = 'HelloWorld'\n\nrun { standardInput = System.in }\nsourceSets { main { java { srcDir './' } } }\n\nrepositories {\n	jcenter()\n}\n\ndependencies {\n	// add dependencies here like following\n	// implementation group: 'org.apache.commons', name: 'commons-lang3', version: '3.9'\n}",
						},
					],
				},
				"visibility": "public",
			},
			"rust": {
				"name": "Rust",
				"title": "Rust Hello World!",
				"mode": "c_cpp",
				"description": None,
				"extension": "rs",
				"languageType": "programming",
				"active": True,
				"worker": "j",
				"workerId": 73,
				"properties": {
					"language": "rust",
					"docs": False,
					"tutorials": False,
					"cheatsheets": False,
					"files": [{"name": "HelloWorld.rs", "content": code}],
				},
				"visibility": "public",
			},
			"haskell": {
				"name": "Haskell",
				"title": "Haskell Hello World!",
				"mode": "haskell",
				"description": None,
				"extension": "hs",
				"languageType": "programming",
				"active": True,
				"properties": {
					"language": "haskell",
					"docs": True,
					"tutorials": False,
					"cheatsheets": False,
					"files": [{"name": "Main.hs", "content": code}],
				},
				"visibility": "public",
			},
			"cs": {
				"name": "C#",
				"title": "C# Hello World!",
				"mode": "csharp",
				"description": None,
				"extension": "cs",
				"languageType": "programming",
				"active": True,
				"properties": {
					"language": "csharp",
					"docs": True,
					"tutorials": True,
					"cheatsheets": True,
					"files": [{"name": "HelloWorld.cs", "content": code}],
				},
				"visibility": "public",
			},
			"pascal": {
				"name": "Pascal",
				"title": "Pascal Hello World!",
				"mode": "javascript",
				"description": None,
				"extension": "pas",
				"languageType": "programming",
				"active": True,
				"worker": "j",
				"workerId": 67,
				"properties": {
					"language": "pascal",
					"docs": False,
					"tutorials": False,
					"cheatsheets": False,
					"files": [{"name": "HelloWorld.pas", "content": code}],
				},
				"visibility": "public",
			},
			"go": {
				"name": "Go",
				"title": "Go Hello World!",
				"mode": "golang",
				"description": None,
				"extension": "go",
				"languageType": "programming",
				"active": True,
				"properties": {
					"language": "go",
					"docs": True,
					"tutorials": True,
					"cheatsheets": True,
					"files": [{"name": "HelloWorld.go", "content": code}],
				},
				"visibility": "public",
			},
		}

		return _lang_configs.get(lang)