from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field, RootModel


class Data(BaseModel):
    queries: list


class Region(BaseModel):
    region_name: str = Field(..., alias="RegionName")
    region_opt_status: str = Field(..., alias="RegionOptStatus")


class Metadata(BaseModel):
    host: str | None = None
    port: str | None = None
    db: str | None = None
    username: str | None = None
    password: str | None = None
    url: str | None = None
    url_from_node: str | None = Field(None, alias="urlFromNode")
    regions: list[Region] | None = None
    selected_region: str | None = Field(None, alias="selectedRegion")


class Template(BaseModel):
    id: str = Field(..., alias="_id")


class Node(BaseModel):
    id: str = Field(..., alias="_id")


class NodeManager(BaseModel):
    id: str = Field(..., alias="_id")


class PortMappingItem(BaseModel):
    container_port: int = Field(..., alias="containerPort")
    node_port: int = Field(..., alias="nodePort")


class User(BaseModel):
    id: str = Field(..., alias="_id")


class UsageCurrentItem(BaseModel):
    start: str
    end: str


class UsageHistoryItem(BaseModel):
    start: str
    end: str


class WorkspaceModel(BaseModel):
    id: str = Field(..., alias="_id")
    created: str
    data: Data | None = None
    metadata: Metadata
    template: Template
    user_ip: str = Field(..., alias="userIp")
    node: Node | None = None
    pass_code: str = Field(..., alias="passCode")
    node_manager: NodeManager = Field(..., alias="nodeManager")
    status: str
    port_mapping: dict[str, Any] | list[PortMappingItem] = Field(
        ..., alias="portMapping"
    )
    expiry: str
    user: User
    last_seen: str = Field(..., alias="lastSeen")
    usage_current: UsageCurrentItem | None = Field(..., alias="usageCurrent")
    usage_history: list[UsageHistoryItem] = Field(..., alias="usageHistory")
    name: str
    properties: dict[str, Any]
    usage_total: int | None = Field(None, alias="usageTotal")
    backup: str | None = None


class WorkspacesModel(RootModel):
    root: list[WorkspaceModel]