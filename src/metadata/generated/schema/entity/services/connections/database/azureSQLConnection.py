# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/azureSQLConnection.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr

from .. import connectionBasicType


class AzureSQLType(Enum):
    AzureSQL = 'AzureSQL'


class AzureSQLScheme(Enum):
    mssql_pyodbc = 'mssql+pyodbc'


class AzureSQLConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[AzureSQLType] = Field(
        AzureSQLType.AzureSQL, description='Service Type', title='Service Type'
    )
    scheme: Optional[AzureSQLScheme] = Field(
        AzureSQLScheme.mssql_pyodbc,
        description='SQLAlchemy driver scheme options.',
        title='Connection Scheme',
    )
    username: str = Field(
        ...,
        description='Username to connect to AzureSQL. This user should have privileges to read the metadata.',
        title='Username',
    )
    password: Optional[CustomSecretStr] = Field(
        None, description='Password to connect to AzureSQL.', title='Password'
    )
    hostPort: str = Field(
        ..., description='Host and port of the AzureSQL service.', title='Host and Port'
    )
    database: str = Field(
        ...,
        description='Database of the data source. This is optional parameter, if you would like to restrict the metadata reading to a single database. When left blank, OpenMetadata Ingestion attempts to scan all the databases.',
        title='Database',
    )
    driver: Optional[str] = Field(
        'ODBC Driver 18 for SQL Server',
        description='SQLAlchemy driver for AzureSQL.',
        title='Driver',
    )
    ingestAllDatabases: Optional[bool] = Field(
        False,
        description='Ingest data from all databases in Azuresql. You can use databaseFilterPattern on top of this.',
        title='Ingest All Databases',
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
    supportsUsageExtraction: Optional[
        connectionBasicType.SupportsUsageExtraction
    ] = Field(None, title='Supports Usage Extraction')
    supportsLineageExtraction: Optional[
        connectionBasicType.SupportsLineageExtraction
    ] = Field(None, title='Supports Lineage Extraction')
    supportsDBTExtraction: Optional[connectionBasicType.SupportsDBTExtraction] = None
    supportsProfiler: Optional[connectionBasicType.SupportsProfiler] = Field(
        None, title='Supports Profiler'
    )
    supportsDatabase: Optional[connectionBasicType.SupportsDatabase] = Field(
        None, title='Supports Database'
    )
    sampleDataStorageConfig: Optional[
        connectionBasicType.SampleDataStorageConfig
    ] = Field(None, title='S3 Config for Sample Data')
