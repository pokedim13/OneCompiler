from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from bs4 import BeautifulSoup, ResultSet
from httpx import Response
from pydantic import __version__ as pydantic_version

from onecompiler.models import StatsModel, TemplatesModel, WorkspaceModel, WorkspacesModel

T = TypeVar("T", bound="BaseOneCompiler")
class BaseOneCompiler(ABC):
    class Compiler(ABC, Generic[T]):
        def __init__(self, onecompiler: T) -> None:
            self.onecompiler = onecompiler

    class Studio(ABC, Generic[T]):
        prefix = "studio/"
        def __init__(self, onecompiler: T) -> None:
            self.onecompiler = onecompiler

        @abstractmethod
        def get_templates(self) -> TemplatesModel:
            """Get templates for create vm or database."""

        @staticmethod
        def _parse_templates(response: Response) -> list[dict]:
            soup = BeautifulSoup(response.content, "html.parser")
            cards: ResultSet = soup.find_all("div", {"style":"display:flex;justify-content:space-between;align-items:center"})
            results = []
            for id, data in enumerate(cards):
                name: str = data.find("h6").text
                template = name.lower().replace(" ", "-")
                
                specification = data.find("span").text
            
                structure = {"id": id, "template": template, "name": name, "specification": specification}
                results.append(structure)
            return results

        @abstractmethod
        def launch(self, template_name: str) -> WorkspaceModel:
            """Launch workspace."""

        @abstractmethod
        def stats(self) -> StatsModel:
            """Stats for live containers."""

        @abstractmethod
        def usage(self, id: str) -> Response:
            """Indicate that you are still using workspace so that it does not turn off."""

        @abstractmethod
        def workspace(self, id: str) -> WorkspaceModel:
            """Get workspace data (backup)."""

        @abstractmethod
        def workspaces(self) -> WorkspacesModel:
            """Get all user workspaces."""

    url = "https://onecompiler.com/api/"
    def __init__(self, token: str = None):
        self.compiler = self.Compiler(self)
        self.studio = self.Studio(self)
        self._token = token

    def get_headers(self) -> dict:
        return {"Authorization": f"Bearer {self._token}"}
    
    @staticmethod
    def _get_model[Model](model: Model, data: any) -> Model:
        if pydantic_version.split(".")[0] == "1":
            return model.parse_obj(data)
        if pydantic_version.split(".")[0] == "2":
            return model.model_validate(data)
        raise ValueError("support pydantic version not found")
    
    @abstractmethod
    def get_notifications(self) -> Response:
        """Return count notifications"""