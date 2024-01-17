# generated by datamodel-codegen:
#   filename:  entity/services/pipelineService.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Extra, Field

from ...type import basic, entityHistory, entityReference, entityReferenceList, tagLabel
from .connections import testConnectionResult
from .connections.pipeline import (
    airbyteConnection,
    airflowConnection,
    customPipelineConnection,
    dagsterConnection,
    databricksPipelineConnection,
    domoPipelineConnection,
    fivetranConnection,
    gluePipelineConnection,
    nifiConnection,
    splineConnection,
)


class PipelineServiceType(Enum):
    Airflow = 'Airflow'
    GluePipeline = 'GluePipeline'
    Airbyte = 'Airbyte'
    Fivetran = 'Fivetran'
    Dagster = 'Dagster'
    Nifi = 'Nifi'
    DomoPipeline = 'DomoPipeline'
    CustomPipeline = 'CustomPipeline'
    DatabricksPipeline = 'DatabricksPipeline'
    Spline = 'Spline'


class PipelineConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    config: Optional[
        Union[
            airflowConnection.AirflowConnection,
            gluePipelineConnection.GluePipelineConnection,
            airbyteConnection.AirbyteConnection,
            fivetranConnection.FivetranConnection,
            dagsterConnection.DagsterConnection,
            nifiConnection.NifiConnection,
            domoPipelineConnection.DomoPipelineConnection,
            customPipelineConnection.CustomPipelineConnection,
            databricksPipelineConnection.DatabricksPipelineConnection,
            splineConnection.SplineConnection,
        ]
    ] = None


class PipelineService(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(
        ..., description='Unique identifier of this pipeline service instance.'
    )
    name: basic.EntityName = Field(
        ..., description='Name that identifies this pipeline service.'
    )
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='FullyQualifiedName same as `name`.'
    )
    serviceType: PipelineServiceType = Field(
        ..., description='Type of pipeline service such as Airflow or Prefect...'
    )
    description: Optional[str] = Field(
        None, description='Description of a pipeline service instance.'
    )
    displayName: Optional[str] = Field(
        None,
        description='Display Name that identifies this pipeline service. It could be title or label from the source services.',
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    testConnectionResult: Optional[testConnectionResult.TestConnectionResult] = Field(
        None, description='Last test connection results for this service'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this Pipeline Service.'
    )
    pipelines: Optional[entityReferenceList.EntityReferenceList] = Field(
        None,
        description='References to pipelines deployed for this pipeline service to extract metadata',
    )
    connection: Optional[PipelineConnection] = None
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this pipeline service.'
    )
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this pipeline service.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )
    dataProducts: Optional[entityReferenceList.EntityReferenceList] = Field(
        None, description='List of data products this entity is part of.'
    )
    domain: Optional[entityReference.EntityReference] = Field(
        None, description='Domain the Pipeline service belongs to.'
    )
