from fastapi import APIRouter
from server.routes.v1.animes import router as animes_router

router = APIRouter()

router.include_router(animes_router, prefix="/animes", tags=["Animes"])
