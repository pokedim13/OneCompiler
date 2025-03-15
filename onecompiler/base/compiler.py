from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from httpx import Response

from onecompiler.models import ExecModel, StatsModel, TemplatesModel, WorkspaceModel, WorkspacesModel

T = TypeVar("T", bound="BaseOneCompiler")
class BaseOneCompiler(ABC):
    class Compiler(ABC, Generic[T]):
        prefix = "code/"
        def __init__(self, onecompiler: T) -> None:
            self.onecompiler = onecompiler

        @staticmethod
        def _get_exec_data(lang: str, files: list) -> dict:
            return {
                "properties": {
                    "language": lang,
                    "files": files
                },
            }

        def exec(self, lang: str, files: list) -> ExecModel:
            return self.onecompiler._request("POST",
                                                model=ExecModel,
                                                url=f"{self.onecompiler._url}{self.prefix}exec",
                                                json=self._get_exec_data(lang, files))

    class Studio(ABC, Generic[T]):
        prefix = "studio/"
        def __init__(self, onecompiler: T) -> None:
            self.onecompiler = onecompiler

        @abstractmethod
        def get_templates(self) -> TemplatesModel:
            """Get templates for DB and VM."""

        def stats(self) -> StatsModel:
            """Stats for live containers."""
            return self.onecompiler._request("GET",
                                             model=StatsModel,
                                             url=f"{self.onecompiler._url}{self.prefix}workspace/stats")

        def launch(self, template_name: str) -> WorkspaceModel:
            """Launch workspace."""
            return self.onecompiler._request("POST",
                                             model=WorkspaceModel,
                                             url=f"{self.onecompiler._url}{self.prefix}workspace/launch",
                                             json={"templateId": template_name})

        def usage(self, id: str) -> Response:
            """Indicate that you are still using workspace so that it does not turn off."""
            return self.onecompiler._request("POST",
                                             url=f"{self.onecompiler._url}{self.prefix}workspace/usage",
                                             json={"templateId": id})

        def workspace(self, id: str) -> WorkspaceModel:
            """Get workspace data (backup)."""
            return self.onecompiler._request("GET",
                                             model=WorkspaceModel,
                                             url=f"{self.onecompiler._url}{self.prefix}workspace/{id}")

        def workspaces(self) -> WorkspacesModel:
            """Get all user workspaces."""
            return self.onecompiler._request("GET",
                                             model=WorkspacesModel,
                                             url=f"{self.onecompiler._url}{self.prefix}workspaces")

        def delete(self, id: str) -> Response:
            """Get workspace data (backup)."""
            return self.onecompiler._request("DELETE",
                                             url=f"{self.onecompiler._url}{self.prefix}workspace/{id}")

    _url = "https://onecompiler.com/api/"
    def __init__(self, token: str = None):
        self.Compiler = self.Compiler(self)
        self.Studio = self.Studio(self)
        self._token = token

    def get_headers(self) -> dict:
        return {"Authorization": f"Bearer {self._token}"}

    def get_notifications(self) -> Response:
        return self._request("GET", url=f"{self._url}notifications/getNotificationsCount")

    @abstractmethod
    def _request[Model](self, method: str, model: Model = None, **kwargs) -> Response | Model:
        ...