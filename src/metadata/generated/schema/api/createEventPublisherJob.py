# generated by datamodel-codegen:
#   filename:  api/createEventPublisherJob.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ..configuration import elasticSearchConfiguration
from ..system import eventPublisherJob


class CreateEventPublisherJob(BaseModel):
    class Config:
        extra = Extra.forbid

    name: Optional[str] = Field(None, description='Name of the result')
    publisherType: Optional[eventPublisherJob.PublisherType] = None
    runMode: Optional[eventPublisherJob.RunMode] = None
    entities: Optional[List[str]] = Field(
        ['all'], description='List of Entities to Reindex', unique_items=True
    )
    recreateIndex: Optional[bool] = Field(
        False, description='This schema publisher run modes.'
    )
    batchSize: Optional[int] = Field(
        100, description='Maximum number of events sent in a batch (Default 10).'
    )
    searchIndexMappingLanguage: Optional[
        elasticSearchConfiguration.SearchIndexMappingLanguage
    ] = Field(
        elasticSearchConfiguration.SearchIndexMappingLanguage.EN,
        description='Recreate Indexes with updated Language',
    )
    afterCursor: Optional[str] = Field(
        None,
        description='Provide After in case of failure to start reindexing after the issue is solved',
    )
