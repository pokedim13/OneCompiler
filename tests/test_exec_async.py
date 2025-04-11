import os

import pytest
import pytest_asyncio
from dotenv import load_dotenv

from onecompiler import AsyncOneCompiler, models

load_dotenv()

compiler = AsyncOneCompiler(os.getenv("token"))

@pytest_asyncio.fixture(scope="module", autouse=True)
async def cleanup():
    """Финализация ресурсов после всех тестов."""
    yield
    if hasattr(compiler, '_client') and hasattr(compiler._client, 'aclose'):
        await compiler._client.aclose()

@pytest.mark.asyncio
async def test_exec() -> None:
    """Тест функции exec с использованием моделей File."""
    file1 = models.File(name="test.py", content="print('Hello from test')")
    assert isinstance(
        await compiler.Compiler.exec("python", [{"name": "main.py", "content": "import test"}, file1]), 
        models.ExecModel,
    )