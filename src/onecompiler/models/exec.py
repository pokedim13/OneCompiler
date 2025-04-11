from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

# All aliased fields use camelCase to match the API response structure


class File(BaseModel):
    """Model for representing a file in the execution context."""
    name: str
    content: str


class Properties(BaseModel):
    """Model for representing execution environment properties."""
    language: str
    docs: bool | None = None
    tutorials: bool | None = None
    cheatsheets: bool | None = None
    files_editable: bool | None = Field(None, alias="filesEditable")
    files_deletable: bool | None = Field(None, alias="filesDeletable")
    files: list[File]
    outbound: str


class Job(BaseModel):
    """Model for representing an execution job."""
    name: str | None = None
    title: str | None = None
    version: str | None = None
    mode: str | None = None
    description: Any | None = None
    extension: str | None = None
    concurrent_jobs: int | None = Field(None, alias="concurrentJobs")
    language_type: str | None = Field(None, alias="languageType")
    active: bool | None = None
    properties: Properties
    visibility: str | None = None
    id: str = Field(..., alias="_id")


class ExecModel(BaseModel):
    """Model for representing execution results."""
    exception: Any
    stdout: str | None = None
    stderr: Any
    execution_time: int | None = Field(None, alias="executionTime")
    job: Job | None = None
    new_visibility: Any = Field(..., alias="newVisibility")