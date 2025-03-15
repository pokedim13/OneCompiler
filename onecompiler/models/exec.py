from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class File(BaseModel):
    name: str
    content: str


class Properties(BaseModel):
    language: str
    docs: bool | None = None
    tutorials: bool | None = None
    cheatsheets: bool | None = None
    files_editable: bool = Field(None, alias="filesEditable")
    files_deletable: bool = Field(None, alias="filesDeletable")
    files: list[File]
    outbound: str


class Job(BaseModel):
    name: str | None = None
    title: str | None = None
    version: str = None
    mode: str | None = None
    description: Any | None = None
    extension: str | None = None
    concurrent_jobs: int = Field(None, alias="concurrentJobs")
    language_type: str | None = Field(None, alias="languageType")
    active: bool | None = None
    properties: Properties
    visibility: str | None = None
    id: str = Field(..., alias="_id")


class ExecModel(BaseModel):
    exception: Any
    stdout: str = None
    stderr: Any
    execution_time: int | None = Field(None, alias="executionTime")
    job: Job = None
    new_visibility: Any = Field(..., alias="newVisibility")