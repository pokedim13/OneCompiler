from httpx import AsyncClient, Client, Response

from onecompiler.base import BaseOneCompiler
from onecompiler.models import TemplatesModel


class OneCompiler(BaseOneCompiler):
    class Studio(BaseOneCompiler.Studio["OneCompiler"]):
        def get_templates(self) -> TemplatesModel:
            res = self.onecompiler._request("GET", 
                                                url="https://onecompiler.com/studio")
            return TemplatesModel.from_response(res)

    def __init__(self, token: str = None):
        super().__init__(token)
        self._client = Client(headers=self.get_headers())

    def _request[Model](self, method: str, model: Model = None, **kwargs) -> Response | Model:
        res = self._client.request(method=method, **kwargs)
        if model is not None:
            return model.model_validate(res.json())
        return res

class AsyncOneCompiler(BaseOneCompiler):
    class Studio(BaseOneCompiler.Studio["OneCompiler"]):
        async def get_templates(self) -> TemplatesModel:
            res = await self.onecompiler._request("GET", 
                                                url="https://onecompiler.com/studio")
            return TemplatesModel.from_response(res)

    def __init__(self, token: str = None):
        super().__init__(token)
        self._client = AsyncClient(headers=self.get_headers())

    async def _request[Model](self, method: str, model: Model = None, **kwargs) -> Response | Model:
        res = await self._client.request(method=method, **kwargs)
        if model is not None:
            return model.model_validate(res.json())
        return res