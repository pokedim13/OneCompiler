from __future__ import annotations

from typing import Any, List, Optional
from pydantic import BaseModel, Field


class File(BaseModel):
    name: str
    content: str


class Properties(BaseModel):
    language: str
    docs: bool | None = None
    tutorials: bool | None = None
    cheatsheets: bool | None = None
    filesEditable: bool = None
    filesDeletable: bool = None
    files: List[File]
    outbound: str


class Job(BaseModel):
    name: str | None = None
    title: str | None = None
    version: str = None
    mode: str | None = None
    description: Any | None = None
    extension: str | None = None
    concurrentJobs: int = None
    languageType: str | None = None
    active: bool | None = None
    properties: Properties
    visibility: str | None = None
    id: str = Field(..., alias="_id")


class ExecModel(BaseModel):
    exception: Any
    stdout: str = None
    stderr: Any
    executionTime: int = None
    job: Job = None
    newVisibility: Any