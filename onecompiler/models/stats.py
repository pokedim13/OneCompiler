from __future__ import annotations

from pydantic import BaseModel, Field


class StatsModel(BaseModel):
    total_workspaces: int = Field(..., alias="totalWorkspaces")
    total_running_workspaces: int = Field(..., alias="totalRunningWorkspaces")
    total_workspaces_today: int = Field(..., alias="totalWorkspacesToday")
    total_workspaces_yesterday: int = Field(..., alias="totalWorkspacesYesterday")
    total_workspaces_last7_days: int = Field(..., alias="totalWorkspacesLast7Days")
    total_workspaces_last7_days_previous: int = Field(
        ..., alias="totalWorkspacesLast7DaysPrevious"
    )