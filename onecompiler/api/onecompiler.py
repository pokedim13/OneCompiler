from httpx import Client, Response

from onecompiler.base import BaseOneCompiler
from onecompiler.models import StatsModel, TemplatesModel, WorkspaceModel, WorkspacesModel


class OneCompiler(BaseOneCompiler):
    class Compiler(BaseOneCompiler.Compiler["OneCompiler"]):
        ...

    class Studio(BaseOneCompiler.Studio["OneCompiler"]):
        def get_templates(self) -> dict:
            res = self.onecompiler._client.get("https://onecompiler.com/studio")
            res: TemplatesModel = self.onecompiler._get_model(TemplatesModel, self._parse_templates(res))
            return res
        
        def launch(self, template_name: str) -> WorkspaceModel:
            res = self.onecompiler._client.post(f"{self.onecompiler.url}{self.prefix}workspace/launch", json={"templateId": template_name})
            res: WorkspaceModel = self.onecompiler._get_model(WorkspaceModel, res.json())
            return res
        
        def stats(self) -> StatsModel:
            res = self.onecompiler._client.get(f"{self.onecompiler.url}{self.prefix}workspace/stats")
            res: StatsModel = self.onecompiler._get_model(StatsModel, res.json())
            return res
        
        def usage(self, id: str) -> Response:
            res = self.onecompiler._client.post(f"{self.onecompiler.url}{self.prefix}workspace/usage", json={"templateId": id})
            return res
        
        def workspace(self, id: str) -> WorkspaceModel:
            res = self.onecompiler._client.get(f"{self.onecompiler.url}{self.prefix}workspace/{id}")
            res: WorkspaceModel = self.onecompiler._get_model(WorkspaceModel, res.json())
            return res
        
        def workspaces(self) -> WorkspacesModel:
            res = self.onecompiler._client.get(f"{self.onecompiler.url}{self.prefix}workspaces")
            res: WorkspacesModel = self.onecompiler._get_model(WorkspacesModel, res.json())
            return res

    def __init__(self, token: str = None):
        super().__init__(token)
        self._client = Client(headers=self.get_headers())

    def get_notifications(self) -> int:
        res = self._client.get(f"{self.url}notifications/getNotificationsCount")
        res = res.json().get("count")
        return res