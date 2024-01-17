# generated by datamodel-codegen:
#   filename:  system/eventPublisherJob.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Extra, Field

from ..configuration import elasticSearchConfiguration
from ..type import basic


class Status(Enum):
    started = 'started'
    running = 'running'
    completed = 'completed'
    failed = 'failed'
    active = 'active'
    activeError = 'activeError'
    stopped = 'stopped'
    success = 'success'


class FailureDetails(BaseModel):
    class Config:
        extra = Extra.forbid

    context: Optional[str] = Field(None, description='Additional Context for Failure.')
    lastFailedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last non-successful callback time in UNIX UTC epoch time in milliseconds.',
    )
    lastFailedReason: Optional[str] = Field(
        None,
        description='Last non-successful activity response reason received during callback.',
    )


class StepStats(BaseModel):
    totalRecords: Optional[int] = Field(0, description='Count of Total Failed Records')
    successRecords: Optional[int] = Field(
        0, description='Count of Total Successfully Records'
    )
    failedRecords: Optional[int] = Field(0, description='Count of Total Failed Records')


class Stats(BaseModel):
    class Config:
        extra = Extra.forbid

    jobStats: Optional[StepStats] = None
    entityStats: Optional[StepStats] = None


class RunMode(Enum):
    stream = 'stream'
    batch = 'batch'


class PublisherType(Enum):
    elasticSearch = 'elasticSearch'
    kafka = 'kafka'


class EventPublisherResult(BaseModel):
    class Config:
        extra = Extra.forbid

    name: Optional[str] = Field(None, description='Name of the result')
    timestamp: basic.Timestamp
    status: Status = Field(..., description='This schema publisher run job status.')
    failure: Optional[Dict[str, Any]] = Field(
        None, description='List of Failures in the Job'
    )
    stats: Optional[Stats] = None
    entities: Optional[List[str]] = Field(
        None, description='List of Entities to Reindex', unique_items=True
    )
    recreateIndex: Optional[bool] = Field(
        None, description='This schema publisher run modes.'
    )
    batchSize: Optional[int] = Field(
        None, description='Maximum number of events sent in a batch (Default 10).'
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
