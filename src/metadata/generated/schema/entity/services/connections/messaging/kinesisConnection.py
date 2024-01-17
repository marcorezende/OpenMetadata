# generated by datamodel-codegen:
#   filename:  entity/services/connections/messaging/kinesisConnection.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from .....security.credentials import awsCredentials
from .. import connectionBasicType


class KinesisType(Enum):
    Kinesis = 'Kinesis'


class KinesisConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[KinesisType] = Field(
        KinesisType.Kinesis, description='Service Type', title='Service Type'
    )
    awsConfig: awsCredentials.AWSCredentials = Field(
        ..., title='AWS Credentials Configuration'
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')
