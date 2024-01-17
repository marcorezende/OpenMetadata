# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/common/basicAuth.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr


class BasicAuth(BaseModel):
    class Config:
        extra = Extra.forbid

    password: Optional[CustomSecretStr] = Field(
        None, description='Password to connect to source.', title='Password'
    )
