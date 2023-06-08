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
    outbound: str


class Job(BaseModel):
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
    _id: str


class Response(BaseModel):
    exception: Any
    stdout: str = None
    stderr: Any
    executionTime: int = None
    job: Job = None
    newVisibility: Any