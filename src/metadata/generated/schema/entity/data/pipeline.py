# generated by datamodel-codegen:
#   filename:  entity/data/pipeline.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import AnyUrl, BaseModel, Extra, Field, constr

from ...type import (
    basic,
    entityHistory,
    entityReference,
    entityReferenceList,
    lifeCycle,
    tagLabel,
    votes,
)
from ..services import pipelineService


class EntityName(BaseModel):
    __root__: constr(regex=r'^((?!::).)*$', min_length=1, max_length=128) = Field(
        ...,
        description='Name of a pipeline. Expected to be unique within a pipeline service.',
    )


class StatusType(Enum):
    Successful = 'Successful'
    Failed = 'Failed'
    Pending = 'Pending'


class TaskStatus(BaseModel):
    class Config:
        extra = Extra.forbid

    name: str = Field(..., description='Name of the Task.')
    executionStatus: StatusType = Field(
        ..., description='Status at a specific execution date.'
    )
    startTime: Optional[basic.Timestamp] = Field(None, description='Task start time')
    endTime: Optional[basic.Timestamp] = Field(None, description='Task end time')
    logLink: Optional[AnyUrl] = Field(None, description='Task end time')


class PipelineStatus(BaseModel):
    class Config:
        extra = Extra.forbid

    timestamp: basic.Timestamp = Field(
        ..., description='Timestamp where the job was executed.'
    )
    executionStatus: StatusType = Field(
        ..., description='Status at a specific execution date.'
    )
    taskStatus: Optional[List[TaskStatus]] = Field(
        None, description='Series of task executions and its status.'
    )


class Task(BaseModel):
    class Config:
        extra = Extra.forbid

    name: str = Field(
        ..., description='Name that identifies this task instance uniquely.'
    )
    displayName: Optional[str] = Field(
        None,
        description='Display Name that identifies this Task. It could be title or label from the pipeline services.',
    )
    fullyQualifiedName: Optional[str] = Field(
        None,
        description="A unique name that identifies a pipeline in the format 'ServiceName.PipelineName.TaskName'.",
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Description of this Task.'
    )
    sourceUrl: Optional[basic.SourceUrl] = Field(
        None,
        description='Task URL to visit/manage. This URL points to respective pipeline service UI.',
    )
    downstreamTasks: Optional[List[str]] = Field(
        None, description='All the tasks that are downstream of this task.'
    )
    taskType: Optional[str] = Field(
        None, description='Type of the Task. Usually refers to the class it implements.'
    )
    taskSQL: Optional[basic.SqlQuery] = Field(
        None, description='SQL used in the task. Can be used to determine the lineage.'
    )
    startDate: Optional[str] = Field(None, description='start date for the task.')
    endDate: Optional[str] = Field(None, description='end date for the task.')
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this task.'
    )


class Pipeline(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(
        ..., description='Unique identifier that identifies a pipeline instance.'
    )
    name: EntityName = Field(
        ..., description='Name that identifies this pipeline instance uniquely.'
    )
    displayName: Optional[str] = Field(
        None,
        description='Display Name that identifies this Pipeline. It could be title or label from the source services.',
    )
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None,
        description="A unique name that identifies a pipeline in the format 'ServiceName.PipelineName'.",
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Description of this Pipeline.'
    )
    dataProducts: Optional[entityReferenceList.EntityReferenceList] = Field(
        None, description='List of data products this entity is part of.'
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    sourceUrl: Optional[basic.SourceUrl] = Field(
        None,
        description='Pipeline  URL to visit/manage. This URL points to respective pipeline service UI.',
    )
    concurrency: Optional[int] = Field(None, description='Concurrency of the Pipeline.')
    pipelineLocation: Optional[str] = Field(None, description='Pipeline Code Location.')
    startDate: Optional[basic.DateTime] = Field(
        None, description='Start date of the workflow.'
    )
    tasks: Optional[List[Task]] = Field(
        None, description='All the tasks that are part of pipeline.'
    )
    pipelineStatus: Optional[PipelineStatus] = Field(
        None, description='Latest Pipeline Status.'
    )
    followers: Optional[entityReferenceList.EntityReferenceList] = Field(
        None, description='Followers of this Pipeline.'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this Pipeline.'
    )
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this entity.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this pipeline.'
    )
    service: entityReference.EntityReference = Field(
        ..., description='Link to service where this pipeline is hosted in.'
    )
    serviceType: Optional[pipelineService.PipelineServiceType] = Field(
        None, description='Service type where this pipeline is hosted in.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )
    extension: Optional[basic.EntityExtension] = Field(
        None,
        description='Entity extension data with custom attributes added to the entity.',
    )
    scheduleInterval: Optional[str] = Field(
        None, description='Scheduler Interval for the pipeline in cron format.'
    )
    domain: Optional[entityReference.EntityReference] = Field(
        None,
        description='Domain the Pipeline belongs to. When not set, the pipeline inherits the domain from the Pipeline service it belongs to.',
    )
    votes: Optional[votes.Votes] = None
    lifeCycle: Optional[lifeCycle.LifeCycle] = Field(
        None, description='Life Cycle properties of the entity'
    )
    sourceHash: Optional[constr(min_length=1, max_length=32)] = Field(
        None, description='Source hash of the entity'
    )
