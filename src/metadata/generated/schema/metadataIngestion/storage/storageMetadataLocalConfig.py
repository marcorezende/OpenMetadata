# generated by datamodel-codegen:
#   filename:  metadataIngestion/storage/storageMetadataLocalConfig.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from pydantic import BaseModel, Extra, Field


class StorageMetadataLocalConfig(BaseModel):
    class Config:
        extra = Extra.forbid

    manifestFilePath: str = Field(
        ...,
        description='Storage Metadata manifest file path to extract locations to ingest from.',
        title='Storage Metadata Manifest File Path',
    )
