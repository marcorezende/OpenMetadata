# generated by datamodel-codegen:
#   filename:  security/credentials/basicAuth.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from pydantic import BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr


class BasicAuth(BaseModel):
    class Config:
        extra = Extra.forbid

    username: str = Field(
        ..., description='Username to access the service.', title='Username'
    )
    password: CustomSecretStr = Field(
        ..., description='Password to access the service.', title='Password'
    )
