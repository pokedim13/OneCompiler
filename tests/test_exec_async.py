import os

import pytest
from dotenv import load_dotenv

from onecompiler import AsyncOneCompiler, models

load_dotenv()

compiler = AsyncOneCompiler(os.getenv("token"))

@pytest.mark.asyncio
async def test_exec() -> None:
    file1 = models.File(name="test.py", content="print('Я ГЕЕЕЕЕЕЕЙ')")
    assert isinstance(
        await compiler.Compiler.exec("python", [{"name": "main.py", "content": "import test"}, file1]), 
        models.ExecModel
    )