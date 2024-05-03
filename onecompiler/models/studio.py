from __future__ import annotations
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, RootModel, Field


class StatsModel(BaseModel):
    totalWorkspaces: int
    totalRunningWorkspaces: int
    totalWorkspacesToday: int
    totalWorkspacesYesterday: int
    totalWorkspacesLast7Days: int
    totalWorkspacesLast7DaysPrevious: int

class WorkspasesModel(RootModel):
    class ModelItem(BaseModel):
        class UsageHistoryItem(BaseModel):
            start: str
            end: str

        class UsageCurrentItem(BaseModel):
            start: str
            end: str            

        class User(BaseModel):
            _id: str

        class PortMappingItem(BaseModel):
            containerPort: int
            nodePort: int

        class NodeManager(BaseModel):
            _id: str

        class Node(BaseModel):
            _id: str

        class Template(BaseModel):
            _id: str

        class Metadata(BaseModel):
            url: str
            urlFromNode: str            

        _id: str
        created: str
        metadata: Metadata
        template: Template
        node: Node
        passCode: str
        nodeManager: NodeManager
        status: str
        portMapping: List[PortMappingItem]
        expiry: str
        user: User
        lastSeen: str
        usageCurrent: Optional[UsageCurrentItem]
        usageHistory: List[UsageHistoryItem]
        properties: Dict[str, Any]
        usageTotal: Optional[int] = None
        backup: Optional[str] = None    
    root: List[ModelItem]


class Workspace: 
    class UsageModel(BaseModel):
        status: str

    class WorkspaceModel(BaseModel):

        class UsageCurrent(BaseModel):
            start: str
            end: str

        class User(BaseModel):
            _id: str  

        class PortMappingItem(BaseModel):
            containerPort: int
            nodePort: int      

        class NodeManager(BaseModel):
            _id: str

        class Node(BaseModel):
            _id: str

        class Template(BaseModel):
            _id: str

        class Metadata(BaseModel):
            url: str
            urlFromNode: str

        id: str = Field(alias="_id")
        created: str
        metadata: Metadata
        template: Template
        node: Node
        passCode: str
        nodeManager: NodeManager
        status: str
        portMapping: List[PortMappingItem]
        expiry: str
        user: User
        lastSeen: str
        usageCurrent: UsageCurrent
        usageHistory: List
        properties: Dict[str, Any]
