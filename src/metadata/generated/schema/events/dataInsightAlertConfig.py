# generated by datamodel-codegen:
#   filename:  events/dataInsightAlertConfig.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field


class DataInsightAlertConfig(BaseModel):
    class Config:
        extra = Extra.forbid

    sendToAdmins: Optional[bool] = Field(False, description='Send the Mails to Admins')
    sendToTeams: Optional[bool] = Field(False, description='Send the Mails to Teams')
