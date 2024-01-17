# generated by datamodel-codegen:
#   filename:  entity/teams/user.json
#   timestamp: 2024-01-10T13:30:42+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, Extra, Field, constr

from ...auth import basicAuth, jwtAuth, ssoAuth
from ...type import basic, entityHistory, entityReference, entityReferenceList, profile


class EntityName(BaseModel):
    __root__: constr(regex=r'^(?u)[\w\-.]+$', min_length=1, max_length=64) = Field(
        ...,
        description='Login name of the user, typically the user ID from an identity provider. Example - uid from LDAP.',
    )


class AuthType(Enum):
    JWT = 'JWT'
    SSO = 'SSO'
    BASIC = 'BASIC'


class AuthenticationMechanism(BaseModel):
    class Config:
        extra = Extra.forbid

    config: Optional[
        Union[
            ssoAuth.SSOAuthMechanism,
            jwtAuth.JWTAuthMechanism,
            basicAuth.BasicAuthMechanism,
        ]
    ] = None
    authType: Optional[AuthType] = None


class User(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(
        ..., description='Unique identifier that identifies a user entity instance.'
    )
    name: EntityName = Field(
        ...,
        description='A unique name of the user, typically the user ID from an identity provider. Example - uid from LDAP.',
    )
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='FullyQualifiedName same as `name`.'
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Used for user biography.'
    )
    displayName: Optional[str] = Field(
        None,
        description="Name used for display purposes. Example 'FirstName LastName'.",
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    email: basic.Email = Field(..., description='Email address of the user.')
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this entity.'
    )
    timezone: Optional[str] = Field(None, description='Timezone of the user.')
    isBot: Optional[bool] = Field(
        None, description='When true indicates a special type of user called Bot.'
    )
    isAdmin: Optional[bool] = Field(
        None,
        description='When true indicates user is an administrator for the system with superuser privileges.',
    )
    authenticationMechanism: Optional[AuthenticationMechanism] = None
    profile: Optional[profile.Profile] = Field(None, description='Profile of the user.')
    teams: Optional[entityReferenceList.EntityReferenceList] = Field(
        None, description='Teams that the user belongs to.'
    )
    defaultPersona: Optional[entityReference.EntityReference] = Field(
        None, description='Default Persona for the user from list of personas.'
    )
    personas: Optional[entityReferenceList.EntityReferenceList] = Field(
        None, description='Personas that the user assigned to.'
    )
    owns: Optional[entityReferenceList.EntityReferenceList] = Field(
        None, description='List of entities owned by the user.'
    )
    follows: Optional[entityReferenceList.EntityReferenceList] = Field(
        None, description='List of entities followed by the user.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )
    roles: Optional[entityReferenceList.EntityReferenceList] = Field(
        None, description='Roles that the user has been assigned.'
    )
    inheritedRoles: Optional[entityReferenceList.EntityReferenceList] = Field(
        None,
        description='Roles that a user is inheriting through membership in teams that have set team default roles.',
    )
    isEmailVerified: Optional[bool] = Field(
        None, description='If the User has verified the mail'
    )
    domain: Optional[entityReference.EntityReference] = Field(
        None,
        description='Domain the User belongs to. This is inherited by the team the user belongs to.',
    )
