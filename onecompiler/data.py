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
    "cobol": [
      "cobol",
      "cbl"
    ],
    "clojure": [
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
    "erlang": [
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
    "haskell": [
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
    "ocaml": [
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
    "bash": [
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