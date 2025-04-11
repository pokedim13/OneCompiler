import os
import asyncio

import pytest
import pytest_asyncio
from dotenv import load_dotenv
from httpx import Response

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
async def test_templates() -> None:
    """Тест получения шаблонов."""
    assert isinstance(await compiler.Studio.get_templates(), models.TemplatesModel)

@pytest.mark.asyncio
async def test_stats() -> None:
    """Тест получения статистики."""
    assert isinstance(await compiler.Studio.stats(), models.StatsModel)

@pytest.mark.asyncio
async def test_launch_and_delete() -> None:
    """Тест создания и удаления рабочего пространства."""
    assert isinstance(res := await compiler.Studio.launch("python"), models.WorkspaceModel)
    assert isinstance(await compiler.Studio.delete(res.id), Response)

@pytest.mark.asyncio
async def test_usage() -> None:
    """Тест обновления статуса использования."""
    assert isinstance(await compiler.Studio.usage("43bruh85w"), Response)

@pytest.mark.asyncio
async def test_workspace() -> None:
    """Тест получения рабочего пространства."""
    assert isinstance(await compiler.Studio.workspace("43bruh85w"), models.WorkspaceModel)

@pytest.mark.asyncio
async def test_workspaces() -> None:
    """Тест получения списка рабочих пространств."""
    assert isinstance(await compiler.Studio.workspaces(), models.WorkspacesModel)
    