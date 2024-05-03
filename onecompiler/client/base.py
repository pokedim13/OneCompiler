from httpx import AsyncClient
from abc import ABC, abstractmethod
from onecompiler.api.compiler import Compiler
from onecompiler.api.studio import Studio

class BaseCompiler:
    _headers = {
		"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
	}
    _token: str
    def get_headers(self):
        return {"Authorization": f"Bearer {self._token}"} | self._headers

class OneCompiler(BaseCompiler):
    def __init__(self, token: str = None) -> None:
        self._token = token
        self._client = AsyncClient(headers=self.get_headers())
        self.compiler = Compiler(self)
        if token:
            self.studio = Studio(self)

    async def get_notifications(self) -> dict:
        url = "https://onecompiler.com/api/notifications/getNotificationsCount"
        res = await self._client.get(url)
        return res.json()