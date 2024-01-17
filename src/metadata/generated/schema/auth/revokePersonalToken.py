# generated by datamodel-codegen:
#   filename:  auth/revokePersonalToken.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ..type import basic


class RevokePersonalToken(BaseModel):
    class Config:
        extra = Extra.forbid

    tokenIds: Optional[List[basic.Uuid]] = Field(
        None, description='Ids of Personal Access Tokens to remove.'
    )
