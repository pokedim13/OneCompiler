from __future__ import annotations
from typing import TYPE_CHECKING
from onecompiler.models import studio
if TYPE_CHECKING:
    from onecompiler.client import OneCompiler


class BaseStudio:
    _url = "https://onecompiler.com/api/studio/"

class Studio(BaseStudio):
    def __init__(self, client: OneCompiler):
        self._client = client

    async def workspaces(self):
        res = await self._client._client.get(self._url + "workspaces")
        res = studio.WorkspasesModel.model_validate(res.json())
        return res
    
    async def workspace(self, id: str):
        res = await self._client._client.get(self._url + f"workspace/{id}")
        res = studio.Workspace.WorkspaceModel.model_validate(res.json())
        return res
    
    async def stats(self):
        res = await self._client._client.get(self._url + "workspace/stats")
        res = studio.StatsModel.model_validate(res.json())
        return res

    async def launch(self, template_name: str):
        data = {"templateId": template_name}
        res = await self._client._client.post(self._url + "workspace/launch", json=data)
        res = studio.Workspace.WorkspaceModel.model_validate(res.json())
        return res
    
    async def usage(self, id: str):
        data = {"_id": id}
        res = await self._client._client.post(self._url + "workspace/usage", json=data)
        res = studio.Workspace.UsageModel.model_validate(res.json())
        return res
