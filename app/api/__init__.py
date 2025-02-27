from fastapi import APIRouter

from core.config import settings
from .notes import router as note_router
from .auth import router as auth_router

router = APIRouter(
    prefix=settings.api.prefix,
)
router.include_router(
    note_router
)
router.include_router(
    auth_router
)
