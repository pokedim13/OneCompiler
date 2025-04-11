import os

from dotenv import load_dotenv

from onecompiler import OneCompiler, models

load_dotenv()

compiler = OneCompiler(os.getenv("token"))

def test_exec() -> None:
    file1 = models.File(name="test.py", content="print('Я ГЕЕЕЕЕЕЕЙ')")
    assert isinstance(
        compiler.Compiler.exec("python", [{"name": "main.py", "content": "import test"}, file1]), 
        models.ExecModel,
    )