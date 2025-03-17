import os

from dotenv import load_dotenv
from httpx import Response

from onecompiler import OneCompiler, models

load_dotenv()

compiler = OneCompiler(os.getenv("token"))

def test_exec() -> None:
    assert isinstance(compiler.Compiler.exec(
        lang="nodejs",
        files=[
    {
        "name": "index.js",
        "content": "console.log(\"Hello, World!\");"
    }
]
    ), models.ExecModel)