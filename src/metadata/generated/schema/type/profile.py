# generated by datamodel-codegen:
#   filename:  type/profile.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from typing import Optional

from pydantic import AnyUrl, BaseModel, Extra

from ..entity.events import webhook


class ImageList(BaseModel):
    class Config:
        extra = Extra.forbid

    image: Optional[AnyUrl] = None
    image24: Optional[AnyUrl] = None
    image32: Optional[AnyUrl] = None
    image48: Optional[AnyUrl] = None
    image72: Optional[AnyUrl] = None
    image192: Optional[AnyUrl] = None
    image512: Optional[AnyUrl] = None


class MessagingProvider(BaseModel):
    class Config:
        extra = Extra.forbid

    slack: Optional[webhook.Webhook] = None
    msTeams: Optional[webhook.Webhook] = None
    gChat: Optional[webhook.Webhook] = None
    generic: Optional[webhook.Webhook] = None


class Profile(BaseModel):
    class Config:
        extra = Extra.forbid

    images: Optional[ImageList] = None
    subscription: Optional[MessagingProvider] = None
