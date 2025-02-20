from __future__ import annotations

from pydantic import BaseModel, RootModel


class TemplateModel(BaseModel):
    id: int
    template: str
    name: str
    specification: str


class TemplatesModel(RootModel):
    root: list[TemplateModel]