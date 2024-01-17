# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/redshiftConnection.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr

from .....security.ssl import verifySSLConfig
from .. import connectionBasicType


class SslMode(Enum):
    disable = 'disable'
    allow = 'allow'
    prefer = 'prefer'
    require = 'require'
    verify_ca = 'verify-ca'
    verify_full = 'verify-full'


class RedshiftType(Enum):
    Redshift = 'Redshift'


class RedshiftScheme(Enum):
    redshift_psycopg2 = 'redshift+psycopg2'


class RedshiftConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[RedshiftType] = Field(
        RedshiftType.Redshift, description='Service Type', title='Service Type'
    )
    scheme: Optional[RedshiftScheme] = Field(
        RedshiftScheme.redshift_psycopg2,
        description='SQLAlchemy driver scheme options.',
        title='Connection Scheme',
    )
    username: str = Field(
        ...,
        description='Username to connect to Redshift. This user should have privileges to read all the metadata in Redshift.',
        title='Username',
    )
    password: Optional[CustomSecretStr] = Field(
        None, description='Password to connect to Redshift.', title='Password'
    )
    hostPort: str = Field(
        ..., description='Host and port of the Redshift service.', title='Host and Port'
    )
    database: str = Field(
        ...,
        description='Initial Redshift database to connect to. If you want to ingest all databases, set ingestAllDatabases to true.',
        title='Database',
    )
    ingestAllDatabases: Optional[bool] = Field(
        False,
        description='Ingest data from all databases in Redshift. You can use databaseFilterPattern on top of this.',
        title='Ingest All Databases',
    )
    sslMode: Optional[SslMode] = Field(
        SslMode.disable,
        description='SSL Mode to connect to redshift database.',
        title='SSL Mode',
    )
    sslConfig: Optional[verifySSLConfig.SslConfig] = None
    connectionOptions: Optional[connectionBasicType.ConnectionOptions] = Field(
        None, title='Connection Options'
    )
    connectionArguments: Optional[connectionBasicType.ConnectionArguments] = Field(
        None, title='Connection Arguments'
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')
    supportsUsageExtraction: Optional[
        connectionBasicType.SupportsUsageExtraction
    ] = None
    supportsLineageExtraction: Optional[
        connectionBasicType.SupportsLineageExtraction
    ] = None
    supportsDBTExtraction: Optional[connectionBasicType.SupportsDBTExtraction] = None
    supportsProfiler: Optional[connectionBasicType.SupportsProfiler] = Field(
        None, title='Supports Profiler'
    )
    supportsDatabase: Optional[connectionBasicType.SupportsDatabase] = Field(
        None, title='Supports Database'
    )
    supportsQueryComment: Optional[connectionBasicType.SupportsQueryComment] = Field(
        None, title='Supports Query Comment'
    )
    sampleDataStorageConfig: Optional[
        connectionBasicType.SampleDataStorageConfig
    ] = Field(None, title='S3 Config for Sample Data')
