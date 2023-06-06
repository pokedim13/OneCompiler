from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class File(BaseModel):
    name: str
    content: str


class Properties(BaseModel):
    language: str
    docs: bool
    tutorials: bool
    cheatsheets: bool
    filesEditable: bool
    filesDeletable: bool
    files: List[File]


class Lang(BaseModel):
    name: str
    title: str
    version: str
    mode: str
    description: Any
    extension: str
    concurrentJobs: int
    languageType: str
    active: bool
    properties: Properties
    visibility: str