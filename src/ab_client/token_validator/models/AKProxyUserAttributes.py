from typing import *

from pydantic import BaseModel, Field


class AKProxyUserAttributes(BaseModel):
    """
    AKProxyUserAttributes model
        Authentik proxy user attributes, typically set via user/group attribute policies.
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
