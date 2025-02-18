from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field, RootModel


class Metadata(BaseModel):
    url: str
    url_from_node: str = Field(..., alias="urlFromNode")


class Template(BaseModel):
    _id: str


class Node(BaseModel):
    _id: str


class NodeManager(BaseModel):
    _id: str


class PortMappingItem(BaseModel):
    container_port: int = Field(..., alias="containerPort")
    node_port: int = Field(..., alias="nodePort")


class User(BaseModel):
    _id: str


class UsageCurrent(BaseModel):
    start: str
    end: str


class WorkspaceModel(BaseModel):
    _id: str
    created: str
    metadata: Metadata
    template: Template
    user_ip: str = Field(..., alias="userIp")
    node: Node
    pass_code: str = Field(..., alias="passCode")
    node_manager: NodeManager = Field(..., alias="nodeManager")
    status: str
    port_mapping: list[PortMappingItem] = Field(..., alias="portMapping")
    expiry: str
    user: User
    last_seen: str = Field(..., alias="lastSeen")
    usage_current: UsageCurrent = Field(..., alias="usageCurrent")
    usage_history: list = Field(..., alias="usageHistory")
    name: str
    properties: dict[str, Any]

class WorkspacesModel(RootModel):
    root: list[WorkspaceModel]