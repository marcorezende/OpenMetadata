# generated by datamodel-codegen:
#   filename:  api/createBot.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ..entity.teams import user
from ..type import basic


class CreateBot(BaseModel):
    class Config:
        extra = Extra.forbid

    name: user.EntityName = Field(..., description='Name of the bot.')
    displayName: Optional[str] = Field(
        None,
        description="Name used for display purposes. Example 'FirstName LastName'.",
    )
    botUser: str = Field(
        ...,
        description='Bot user name created for this bot on behalf of which the bot performs all the operations, such as updating description, responding on the conversation threads, etc.',
    )
    description: Optional[str] = Field(None, description='Description of the bot.')
    provider: Optional[basic.ProviderType] = basic.ProviderType.user
