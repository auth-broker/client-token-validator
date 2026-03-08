from typing import *

from pydantic import BaseModel, Field

from .AKProxy import AKProxy


class ValidatedOIDCClaims(BaseModel):
    """
    ValidatedOIDCClaims model
        Validated claims from an OIDC JWT issued by Authentik.

    Covers standard OIDC claims (RFC 7519 / OIDC Core 1.0) as well as
    Authentik-specific extensions such as `ak_proxy`, `entitlements`, and `roles`.
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    iss: str = Field(validation_alias="iss")

    sub: str = Field(validation_alias="sub")

    aud: Union[str, List[str]] = Field(validation_alias="aud")

    exp: int = Field(validation_alias="exp")

    iat: int = Field(validation_alias="iat")

    auth_time: int = Field(validation_alias="auth_time")

    acr: str = Field(validation_alias="acr")

    name: Optional[Union[str, None]] = Field(validation_alias="name", default=None)

    given_name: Optional[Union[str, None]] = Field(validation_alias="given_name", default=None)

    preferred_username: Optional[Union[str, None]] = Field(validation_alias="preferred_username", default=None)

    nickname: Optional[Union[str, None]] = Field(validation_alias="nickname", default=None)

    email: Optional[Union[str, None]] = Field(validation_alias="email", default=None)

    email_verified: Optional[Union[bool, None]] = Field(validation_alias="email_verified", default=None)

    entitlements: Optional[List[str]] = Field(validation_alias="entitlements", default=None)

    roles: Optional[List[str]] = Field(validation_alias="roles", default=None)

    groups: Optional[List[str]] = Field(validation_alias="groups", default=None)

    ak_proxy: Optional[AKProxy] = Field(validation_alias="ak_proxy", default=None)
