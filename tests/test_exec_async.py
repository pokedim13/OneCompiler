import os

import pytest
from dotenv import load_dotenv
from httpx import Response

from onecompiler import AsyncOneCompiler, models

load_dotenv()

compiler = AsyncOneCompiler(os.getenv("token"))

@pytest.mark.asyncio
async def test_exec() -> None:
    assert isinstance(await compiler.Compiler.exec(
        lang="nodejs",
        files=[
    {
        "name": "index.js",
        "content": "console.log(\"Hello, World!\");"
    }
]
    ), models.ExecModel)