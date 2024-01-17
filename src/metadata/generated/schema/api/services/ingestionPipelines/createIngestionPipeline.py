# generated by datamodel-codegen:
#   filename:  api/services/ingestionPipelines/createIngestionPipeline.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ....entity.services.ingestionPipelines import ingestionPipeline
from ....metadataIngestion import workflow
from ....type import basic, entityReference


class CreateIngestionPipelineRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: basic.EntityName = Field(
        ..., description='Name that identifies this pipeline instance uniquely.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this ingestion pipeline.'
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Description of the pipeline.'
    )
    pipelineType: ingestionPipeline.PipelineType
    sourceConfig: workflow.SourceConfig
    airflowConfig: ingestionPipeline.AirflowConfig
    loggerLevel: Optional[workflow.LogLevels] = Field(
        workflow.LogLevels.INFO, description='Set the logging level for the workflow.'
    )
    service: entityReference.EntityReference = Field(
        ...,
        description='Link to the service for which ingestion pipeline is ingesting the metadata.',
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this Pipeline.'
    )
