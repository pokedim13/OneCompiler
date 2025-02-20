from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, RootModel, Field


class Data(BaseModel):
    queries: List


class Region(BaseModel):
    region_name: str = Field(..., alias='RegionName')
    region_opt_status: str = Field(..., alias='RegionOptStatus')


class Metadata(BaseModel):
    host: Optional[str] = None
    port: Optional[str] = None
    db: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    url: Optional[str] = None
    url_from_node: Optional[str] = Field(None, alias='urlFromNode')
    regions: Optional[List[Region]] = None
    selected_region: Optional[str] = Field(None, alias='selectedRegion')


class Template(BaseModel):
    _id: str


class Node(BaseModel):
    _id: str


class NodeManager(BaseModel):
    _id: str


class PortMappingItem(BaseModel):
    container_port: int = Field(..., alias='containerPort')
    node_port: int = Field(..., alias='nodePort')


class User(BaseModel):
    _id: str


class UsageCurrentItem(BaseModel):
    start: str
    end: str


class UsageHistoryItem(BaseModel):
    start: str
    end: str


class WorkspaceModel(BaseModel):
    _id: str
    created: str
    data: Optional[Data] = None
    metadata: Metadata
    template: Template
    user_ip: str = Field(..., alias='userIp')
    node: Optional[Node] = None
    pass_code: str = Field(..., alias='passCode')
    node_manager: NodeManager = Field(..., alias='nodeManager')
    status: str
    port_mapping: Union[Dict[str, Any], List[PortMappingItem]] = Field(
        ..., alias='portMapping'
    )
    expiry: str
    user: User
    last_seen: str = Field(..., alias='lastSeen')
    usage_current: Optional[UsageCurrentItem] = Field(..., alias='usageCurrent')
    usage_history: List[UsageHistoryItem] = Field(..., alias='usageHistory')
    name: str
    properties: Dict[str, Any]
    usage_total: Optional[int] = Field(None, alias='usageTotal')
    backup: Optional[str] = None


class WorkspacesModel(RootModel):
    root: List[WorkspaceModel]
