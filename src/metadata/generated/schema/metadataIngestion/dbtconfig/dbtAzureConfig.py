# generated by datamodel-codegen:
#   filename:  metadataIngestion/dbtconfig/dbtAzureConfig.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ...security.credentials import azureCredentials


class DbtPrefixConfig(BaseModel):
    class Config:
        extra = Extra.forbid

    dbtBucketName: Optional[str] = Field(
        None,
        description='Name of the bucket where the dbt files are stored',
        title='DBT Bucket Name',
    )
    dbtObjectPrefix: Optional[str] = Field(
        None,
        description='Path of the folder where the dbt files are stored',
        title='DBT Object Prefix',
    )


class DbtAzureConfig(BaseModel):
    dbtSecurityConfig: Optional[azureCredentials.AzureCredentials] = Field(
        None, title='DBT Azure Security Config'
    )
    dbtPrefixConfig: Optional[DbtPrefixConfig] = Field(
        None,
        description='Details of the bucket where the dbt files are stored',
        title='DBT Prefix Config',
    )
