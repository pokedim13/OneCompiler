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
    outbound: str


class Job(BaseModel):
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
    _id: str


class Response(BaseModel):
    exception: Any
    stdout: str = None
    stderr: Any
    executionTime: int = None
    job: Job = None
    newVisibility: Any
