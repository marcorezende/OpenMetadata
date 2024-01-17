# generated by datamodel-codegen:
#   filename:  api/teams/createPersona.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ...type import basic


class CreatePersonaRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: basic.EntityName
    displayName: Optional[str] = Field(
        None,
        description="Optional name used for display purposes. Example 'Data Steward'.",
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Optional description of the team.'
    )
    users: Optional[List[basic.Uuid]] = Field(
        None, description='Optional IDs of users that are going to assign a Persona.'
    )
