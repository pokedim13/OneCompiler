import os

from dotenv import load_dotenv
from httpx import Response

from onecompiler import OneCompiler, models

load_dotenv()

compiler = OneCompiler(os.getenv("token"))

def test_templates() -> None:
    assert isinstance(compiler.Studio.get_templates(), models.TemplatesModel)

def test_stats() -> None:
    assert isinstance(compiler.Studio.stats(), models.StatsModel)

def test_launch_and_delete() -> None:
    assert isinstance(res := compiler.Studio.launch("python"), models.WorkspaceModel)
    assert isinstance(compiler.Studio.delete(res.id), Response)

def test_usage() -> None:
    assert isinstance(compiler.Studio.usage("43bruh85w"), Response)

def test_workspace() -> None:
    assert isinstance(compiler.Studio.workspace("43bruh85w"), models.WorkspaceModel)

def test_workspaces() -> None:
    assert isinstance(compiler.Studio.workspaces(), models.WorkspacesModel)
    