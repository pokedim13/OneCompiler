null, true, false = None, True, False
data = {
        "java":{
            "name": "Java",
            "title": "Java Hello World",
            "version": "11",
            "mode": "java",
            "description": null,
            "extension": "java",
            "concurrentJobs": 2,
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "java",
                "docs": true,
                "tutorials": false,
                "cheatsheets": true,
                "filesEditable": true,
                "filesDeletable": true,
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
		"py": {
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
				"files": [{"name": "main.py", "content": "{code}"}],
			},
			"visibility": "public",
		    },
        "c": {
			"name": "C",
			"title": "C Language Hello World",
			"version": "latest",
			"mode": "c_cpp",
			"description": null,
			"extension": "c",
			"languageType": "programming",
			"active": true,
			"properties": {
				"language": "c",
				"docs": true,
				"tutorials": true,
				"cheatsheets": true,
				"filesEditable": true,
				"filesDeletable": true,
				"files": [{"name": "Main.c", "content": "{code}"}],
			},
			"visibility": "public",
		    },
        "cpp": {
			"name": "C++",
			"title": "C++ Hello World",
			"version": "latest",
			"mode": "c_cpp",
			"description": null,
			"extension": "cpp",
			"languageType": "programming",
			"active": true,
			"properties": {
				"language": "cpp",
				"docs": true,
				"tutorials": true,
				"cheatsheets": true,
				"files": [{"name": "Main.cpp", "content": "{code}"}],
			},
			"visibility": "public",
		    },
        "node": {
            "name": "NodeJS",
            "title": "NodeJS Hello World",
            "version": "12.13",
            "mode": "javascript",
            "description": null,
            "extension": "js",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "nodejs",
                "docs": true,
                "tutorials": true,
                "cheatsheets": true,
                "filesEditable": true,
                "filesDeletable": true,
                "files": [{"name": "index.js","content": "{code}"}]
            },
            "visibility": "public"
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
				"files": [{"name": "index.js", "content": "{code}"}],
			},
			"visibility": "public",
		    },
        "groovy": {
            "name": "Groovy",
            "title": "Groovy Hello World",
            "mode": "groovy",
            "description": null,
            "extension": "groovy",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "groovy",
                "docs": true,
                "tutorials": true,
                "cheatsheets": true,
                "files": [{"name": "Main.groovy", "content": "{code}"}]
            },
            "visibility": "public"
            },
        "jsh": {
            "name": "JShell",
            "title": "JShell Hello World",
            "mode": "java",
            "description": null,
            "extension": "jsh",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "jshell",
                "docs": true,
                "tutorials": false,
                "cheatsheets": true,
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
            "description": null,
            "extension": "hs",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "haskell",
                "docs": true,
                "tutorials": false,
                "cheatsheets": false,
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
            "description": null,
            "extension": "tcl",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "tcl",
                "docs": true,
                "tutorials": false,
                "cheatsheets": false,
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
            "description": null,
            "extension": "lua",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "lua",
                "docs": true,
                "tutorials": false,
                "cheatsheets": false,
                "files": [
                {
                    "name": "Main.lua",
                    "content": "{code}"
                }
                ]
            },
            "visibility": "public"
            },
        "adb": {
            "name": "Ada",
            "title": "Ada Hello World!",
            "mode": "ada",
            "description": null,
            "extension": "adb",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "ada",
                "docs": true,
                "tutorials": false,
                "cheatsheets": false,
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
            "description": null,
            "extension": "lsp",
            "languageType": "programming",
            "active": true,
            "worker": "j",
            "workerId": 55,
            "properties": {
                "language": "commonlisp",
                "docs": true,
                "tutorials": false,
                "cheatsheets": false,
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
            "description": null,
            "extension": "d",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "d",
                "docs": true,
                "tutorials": false,
                "cheatsheets": false,
                "files": [
                {
                    "name": "HelloWorld.d",
                    "content": "{code}"
                }
                ]
            },
            "visibility": "public"
            },
        "ex": {
            "name": "Elixir",
            "title": "Elixir Hello World!",
            "mode": "c_cpp",
            "description": null,
            "extension": "ex",
            "languageType": "programming",
            "active": true,
            "worker": "j",
            "workerId": 57,
            "properties": {
                "language": "elixir",
                "docs": true,
                "tutorials": false,
                "cheatsheets": false,
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
            "description": null,
            "extension": "erl",
            "languageType": "programming",
            "active": true,
            "worker": "j",
            "workerId": 58,
            "properties": {
                "language": "erlang",
                "docs": true,
                "tutorials": false,
                "cheatsheets": false,
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
            "description": null,
            "extension": "fs",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "fsharp",
                "docs": true,
                "tutorials": false,
                "cheatsheets": false,
                "files": [
                {
                    "name": "HelloWorld.fs",
                    "content": "{code}"
                }
                ]
            },
            "visibility": "public"
            },
        "ftn": {
            "name": "Fortran",
            "title": "Fortran Hello World!",
            "mode": "fortran",
            "description": null,
            "extension": "ftn",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "fortran",
                "docs": true,
                "tutorials": false,
                "cheatsheets": false,
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
            "description": null,
            "extension": "asm",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "assembly",
                "docs": true,
                "tutorials": false,
                "cheatsheets": false,
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
            "description": null,
            "extension": "scala",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "scala",
                "docs": true,
                "tutorials": false,
                "cheatsheets": false,
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
            "description": null,
            "extension": "php",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "php",
                "docs": true,
                "tutorials": true,
                "cheatsheets": true,
                "files": [
                {
                    "name": "HelloWorld.php",
                    "content": "{code}"
                }
                ]
            },
            "visibility": "public"
            },
        "py2": {
            "name": "Python2",
            "title": "Python2 Hello World!",
            "mode": "python",
            "description": null,
            "extension": "py",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "python2",
                "docs": true,
                "tutorials": false,
                "cheatsheets": false,
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
            "description": null,
            "extension": "cs",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "csharp",
                "docs": true,
                "tutorials": true,
                "cheatsheets": true,
                "files": [
                {
                    "name": "HelloWorld.cs",
                    "content": "{code}"
                }
                ]
            },
            "visibility": "public"
            },
        "pl": {
            "name": "Perl",
            "title": "Perl Hello World!",
            "mode": "perl",
            "description": null,
            "extension": "pl",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "perl",
                "docs": true,
                "tutorials": true,
                "cheatsheets": true,
                "files": [
                {
                    "name": "HelloWorld.pl",
                    "content": "{code}"
                }
                ]
            },
            "visibility": "public"
            },
        "rb": {
            "name": "Ruby",
            "title": "Ruby Hello World!",
            "mode": "ruby",
            "description": null,
            "extension": "rb",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "ruby",
                "docs": true,
                "tutorials": true,
                "cheatsheets": true,
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
            "description": null,
            "extension": "go",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "go",
                "docs": true,
                "tutorials": true,
                "cheatsheets": true,
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
            "description": null,
            "extension": "r",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "r",
                "docs": true,
                "tutorials": true,
                "cheatsheets": true,
                "files": [
                {
                    "name": "HelloWorld.r",
                    "content": "{code}"
                }
                ]
            },
            "visibility": "public"
            },
        "rkt": {
            "name": "Racket",
            "title": "Racket Hello World!",
            "mode": "perl",
            "description": null,
            "extension": "rkt",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "racket",
                "docs": true,
                "tutorials": false,
                "cheatsheets": false,
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
            "description": null,
            "extension": "ml",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "ocaml",
                "docs": true,
                "tutorials": false,
                "cheatsheets": false,
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
            "description": null,
            "extension": "vb",
            "languageType": "programming",
            "active": true,
            "properties": {
                "language": "vb",
                "docs": true,
                "tutorials": true,
                "cheatsheets": true,
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
            "description": null,
            "extension": "sh",
            "languageType": "programming",
            "active": true,
            "worker": "j",
            "workerId": 46,
            "properties": {
                "language": "bash",
                "docs": false,
                "tutorials": false,
                "cheatsheets": false,
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
            "description": null,
            "extension": "clj",
            "languageType": "programming",
            "active": true,
            "worker": "j",
            "workerId": 86,
            "properties": {
                "language": "clojure",
                "docs": false,
                "tutorials": false,
                "cheatsheets": false,
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
            "description": null,
            "extension": "ts",
            "languageType": "programming",
            "active": true,
            "worker": "j",
            "workerId": 74,
            "properties": {
                "language": "typescript",
                "docs": false,
                "tutorials": false,
                "cheatsheets": false,
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
            "description": null,
            "extension": "cbl",
            "languageType": "programming",
            "active": true,
            "worker": "j",
            "workerId": 77,
            "properties": {
                "language": "cobol",
                "docs": false,
                "tutorials": false,
                "cheatsheets": false,
                "files": [
                {
                    "name": "HelloWorld.cbl",
                    "content": "{code}"
                }
                ],
                "result": {
                "success": true,
                "output": "Hello, World!\n"
                }
            },
            "visibility": "public"
            },
        "kt": {
            "name": "Kotlin",
            "title": "Kotlin Hello World!",
            "mode": "groovy",
            "description": null,
            "extension": "kt",
            "languageType": "programming",
            "active": true,
            "worker": "j",
            "workerId": 78,
            "properties": {
                "language": "kotlin",
                "docs": false,
                "tutorials": false,
                "cheatsheets": false,
                "files": [
                {
                    "name": "HelloWorld.kt",
                    "content": "{code}"
                }
                ]
            },
            "visibility": "public"
            },
        "pas": {
            "name": "Pascal",
            "title": "Pascal Hello World!",
            "mode": "javascript",
            "description": null,
            "extension": "pas",
            "languageType": "programming",
            "active": true,
            "worker": "j",
            "workerId": 67,
            "properties": {
                "language": "pascal",
                "docs": false,
                "tutorials": false,
                "cheatsheets": false,
                "files": [
                    {
                        "name": "HelloWorld.pas",
                        "content": "{code}"
                    }
                ]
            },
            "visibility": "public"
        },
        "pl": {
            "name": "Prolog",
            "title": "Prolog Hello World!",
            "mode": "javascript",
            "description": null,
            "extension": "pl",
            "languageType": "programming",
            "active": true,
            "worker": "j",
            "workerId": 69,
            "properties": {
                "language": "prolog",
                "docs": false,
                "tutorials": false,
                "cheatsheets": false,
                "files": [
                {
                    "name": "HelloWorld.pl",
                    "content": "{code}"
                }
                ]
            },
            "visibility": "public"
            },
        "rs": {
            "name": "Rust",
            "title": "Rust Hello World!",
            "mode": "c_cpp",
            "description": null,
            "extension": "rs",
            "languageType": "programming",
            "active": true,
            "worker": "j",
            "workerId": 73,
            "properties": {
                "language": "rust",
                "docs": false,
                "tutorials": false,
                "cheatsheets": false,
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
            "description": null,
            "extension": "swift",
            "languageType": "programming",
            "active": true,
            "worker": "j",
            "workerId": 83,
            "properties": {
                "language": "swift",
                "docs": false,
                "tutorials": false,
                "cheatsheets": false,
                "files": [
                {
                    "name": "HelloWorld.swift",
                    "content": "{code}"
                }
                ]
            },
            "visibility": "public"
            },
        "m": {
            "name": "Octave",
            "title": "Octave Hello World!",
            "mode": "javascript",
            "description": null,
            "extension": "m",
            "languageType": "programming",
            "active": true,
            "worker": "j",
            "workerId": 66,
            "properties": {
                "language": "octave",
                "docs": false,
                "tutorials": false,
                "cheatsheets": false,
                "files": [
                {
                    "name": "HelloWorld.m",
                    "content": "{code}"
                }
                ]
            },
            "visibility": "public"
            },
        "bf": {
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
            "description": null,
            "extension": "coffee",
            "languageType": "programming",
            "active": true,
            "worker": "s",
            "properties": {
                "language": "coffeescript",
                "docs": false,
                "tutorials": false,
                "cheatsheets": false,
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
            "description": null,
            "extension": "ejs",
            "languageType": "programming",
            "active": true,
            "worker": "s",
            "properties": {
                "language": "ejs",
                "docs": false,
                "tutorials": false,
                "cheatsheets": false,
                "files": [
                {
                    "name": "helloworld.ejs",
                    "content": "{code}"
                }
                ]
            },
            "visibility": "public"
            }
	}

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