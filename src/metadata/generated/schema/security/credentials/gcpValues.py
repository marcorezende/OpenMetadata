# generated by datamodel-codegen:
#   filename:  security/credentials/gcpValues.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr


class SingleProjectId(BaseModel):
    __root__: str = Field(..., title='Single Project ID')


class MultipleProjectId(BaseModel):
    __root__: List[str] = Field(..., title='Multiple Project ID')


class GcpCredentialsValues(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[str] = Field(
        None,
        description='Google Cloud Platform account type.',
        title='Credentials Type',
    )
    projectId: Optional[Union[SingleProjectId, MultipleProjectId]] = Field(
        None, description='Project ID', title='Project ID'
    )
    privateKeyId: Optional[str] = Field(
        None, description='Google Cloud private key id.', title='Private Key ID'
    )
    privateKey: Optional[CustomSecretStr] = Field(
        None, description='Google Cloud private key.', title='Private Key'
    )
    clientEmail: Optional[str] = Field(
        None, description='Google Cloud email.', title='Client Email'
    )
    clientId: Optional[str] = Field(
        None, description='Google Cloud Client ID.', title='Client ID'
    )
    authUri: Optional[AnyUrl] = Field(
        'https://accounts.google.com/o/oauth2/auth',
        description='Google Cloud auth uri.',
        title='Authentication URI',
    )
    tokenUri: Optional[AnyUrl] = Field(
        'https://oauth2.googleapis.com/token',
        description='Google Cloud token uri.',
        title='Token URI',
    )
    authProviderX509CertUrl: Optional[AnyUrl] = Field(
        'https://www.googleapis.com/oauth2/v1/certs',
        description='Google Cloud auth provider certificate.',
        title='Authentication Provider x509 Certificate URL',
    )
    clientX509CertUrl: Optional[AnyUrl] = Field(
        None,
        description='Google Cloud client certificate uri.',
        title='Client x509 Certificate URL',
    )
