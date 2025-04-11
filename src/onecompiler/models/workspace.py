from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field, RootModel

# All aliased fields use camelCase to match the API response structure


class Data(BaseModel):
    """Model for representing workspace query data."""
    queries: list = []


class Region(BaseModel):
    """Model for representing a deployment region."""
    region_name: str = Field(..., alias="RegionName")
    region_opt_status: str = Field(..., alias="RegionOptStatus")


class Metadata(BaseModel):
    """Model for representing workspace metadata."""
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
    """Model for representing a workspace template."""
    id: str = Field(..., alias="_id")


class Node(BaseModel):
    """Model for representing a node."""
    id: str = Field(..., alias="_id")


class NodeManager(BaseModel):
    """Model for representing a node manager."""
    id: str = Field(..., alias="_id")


class PortMappingItem(BaseModel):
    """Model for representing a port mapping entry."""
    container_port: int = Field(..., alias="containerPort")
    node_port: int = Field(..., alias="nodePort")


class User(BaseModel):
    """Model for representing a user."""
    id: str = Field(..., alias="_id")


class UsageCurrentItem(BaseModel):
    """Model for representing current usage time period."""
    start: str
    end: str


class UsageHistoryItem(BaseModel):
    """Model for representing a historical usage time period."""
    start: str
    end: str


class WorkspaceModel(BaseModel):
    """Model for representing a workspace."""
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
        ..., alias="portMapping",
    )
    expiry: str
    user: User
    last_seen: str = Field(..., alias="lastSeen")
    usage_current: UsageCurrentItem | None = Field(None, alias="usageCurrent")
    usage_history: list[UsageHistoryItem] = Field([], alias="usageHistory")
    name: str
    properties: dict[str, Any] = {}
    usage_total: int | None = Field(None, alias="usageTotal")
    backup: str | None = None


class WorkspacesModel(RootModel):
    """Model for representing a collection of workspaces."""
    root: list[WorkspaceModel] = []