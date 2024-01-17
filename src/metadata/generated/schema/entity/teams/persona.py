# generated by datamodel-codegen:
#   filename:  entity/teams/persona.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ...type import basic, entityHistory, entityReferenceList


class Team(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid
    name: basic.EntityName = Field(
        ..., description="A unique name of Persona. Example 'data engineer'"
    )
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='FullyQualifiedName same as `name`.'
    )
    displayName: Optional[str] = Field(
        None, description="Name used for display purposes. Example 'Data Steward'."
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Description of the persona.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this entity.'
    )
    users: Optional[entityReferenceList.EntityReferenceList] = Field(
        None, description='Users that are assigned a persona.'
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
