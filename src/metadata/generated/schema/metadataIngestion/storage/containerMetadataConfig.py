# generated by datamodel-codegen:
#   filename:  metadataIngestion/storage/containerMetadataConfig.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ...entity.data import table


class MetadataEntry(BaseModel):
    dataPath: str = Field(
        ...,
        description='The path where the data resides in the container, excluding the bucket name',
        title='Data path',
    )
    structureFormat: Optional[str] = Field(
        None,
        description="What's the schema format for the container, eg. avro, parquet, csv.",
        title='Schema format',
    )
    separator: Optional[str] = Field(
        None,
        description='For delimited files such as CSV, what is the separator being used?',
        title='Separator',
    )
    isPartitioned: Optional[bool] = Field(
        False,
        description="Flag indicating whether the container's data is partitioned",
        title='Is Partitioned',
    )
    partitionColumns: Optional[List[table.Column]] = Field(
        None,
        description="What are the partition columns in case the container's data is partitioned",
        title='Partition Columns',
    )


class StorageContainerConfig(BaseModel):
    class Config:
        extra = Extra.forbid

    entries: List[MetadataEntry] = Field(
        ...,
        description='List of metadata entries for the bucket containing information about where data resides and its structure',
    )
