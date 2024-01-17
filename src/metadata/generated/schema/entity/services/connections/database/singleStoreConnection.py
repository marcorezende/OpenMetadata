# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/singleStoreConnection.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr

from .. import connectionBasicType


class SingleStoreType(Enum):
    SingleStore = 'SingleStore'


class SingleStoreScheme(Enum):
    mysql_pymysql = 'mysql+pymysql'


class SingleStoreConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[SingleStoreType] = Field(
        SingleStoreType.SingleStore, description='Service Type', title='Service Type'
    )
    scheme: Optional[SingleStoreScheme] = Field(
        SingleStoreScheme.mysql_pymysql,
        description='SQLAlchemy driver scheme options.',
        title='Connection Scheme',
    )
    username: str = Field(
        ...,
        description='Username to connect to SingleStore. This user should have privileges to read all the metadata in MySQL.',
        title='Username',
    )
    password: Optional[CustomSecretStr] = Field(
        None, description='Password to connect to SingleStore.', title='Password'
    )
    hostPort: str = Field(
        ...,
        description='Host and port of the SingleStore service.',
        title='Host and Port',
    )
    databaseName: Optional[str] = Field(
        None,
        description='Optional name to give to the database in OpenMetadata. If left blank, we will use default as the database name.',
        title='Database Name',
    )
    databaseSchema: Optional[str] = Field(
        None,
        description='Database Schema of the data source. This is optional parameter, if you would like to restrict the metadata reading to a single schema. When left blank, OpenMetadata Ingestion attempts to scan all the schemas.',
        title='Database Schema',
    )
    connectionOptions: Optional[connectionBasicType.ConnectionOptions] = Field(
        None, title='Connection Options'
    )
    connectionArguments: Optional[connectionBasicType.ConnectionArguments] = Field(
        None, title='Connection Arguments'
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')
    supportsDBTExtraction: Optional[connectionBasicType.SupportsDBTExtraction] = None
    supportsProfiler: Optional[connectionBasicType.SupportsProfiler] = Field(
        None, title='Supports Profiler'
    )
    supportsQueryComment: Optional[connectionBasicType.SupportsQueryComment] = Field(
        None, title='Supports Query Comment'
    )
    sampleDataStorageConfig: Optional[
        connectionBasicType.SampleDataStorageConfig
    ] = Field(None, title='S3 Config for Sample Data')
