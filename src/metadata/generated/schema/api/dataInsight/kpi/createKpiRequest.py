# generated by datamodel-codegen:
#   filename:  api/dataInsight/kpi/createKpiRequest.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ....dataInsight.kpi import basic as basic_1
from ....type import basic, entityReference


class CreateKpiRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: basic.EntityName = Field(..., description='Name that identifies this Kpi.')
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this Kpi.'
    )
    description: basic.Markdown = Field(..., description='Description of the Kpi.')
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this Kpi'
    )
    dataInsightChart: basic.FullyQualifiedEntityName = Field(
        ..., description='Fully qualified name of the Chart this kpi refers to'
    )
    startDate: basic.Timestamp = Field(..., description='Start Date for the KPIs')
    endDate: basic.Timestamp = Field(..., description='End Date for the KPIs')
    targetDefinition: List[basic_1.KpiTarget] = Field(
        ..., description='Metrics from the chart and the target to achieve the result.'
    )
    metricType: basic_1.KpiTargetType
