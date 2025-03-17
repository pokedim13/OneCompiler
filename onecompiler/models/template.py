from __future__ import annotations

from bs4 import BeautifulSoup, ResultSet
from httpx import Response
from pydantic import BaseModel, RootModel


class TemplateModel(BaseModel):
    id: int
    template: str
    name: str
    specification: str


class TemplatesModel(RootModel):
    root: list[TemplateModel]

    @classmethod
    def from_response(cls, response: Response) -> TemplatesModel:
        soup = BeautifulSoup(response.content, "html.parser")
        cards: ResultSet = soup.find_all("div", {"style": "display:flex;justify-content:space-between;align-items:center"})
        results = []
        
        for id, data in enumerate(cards):
            name: str = data.find("h6").text.strip()
            template = name.lower().replace(" ", "-")
            specification = data.find("span").text.strip()
            
            structure = {"id": id, "template": template, "name": name, "specification": specification}
            results.append(structure)

        # Валидация данных с использованием Pydantic
        return cls(root=results)