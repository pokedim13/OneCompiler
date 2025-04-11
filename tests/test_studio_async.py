import os

import pytest
from dotenv import load_dotenv
from httpx import Response

from onecompiler import AsyncOneCompiler, models

load_dotenv()

compiler = AsyncOneCompiler(os.getenv("token"))

@pytest.mark.asyncio
async def test_templates() -> None:
    assert isinstance(await compiler.Studio.get_templates(), models.TemplatesModel)

@pytest.mark.asyncio
async def test_stats() -> None:
    assert isinstance(await compiler.Studio.stats(), models.StatsModel)

@pytest.mark.asyncio
async def test_launch_and_delete() -> None:
    assert isinstance(res := await compiler.Studio.launch("python"), models.WorkspaceModel)
    assert isinstance(await compiler.Studio.delete(res.id), Response)

@pytest.mark.asyncio
async def test_usage() -> None:
    assert isinstance(await compiler.Studio.usage("43bruh85w"), Response)

@pytest.mark.asyncio
async def test_workspace() -> None:
    assert isinstance(await compiler.Studio.workspace("43bruh85w"), models.WorkspaceModel)

@pytest.mark.asyncio
async def test_workspaces() -> None:
    assert isinstance(await compiler.Studio.workspaces(), models.WorkspacesModel)
    