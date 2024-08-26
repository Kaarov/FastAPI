from fastapi_users.authentication import BearerTransport

from core.config import settings

bearer_transport = BearerTransport(
    # TODO: update url
    tokenUrl=settings.api.bearer_token_url,
)
