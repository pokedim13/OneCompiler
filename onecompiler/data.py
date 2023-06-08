data2 = {
        'programming': {
            "java":{
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
                    {
                        "name": "Main.java",
                        "content": "{code}"
                    }
                    ],
                    "newFileOptions": [
                    {
                        "helpText": "New Java file",
                        "name": "NewClass${i}.java",
                        "content": "public class NewClass${i} {\n\n  public String sayHelloFromNewClass(){\n    return \"Hello from New Class\";\n  }\n\n}"
                    },
                    {
                        "helpText": "Add Dependencies",
                        "name": "build.gradle",
                        "content": "apply plugin:'application'\nmainClassName = 'HelloWorld'\n\nrun { standardInput = System.in }\nsourceSets { main { java { srcDir './' } } }\n\nrepositories {\n    jcenter()\n}\n\ndependencies {\n    // add dependencies here like following\n    // implementation group: 'org.apache.commons', name: 'commons-lang3', version: '3.9'\n}"
                    }
                    ]
                },
                "visibility": "public"
                },
    		"python": {
    			"name": "p",
    			"title": "Python Hello World",
    			"version": "latest",
    			"mode": "pythonn",
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
    				"files": [{"name": "main.py", "content": "{code}"}],
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
    				"files": [{"name": "Main.c", "content": "{code}"}],
    			},
    			"visibility": "public",
    		    },
            "cpp": {
    			"name": "C++",
    			"title": "C++ Hello World",
    			"version": "latest",
    			"mode": "c",
    			"description": None,
    			"extension": "cpp",
    			"languageType": "programming",
    			"active": True,
    			"properties": {
    				"language": "cpp",
    				"docs": True,
    				"tutorials": True,
    				"cheatsheets": True,
    				"files": [{"name": "Main.cpp", "content": "{code}"}],
    			},
    			"visibility": "public",
    		    },
            "node": {
                "name": "NodeJS",
                "title": "NodeJS Hello World",
                "version": "12.13",
                "mode": "javascript",
                "description": None,
                "extension": "js",
                "languageType": "programming",
                "active": True,
                "properties": {
                    "language": "nodejs",
                    "docs": True,
                    "tutorials": True,
                    "cheatsheets": True,
                    "filesEditable": True,
                    "filesDeletable": True,
                    "files": [{"name": "index.js","content": "{code}"}]
                },
                "visibility": "public"
                },
            "js": {
    			"name": "JavaScript",
    			"title": "JavaScript Hello World",
    			"version": "ES6",
    			"mode": "javascript",
    			#"description": None,
    			"extension": "js",
    			"languageType": "programming",
    			"active": True,
    			"properties": {
    				"language": "javascript",
    				"docs": True,
    				"tutorials": True,
    				"cheatsheets": True,
    				"files": [{"name": "index.js", "content": "{code}"}],
    			},
    			"visibility": "public",
    		    },

            "groovy": {
                "name": "Groovy",
                "title": "Groovy Hello World",
                "mode": "groovy",
                "description": None,
                "extension": "groovy",
                "languageType": "programming",
                "active": True,
                "properties": {
                    "language": "groovy",
                    "docs": True,
                    "tutorials": True,
                    "cheatsheets": True,
                    "files": [{"name": "Main.groovy", "content": "{code}"}]
                },
                "visibility": "public"
                },
            "jsh": {
                "name": "JShell",
                "title": "JShell Hello World",
                "mode": "java",
                "description": None,
                "extension": "jsh",
                "languageType": "programming",
                "active": True,
                "properties": {
                    "language": "jshell",
                    "docs": True,
                    "tutorials": False,
                    "cheatsheets": True,
                    "files": [
                    {
                        "name": "script.jsh",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            'hs': {
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
                    "files": [
                    {
                        "name": "Main.hs",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "tcl": {
                "name": "Tcl",
                "title": "Tcl Hello World!",
                "mode": "tcl",
                "description": None,
                "extension": "tcl",
                "languageType": "programming",
                "active": True,
                "properties": {
                    "language": "tcl",
                    "docs": True,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "main.tcl",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "lua": {
                "name": "Lua",
                "title": "Lua Hello World!",
                "mode": "lua",
                "description": None,
                "extension": "lua",
                "languageType": "programming",
                "active": True,
                "properties": {
                    "language": "lua",
                    "docs": True,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "Main.lua",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "ada": {
                "name": "Ada",
                "title": "Ada Hello World!",
                "mode": "ada",
                "description": None,
                "extension": "adb",
                "languageType": "programming",
                "active": True,
                "properties": {
                    "language": "ada",
                    "docs": True,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "HelloWorld.adb",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "lsp": {
                "name": "CommonLisp",
                "title": "CommonLisp Hello World!",
                "mode": "lisp",
                "description": None,
                "extension": "lsp",
                "languageType": "programming",
                "active": True,
                "worker": "j",
                "workerId": 55,
                "properties": {
                    "language": "commonlisp",
                    "docs": True,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "HelloWorld.lsp",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "d": {
                "name": "D",
                "title": "D Hello World!",
                "mode": "c_cpp",
                "description": None,
                "extension": "d",
                "languageType": "programming",
                "active": True,
                "properties": {
                    "language": "d",
                    "docs": True,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "HelloWorld.d",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "elixir": {
                "name": "Elixir",
                "title": "Elixir Hello World!",
                "mode": "c_cpp",
                "description": None,
                "extension": "ex",
                "languageType": "programming",
                "active": True,
                "worker": "j",
                "workerId": 57,
                "properties": {
                    "language": "elixir",
                    "docs": True,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "HelloWorld.ex",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "erl": {
                "name": "Erlang",
                "title": "Erlang Hello World!",
                "mode": "c_cpp",
                "description": None,
                "extension": "erl",
                "languageType": "programming",
                "active": True,
                "worker": "j",
                "workerId": 58,
                "properties": {
                    "language": "erlang",
                    "docs": True,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "main.erl",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "fs": {
                "name": "F#",
                "title": "F# Hello World!",
                "mode": "csharp",
                "description": None,
                "extension": "fs",
                "languageType": "programming",
                "active": True,
                "properties": {
                    "language": "fsharp",
                    "docs": True,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "HelloWorld.fs",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "fortran": {
                "name": "Fortran",
                "title": "Fortran Hello World!",
                "mode": "fortran",
                "description": None,
                "extension": "ftn",
                "languageType": "programming",
                "active": True,
                "properties": {
                    "language": "fortran",
                    "docs": True,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "HelloWorld.ftn",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "asm": {
                "name": "Assembly",
                "title": "Assembly Hello World!",
                "mode": "assembly_x86",
                "description": None,
                "extension": "asm",
                "languageType": "programming",
                "active": True,
                "properties": {
                    "language": "assembly",
                    "docs": True,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "HelloWorld.asm",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "scala": {
                "name": "Scala",
                "title": "Scala Hello World!",
                "mode": "scala",
                "description": None,
                "extension": "scala",
                "languageType": "programming",
                "active": True,
                "properties": {
                    "language": "scala",
                    "docs": True,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "HelloWorld.scala",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
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
                    "files": [
                    {
                        "name": "HelloWorld.php",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "python2": {
                "name": "Python2",
                "title": "Python2 Hello World!",
                "mode": "python",
                "description": None,
                "extension": "py",
                "languageType": "programming",
                "active": True,
                "properties": {
                    "language": "python2",
                    "docs": True,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "HelloWorld.py",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
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
                    "files": [
                    {
                        "name": "HelloWorld.cs",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "perl": {
                "name": "Perl",
                "title": "Perl Hello World!",
                "mode": "perl",
                "description": None,
                "extension": "pl",
                "languageType": "programming",
                "active": True,
                "properties": {
                    "language": "perl",
                    "docs": True,
                    "tutorials": True,
                    "cheatsheets": True,
                    "files": [
                    {
                        "name": "HelloWorld.pl",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "ruby": {
                "name": "Ruby",
                "title": "Ruby Hello World!",
                "mode": "ruby",
                "description": None,
                "extension": "rb",
                "languageType": "programming",
                "active": True,
                "properties": {
                    "language": "ruby",
                    "docs": True,
                    "tutorials": True,
                    "cheatsheets": True,
                    "files": [
                    {
                        "name": "HelloWorld.rb",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
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
                    "files": [
                    {
                        "name": "HelloWorld.go",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "r": {
                "name": "R",
                "title": "R Hello World!",
                "mode": "r",
                "description": None,
                "extension": "r",
                "languageType": "programming",
                "active": True,
                "properties": {
                    "language": "r",
                    "docs": True,
                    "tutorials": True,
                    "cheatsheets": True,
                    "files": [
                    {
                        "name": "HelloWorld.r",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "racket": {
                "name": "Racket",
                "title": "Racket Hello World!",
                "mode": "perl",
                "description": None,
                "extension": "rkt",
                "languageType": "programming",
                "active": True,
                "properties": {
                    "language": "racket",
                    "docs": True,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "HelloWorld.rkt",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "ml": {
                "name": "OCaml",
                "title": "Ocaml Hello World!",
                "mode": "perl",
                "description": None,
                "extension": "ml",
                "languageType": "programming",
                "active": True,
                "properties": {
                    "language": "ocaml",
                    "docs": True,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "HelloWorld.ml",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "vb": {
                "name": "Visual Basic (VB.NET)",
                "title": "Visual Basic Hello World!",
                "mode": "vbscript",
                "description": None,
                "extension": "vb",
                "languageType": "programming",
                "active": True,
                "properties": {
                    "language": "vb",
                    "docs": True,
                    "tutorials": True,
                    "cheatsheets": True,
                    "files": [
                    {
                        "name": "HelloWorld.vb",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "sh": {
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
                    "files": [
                    {
                        "name": "HelloWorld.sh",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "clj": {
                "name": "Clojure",
                "title": "Clojure Hello World!",
                "mode": "lisp",
                "description": None,
                "extension": "clj",
                "languageType": "programming",
                "active": True,
                "worker": "j",
                "workerId": 86,
                "properties": {
                    "language": "clojure",
                    "docs": False,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "HelloWorld.clj",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "ts": {
                "name": "TypeScript",
                "title": "TypeScript Hello World!",
                "mode": "javascript",
                "description": None,
                "extension": "ts",
                "languageType": "programming",
                "active": True,
                "worker": "j",
                "workerId": 74,
                "properties": {
                    "language": "typescript",
                    "docs": False,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "HelloWorld.ts",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "cbl": {
                "name": "Cobol",
                "title": "Cobol Hello World!",
                "mode": "assembly_x86",
                "description": None,
                "extension": "cbl",
                "languageType": "programming",
                "active": True,
                "worker": "j",
                "workerId": 77,
                "properties": {
                    "language": "cobol",
                    "docs": False,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "HelloWorld.cbl",
                        "content": "{code}"
                    }
                    ],
                    "result": {
                    "success": True,
                    "output": "Hello, World!\n"
                    }
                },
                "visibility": "public"
                },
            "kotlin": {
                "name": "Kotlin",
                "title": "Kotlin Hello World!",
                "mode": "groovy",
                "description": None,
                "extension": "kt",
                "languageType": "programming",
                "active": True,
                "worker": "j",
                "workerId": 78,
                "properties": {
                    "language": "kotlin",
                    "docs": False,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "HelloWorld.kt",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
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
                    "files": [
                        {
                            "name": "HelloWorld.pas",
                            "content": "{code}"
                        }
                    ]
                },
                "visibility": "public"
            },
            "prolog": {
                "name": "Prolog",
                "title": "Prolog Hello World!",
                "mode": "javascript",
                "description": None,
                "extension": "pl",
                "languageType": "programming",
                "active": True,
                "worker": "j",
                "workerId": 69,
                "properties": {
                    "language": "prolog",
                    "docs": False,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "HelloWorld.pl",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
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
                    "files": [
                    {
                        "name": "HelloWorld.rs",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "swift": {
                "name": "Swift",
                "title": "Swift Hello World!",
                "mode": "c_cpp",
                "description": None,
                "extension": "swift",
                "languageType": "programming",
                "active": True,
                "worker": "j",
                "workerId": 83,
                "properties": {
                    "language": "swift",
                    "docs": False,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "HelloWorld.swift",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "octave": {
                "name": "Octave",
                "title": "Octave Hello World!",
                "mode": "javascript",
                "description": None,
                "extension": "m",
                "languageType": "programming",
                "active": True,
                "worker": "j",
                "workerId": 66,
                "properties": {
                    "language": "octave",
                    "docs": False,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "HelloWorld.m",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
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
    				"files": [{"name": "helloworld.bf", "content": "{code}"}],
    			},
    			"visibility": "public",
    		},
            "coffee": {
                "name": "CoffeeScript",
                "title": "CoffeeScript Hello World!",
                "mode": "javascript",
                "description": None,
                "extension": "coffee",
                "languageType": "programming",
                "active": True,
                "worker": "s",
                "properties": {
                    "language": "coffeescript",
                    "docs": False,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "helloworld.coffee",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "ejs": {
                "name": "EJS",
                "title": "EJS Hello World!",
                "mode": "javascript",
                "description": None,
                "extension": "ejs",
                "languageType": "programming",
                "active": True,
                "worker": "s",
                "properties": {
                    "language": "ejs",
                    "docs": False,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "helloworld.ejs",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            },
        'query': {
            "sqlite": {
                "name": "SQLite",
                "title": "SQLite",
                "mode": "sql",
                "description": None,
                "extension": "sql",
                "languageType": "database",
                "active": True,
                "worker": "j",
                "workerId": 82,
                "properties": {
                    "language": "sqlite",
                    "docs": True,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "queries.sql",
                        "content": "{code}"
                    }
                    ],
                    "result": {
                    "success": True,
                    "output": "1|Clark|Sales\n3|Ava|Sales\n"
                    }
                },
                "visibility": "public"
                },
            "postgres":{
                "name": "PostgreSQL",
                "title": "PostgreSQL",
                "mode": "sql",
                "description": None,
                "extension": "sql",
                "languageType": "database",
                "active": True,
                "properties": {
                    "language": "postgresql",
                    "docs": False,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "commands.sql",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "redis": {
                "name": "Redis",
                "title": "Redis",
                "mode": "javascript",
                "description": None,
                "extension": "redis",
                "languageType": "database",
                "active": True,
                "properties": {
                    "language": "redis",
                    "docs": True,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "commands.redis",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "mysql": {
                "name": "MySQL",
                "title": "MySQL",
                "mode": "sql",
                "description": None,
                "extension": "sql",
                "languageType": "database",
                "active": True,
                "properties": {
                    "language": "mysql",
                    "docs": False,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "queries.sql",
                        "content": "{code}"
                    }
                    ],
                },
                "visibility": "public"
                },
            "mongo": {
                "name": "MongoDB",
                "title": "MongoDB",
                "mode": "javascript",
                "description": None,
                "extension": "js",
                "languageType": "database",
                "active": True,
                "properties": {
                    "language": "mongodb",
                    "docs": False,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "script.js",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "maria": {
                "name": "MariaDB",
                "title": "MariaDB",
                "mode": "sql",
                "description": None,
                "extension": "sql",
                "languageType": "database",
                "active": True,
                "properties": {
                    "language": "mariadb",
                    "docs": True,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "commands.sql",
                        "content": "{code}"
                    }
                    ]
                },
                "visibility": "public"
                },
            "ms_sql":{
                "name": "Microsoft SQL Server",
                "title": "SQL Server",
                "mode": "sql",
                "description": None,
                "extension": "sql",
                "languageType": "database",
                "active": True,
                "properties": {
                    "language": "sqlserver",
                    "docs": False,
                    "tutorials": False,
                    "cheatsheets": False,
                    "files": [
                    {
                        "name": "queries.sql",
                        "content": "{code}"
                    }
                    ]
                },
                "concurrentJobs": 5,
                "visibility": "public"
                }
        }
	}


# FullName
data = {
  "programming": {
    "ada": [
      "ada",
      "adb"
    ],
    "asm": [
      "assembly",
      "asm"
    ],
    "brainfk": [
      "brainfk",
      "bf"
    ],
    "c": [
      "c",
      "c"
    ],
    "cbl": [
      "cobol",
      "cbl"
    ],
    "clj": [
      "clojure",
      "clj"
    ],
    "coffee": [
      "coffeescript",
      "coffee"
    ],
    "cpp": [
      "cpp",
      "cpp"
    ],
    "cs": [
      "csharp",
      "cs"
    ],
    "d": [
      "d",
      "d"
    ],
    "ejs": [
      "ejs",
      "ejs"
    ],
    "elixir": [
      "elixir",
      "ex"
    ],
    "erl": [
      "erlang",
      "erl"
    ],
    "fortran": [
      "fortran",
      "ftn"
    ],
    "fs": [
      "fsharp",
      "fs"
    ],
    "go": [
      "go",
      "go"
    ],
    "groovy": [
      "groovy",
      "groovy"
    ],
    "hs": [
      "haskell",
      "hs"
    ],
    "java": [
      "java",
      "java"
    ],
    "js": [
      "javascript",
      "js"
    ],
    "jsh": [
      "jshell",
      "jsh"
    ],
    "kotlin": [
      "kotlin",
      "kt"
    ],
    "lsp": [
      "commonlisp",
      "lsp"
    ],
    "lua": [
      "lua",
      "lua"
    ],
    "ml": [
      "ocaml",
      "ml"
    ],
    "node": [
      "nodejs",
      "js"
    ],
    "octave": [
      "octave",
      "m"
    ],
    "pascal": [
      "pascal",
      "pas"
    ],
    "perl": [
      "perl",
      "pl"
    ],
    "php": [
      "php",
      "php"
    ],
    "prolog": [
      "prolog",
      "pl"
    ],
    "python": [
      "python",
      "py"
    ],
    "python2": [
      "python2",
      "py"
    ],
    "r": [
      "r",
      "r"
    ],
    "racket": [
      "racket",
      "rkt"
    ],
    "ruby": [
      "ruby",
      "rb"
    ],
    "rust": [
      "rust",
      "rs"
    ],
    "scala": [
      "scala",
      "scala"
    ],
    "sh": [
      "bash",
      "sh"
    ],
    "swift": [
      "swift",
      "swift"
    ],
    "tcl": [
      "tcl",
      "tcl"
    ],
    "ts": [
      "typescript",
      "ts"
    ],
    "vb": [
      "vb",
      "vb"
    ]
  },
  "query": {
    "maria": [
      "mariadb",
      "sql"
    ],
    "mongo": [
      "mongodb",
      "js"
    ],
    "ms_sql": [
      "sqlserver",
      "sql"
    ],
    "mysql": [
      "mysql",
      "sql"
    ],
    "postgres": [
      "postgresql",
      "sql"
    ],
    "redis": [
      "redis",
      "redis"
    ],
    "sqlite": [
      "sqlite",
      "sql"
    ]
  }
}


# ================================================ #
test = {
    'java': """
import java.util.*;

public class Main {
    public static void main(String[] args) {
      System.out.println("Hello, World!");
  }
}    
    """,
    ###########################
    'py': """
print("Hello, World!")    
    """,
    ###########################
    'c': """
#include <stdio.h>
int main()
{
    printf("Hello, World!");
}    
    """,
    ###########################
    'cpp': """
#include <stdio.h>
int main()
{
    printf("Hello, World!");
}      
    """, 
    ###########################
    'node': """
console.log("Hello, World!");        
    """, 
    ###########################
    'js': """
console.log("Hello, World!");       
    """, 
    ###########################
    'groovy': """
println "Hello, World!"    
    """, 
    ###########################
    'jsh': """
System.out.println("Hello, World!");
    """, 
    ###########################
    'hs': """
main = putStrLn "Hello, World!"
    """, 
    ###########################
    'tcl': """
puts "Hello, World!"
    """, 
    ###########################
    'lua': """
print ("Hello, World!")
    """, 
    ###########################
    'adb': """
with Ada.Text_IO; use Ada.Text_IO;
procedure Hello is
begin
		Put_Line ("Hello, World!");
end Hello;
    """, 
    ###########################
    'lsp': """
(format t "Hello, World!")
    """, 
    ###########################
    'd': """
import std.stdio;

void main()
{
		writeln("Hello, World!");
}
    """, 
    ###########################
    'ex': """
IO.puts "Hello, World!"
    """, 
    ###########################
    'erl': """
main(_) -> io:fwrite("Hello, World!").
    """, 
    ###########################
    'fs': """
open System
printfn "Hello, World!"
    """, 
    ###########################
    'ftn': """
program hello
	print *, "Hello, World!"
end program hello
    """, 
    ###########################
    'asm': """
section .data
	hello:     db 'Hello, World!',10    ; 'Hello, World!' plus a linefeed character
	helloLen:  equ $-hello             ; Length of the 'Hello world!' string

section .text
	global _start

_start:
	mov eax,4            ; The system call for write (sys_write)
	mov ebx,1            ; File descriptor 1 - standard output
	mov ecx,hello        ; Put the offset of hello in ecx
	mov edx,helloLen     ; helloLen is a constant, so we don't need to say
	                     ;  mov edx,[helloLen] to get it's actual value
	int 80h              ; Call the kernel
	mov eax,1            ; The system call for exit (sys_exit)
	mov ebx,0            ; Exit with return "code" of 0 (no error)
	int 80h;
    """, 
    ###########################
    'scala': """
object HelloWorld {
	def main(args: Array[String]): Unit = {
	println("Hello, World!")
	}
}
    """, 
    ###########################
    'php': """
<?php
	echo "Hello, World!"
?>    
    """, 
    ###########################
    'py2': """
print 'hello, world!'
    """, 
    ###########################
    'cs': """
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace HelloWorld
{
	public class Program
	{
		public static void Main(string[] args)
		{
			Console.WriteLine("Hello, World!");
		}
	}
}
    """, 
    ###########################
    'pl': """
:- initialization(main).
main :- write('Hello, World!').
    """, 
    ###########################
    'rb': """
puts "Hello, World!"
    """, 
    ###########################
    'go': """
package main
import "fmt"

func main() {
	fmt.Printf("Hello, World!")
}
    """, 
    ###########################
    'r': """
cat("Hello, World!")
    """, 
    ###########################
    'rkt': """
#lang racket/base
(display "Hello, World!")
    """, 
    ###########################
    'ml': """
print_string "Hello, World!"
    """, 
    ###########################
    'vb': """
Public Module Program
	Public Sub Main(args() As string)
		Console.WriteLine("Hello, World!")
	End Sub
End Module
    """, 
    ###########################
    'sh': """
echo "Hello, World!"
    """, 
    'clj': """
(defn greetings [msg]
(println (format "Hello, %s" msg)))

(greetings "World!")
    """, 
    ###########################
    'ts': """
console.log("Hello, World!")
    """, 
    ###########################
    'cbl': """
IDENTIFICATION DIVISION.
PROGRAM-ID. HELLO-WORLD.
PROCEDURE DIVISION.
DISPLAY 'Hello, World!'.
STOP RUN.
    """, 
    ###########################
    'kt': """
fun main(args: Array<String>) {
    println("Hello, World!")
}
    """, 
    ###########################
    'pas': """
program Hello;
begin
  writeln ('Hello, World!')
end.
    """, 
    ###########################
    'rs': """
fn main() {
    println!("Hello, World!");
}
    """, 
    ###########################
    'swift': """
print("Hello, World!")
    """, 
    ###########################
    'm': """
disp('Hello, World!')
    """, 
    ###########################
    'bf': """
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
    """, 
    ###########################
    'coffee': """
console.log "Hello, World!"
    """, 
    ###########################
    'ejs': """
<%
 let message = 'Hello, World!'
%>
<%= message %>
    """
}