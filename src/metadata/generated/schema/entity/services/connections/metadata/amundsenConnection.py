# generated by datamodel-codegen:
#   filename:  entity/services/connections/metadata/amundsenConnection.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import AnyUrl, BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr

from .. import connectionBasicType


class AmundsenType(Enum):
    Amundsen = 'Amundsen'


class AmundsenConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[AmundsenType] = Field(
        AmundsenType.Amundsen, description='Service Type'
    )
    username: str = Field(
        ..., description='username to connect to the Amundsen Neo4j Connection.'
    )
    password: CustomSecretStr = Field(
        ..., description='password to connect to the Amundsen Neo4j Connection.'
    )
    hostPort: AnyUrl = Field(
        ...,
        description='Host and port of the Amundsen Neo4j Connection. This expect a URI format like: bolt://localhost:7687.',
        title='Host and Port',
    )
    maxConnectionLifeTime: Optional[int] = Field(
        50, description='Maximum connection lifetime for the Amundsen Neo4j Connection.'
    )
    validateSSL: Optional[bool] = Field(
        False, description='Enable SSL validation for the Amundsen Neo4j Connection.'
    )
    encrypted: Optional[bool] = Field(
        False, description='Enable encryption for the Amundsen Neo4j Connection.'
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = None
