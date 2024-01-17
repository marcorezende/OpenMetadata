# generated by datamodel-codegen:
#   filename:  api/data/createSearchIndex.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field, constr

from ...entity.data import searchIndex
from ...type import basic, entityReference, lifeCycle, tagLabel


class CreateSearchIndexRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: basic.EntityName = Field(
        ..., description='Name that identifies this SearchIndex instance uniquely.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this SearchIndex.'
    )
    description: Optional[basic.Markdown] = Field(
        None,
        description='Description of the SearchIndex instance. What it has and how to use it.',
    )
    service: basic.FullyQualifiedEntityName = Field(
        ...,
        description='Fully qualified name of the search service where this searchIndex is hosted in',
    )
    fields: List[searchIndex.SearchIndexField] = Field(
        ..., description='Fields in this SearchIndex.'
    )
    searchIndexSettings: Optional[searchIndex.SearchIndexSettings] = Field(
        None, description='Contains key/value pair of searchIndex settings.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this SearchIndex'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this SearchIndex'
    )
    extension: Optional[basic.EntityExtension] = Field(
        None,
        description='Entity extension data with custom attributes added to the entity.',
    )
    domain: Optional[basic.FullyQualifiedEntityName] = Field(
        None,
        description='Fully qualified name of the domain the SearchIndex belongs to.',
    )
    dataProducts: Optional[List[basic.FullyQualifiedEntityName]] = Field(
        None,
        description='List of fully qualified names of data products this entity is part of.',
    )
    lifeCycle: Optional[lifeCycle.LifeCycle] = Field(
        None, description='Life Cycle of the entity'
    )
    sourceHash: Optional[constr(min_length=1, max_length=32)] = Field(
        None, description='Source hash of the entity'
    )
