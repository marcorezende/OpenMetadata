# generated by datamodel-codegen:
#   filename:  entity/applications/jobStatus.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from pydantic import BaseModel, Field

from .configuration import searchIndexingApp


class JobRun(BaseModel):
    pass


class Configuration(BaseModel):
    __root__: searchIndexingApp.SearchIndexingApp = Field(
        ..., description='Configuration Object.'
    )
