# generated by datamodel-codegen:
#   filename:  auth/logoutRequest.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ..type import basic


class LogoutRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    username: Optional[str] = Field(None, description='Logout Username')
    token: str = Field(..., description='Token To be Expired')
    logoutTime: Optional[basic.DateTime] = Field(None, description='Logout Time')
    refreshToken: Optional[str] = Field(None, description='Refresh Token')
