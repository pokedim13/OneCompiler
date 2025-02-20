from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from httpx import Response
from bs4 import BeautifulSoup, ResultSet

from onecompiler.models import TemplatesModel, WorkspaceModel, WorkspacesModel, StatsModel

T = TypeVar("T", bound="BaseOneCompiler")
class BaseOneCompiler(ABC):
    class Compiler(ABC, Generic[T]):
        def __init__(self, onecompiler: T) -> None:
            self.onecompiler = onecompiler

    class Studio(ABC, Generic[T]):
        prefix = "studio/"
        def __init__(self, onecompiler: T) -> None:
            self.onecompiler = onecompiler

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
        def get_templates(self) -> TemplatesModel:
            """Get templates for create vm or database."""
        
        def launch(self, template_name: str) -> WorkspaceModel:
            """Launch workspace."""
            return self.onecompiler._request("POST",
                                             model=WorkspaceModel,
                                             url=f"{self.onecompiler._url}{self.prefix}workspace/launch",
                                             json={"templateId": template_name})
        
        def stats(self) -> StatsModel:
            """Stats for live containers."""
            return self.onecompiler._request("GET",
                                             model=StatsModel,
                                             url=f"{self.onecompiler._url}{self.prefix}workspace/stats")
        
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

    _url = "https://onecompiler.com/api/"
    def __init__(self, token: str = None):
        self.compiler = self.Compiler(self)
        self.studio = self.Studio(self)
        self._token = token

    def get_headers(self) -> dict:
        return {"Authorization": f"Bearer {self._token}"}

    def get_notifications(self) -> Response:
        """Return count notifications"""

    @abstractmethod
    def _request[Model](self, method: str, model: Model = None, **kwargs) -> Response | Model:
        ...