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
    filesEditable: bool = None
    filesDeletable: bool = None
    files: List[File]


class Lang(BaseModel):
    name: str
    title: str
    version: str = None
    mode: str
    description: Any
    extension: str
    concurrentJobs: int = None
    languageType: str
    active: bool
    properties: Properties
    visibility: str