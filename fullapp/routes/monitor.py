import logging
import re

from fastapi import Depends, Response
from fastapi import Request

from fullapp.models.monitor import Health, HealthStatus

### Monitoring tools


logger = logging.getLogger(__name__)

SLUG_RE = re.compile(r"\W")


def get_version(request: Request):
    return request.app.version


def get_slug(request: Request):
    return SLUG_RE.sub("-", request.app.title.lower())


def health_check(slug: str = Depends(get_slug), version: str = Depends(get_version)):
    health = Health(
        status=HealthStatus.status_pass,
        version=version.split(".", 1)[0],
        release_id=version,
        description=slug,
    )
    return Response(
        content=health.json(by_alias=True, skip_defaults=True),
        media_type="application/health+json",
    )
