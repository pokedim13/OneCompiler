from __future__ import annotations
from typing import Any, List, Optional
from pydantic import BaseModel


class NewFileOption(BaseModel):
    helpText: str
    name: str
    content: str

class File(BaseModel):
    name: str
    content: str

class LangModel(BaseModel):

    class Properties(BaseModel):
        language: str
        docs: bool
        tutorials: bool
        cheatsheets: bool
        filesEditable: bool = None
        filesDeletable: bool = None
        files: List[File]
        newFileOptions: List[NewFileOption] = None

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

class ResponceModel(BaseModel):
    class Job(BaseModel):

        class Properties(BaseModel):
            language: str
            docs: bool
            tutorials: bool
            cheatsheets: bool
            filesEditable: bool = None
            filesDeletable: bool = None
            files: List[File]
            newFileOptions: List[NewFileOption] = None
            outbound: str

        name: str
        title: str
        version: str
        mode: str
        description: Any = None
        extension: str
        concurrentJobs: int = None
        languageType: str
        active: bool
        properties: Properties
        visibility: str
        _id: str

    exception: Any = None
    stdout: str
    stderr: Any = None
    executionTime: int = None
    job: Job = None
    newVisibility: Any
