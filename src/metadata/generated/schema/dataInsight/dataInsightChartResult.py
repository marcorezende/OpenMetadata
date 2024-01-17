# generated by datamodel-codegen:
#   filename:  dataInsight/dataInsightChartResult.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Extra, Field

from .type import (
    aggregatedUnusedAssetsCount,
    aggregatedUnusedAssetsSize,
    aggregatedUsedVsUnusedAssetsCount,
    aggregatedUsedVsUnusedAssetsSize,
    dailyActiveUsers,
    mostActiveUsers,
    mostViewedEntities,
    pageViewsByEntities,
    percentageOfEntitiesWithDescriptionByType,
    percentageOfEntitiesWithOwnerByType,
    percentageOfServicesWithDescription,
    percentageOfServicesWithOwner,
    totalEntitiesByTier,
    totalEntitiesByType,
    unusedAssets,
)


class DataInsightChartType(Enum):
    TotalEntitiesByType = 'TotalEntitiesByType'
    TotalEntitiesByTier = 'TotalEntitiesByTier'
    PercentageOfEntitiesWithDescriptionByType = (
        'PercentageOfEntitiesWithDescriptionByType'
    )
    PercentageOfEntitiesWithOwnerByType = 'PercentageOfEntitiesWithOwnerByType'
    DailyActiveUsers = 'DailyActiveUsers'
    MostActiveUsers = 'MostActiveUsers'
    MostViewedEntities = 'MostViewedEntities'
    PageViewsByEntities = 'PageViewsByEntities'
    PercentageOfServicesWithDescription = 'PercentageOfServicesWithDescription'
    PercentageOfServicesWithOwner = 'PercentageOfServicesWithOwner'
    UnusedAssets = 'UnusedAssets'
    AggregatedUnusedAssetsSize = 'AggregatedUnusedAssetsSize'
    AggregatedUnusedAssetsCount = 'AggregatedUnusedAssetsCount'
    AggregatedUsedVsUnusedAssetsSize = 'AggregatedUsedVsUnusedAssetsSize'
    AggregatedUsedVsUnusedAssetsCount = 'AggregatedUsedVsUnusedAssetsCount'


class DataInsightChartResult(BaseModel):
    class Config:
        extra = Extra.forbid

    chartType: DataInsightChartType = Field(
        ...,
        description='Chart Type that will consume the data. Must match name of dataInsightChart.',
    )
    total: Optional[int] = Field(
        None, description='Total number of hits returned by the aggregation.'
    )
    data: Optional[
        List[
            Union[
                percentageOfEntitiesWithDescriptionByType.PercentageOfEntitiesWithDescriptionByType,
                percentageOfEntitiesWithOwnerByType.PercentageOfEntitiesWithOwnerByType,
                totalEntitiesByTier.TotalEntitiesByTier,
                totalEntitiesByType.TotalEntitiesByType,
                dailyActiveUsers.DailyActiveUsers,
                pageViewsByEntities.PageViewsByEntities,
                mostActiveUsers.MostActiveUsers,
                mostViewedEntities.MostViewedEntities,
                percentageOfServicesWithDescription.PercentageOfServicesWithDescription,
                percentageOfServicesWithOwner.PercentageOfServicesWithOwner,
                unusedAssets.UnusedAssets,
                aggregatedUnusedAssetsSize.AggregatedUnusedAssetsSize,
                aggregatedUnusedAssetsCount.AggregatedUnusedAssetsCount,
                aggregatedUsedVsUnusedAssetsSize.AggregatedUsedVsUnusedAssetsSize,
                aggregatedUsedVsUnusedAssetsCount.AggregatedUsedVsUnusedAssetsCount,
            ]
        ]
    ] = Field(None, description='Array of consumable data.')
