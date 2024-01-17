# generated by datamodel-codegen:
#   filename:  api/data/createDatabaseSchema.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field, constr

from ...entity.data import databaseSchema
from ...type import basic, entityReference, lifeCycle, tagLabel


class CreateDatabaseSchemaRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: databaseSchema.EntityName = Field(
        ..., description='Name that identifies this database schema instance uniquely.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this database schema.'
    )
    description: Optional[basic.Markdown] = Field(
        None,
        description='Description of the schema instance. What it has and how to use it.',
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this schema'
    )
    database: basic.FullyQualifiedEntityName = Field(
        ...,
        description='Link to the database fully qualified name where this schema is hosted in',
    )
    dataProducts: Optional[List[basic.FullyQualifiedEntityName]] = Field(
        None,
        description='List of fully qualified names of data products this entity is part of.',
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this table'
    )
    retentionPeriod: Optional[basic.Duration] = Field(
        None,
        description='Retention period of the data in the database. Period is expressed as duration in ISO 8601 format in UTC. Example - `P23DT23H`.',
    )
    extension: Optional[basic.EntityExtension] = Field(
        None,
        description='Entity extension data with custom attributes added to the entity.',
    )
    sourceUrl: Optional[basic.SourceUrl] = Field(
        None, description='Source URL of database schema.'
    )
    domain: Optional[str] = Field(
        None,
        description='Fully qualified name of the domain the Database Schema belongs to.',
    )
    lifeCycle: Optional[lifeCycle.LifeCycle] = Field(
        None, description='Life Cycle of the entity'
    )
    sourceHash: Optional[constr(min_length=1, max_length=32)] = Field(
        None, description='Source hash of the entity'
    )
