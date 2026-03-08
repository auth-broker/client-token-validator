from typing import *

from pydantic import BaseModel, Field

from .AKProxyUserAttributes import AKProxyUserAttributes


class AKProxy(BaseModel):
    """
    AKProxy model
        Authentik-specific proxy metadata injected into tokens by the ak_proxy scope.
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    user_attributes: Optional[AKProxyUserAttributes] = Field(validation_alias="user_attributes", default=None)

    is_superuser: Optional[bool] = Field(validation_alias="is_superuser", default=False)
