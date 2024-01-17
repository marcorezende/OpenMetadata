# generated by datamodel-codegen:
#   filename:  entity/services/messagingService.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Extra, Field

from ...type import basic, entityHistory, entityReference, entityReferenceList, tagLabel
from .connections import testConnectionResult
from .connections.messaging import (
    customMessagingConnection,
    kafkaConnection,
    kinesisConnection,
    redpandaConnection,
)


class MessagingServiceType(Enum):
    Kafka = 'Kafka'
    Redpanda = 'Redpanda'
    Kinesis = 'Kinesis'
    CustomMessaging = 'CustomMessaging'


class Brokers(BaseModel):
    __root__: List[str] = Field(
        ...,
        description='Multiple bootstrap addresses for Kafka. Single proxy address for Pulsar.',
    )


class MessagingConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    config: Optional[
        Union[
            kafkaConnection.KafkaConnection,
            redpandaConnection.RedpandaConnection,
            kinesisConnection.KinesisConnection,
            customMessagingConnection.CustomMessagingConnection,
        ]
    ] = None


class MessagingService(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(
        ..., description='Unique identifier of this messaging service instance.'
    )
    name: basic.EntityName = Field(
        ..., description='Name that identifies this messaging service.'
    )
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='FullyQualifiedName same as `name`.'
    )
    serviceType: MessagingServiceType = Field(
        ..., description='Type of messaging service such as Kafka or Pulsar...'
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Description of a messaging service instance.'
    )
    displayName: Optional[str] = Field(
        None,
        description='Display Name that identifies this messaging service. It could be title or label from the source services.',
    )
    connection: Optional[MessagingConnection] = None
    pipelines: Optional[entityReferenceList.EntityReferenceList] = Field(
        None,
        description='References to pipelines deployed for this messaging service to extract topic configs and schemas.',
    )
    testConnectionResult: Optional[testConnectionResult.TestConnectionResult] = Field(
        None, description='Last test connection results for this service'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this Message Service.'
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this messaging service.'
    )
    href: Optional[basic.Href] = Field(
        None,
        description='Link to the resource corresponding to this messaging service.',
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
        None, description='Domain the Messaging service belongs to.'
    )
