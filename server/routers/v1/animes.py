from fastapi import APIRouter
from server.schemas.animes import AnimeItem
from typing import List

router = APIRouter()


@router.get("/", response_model=List[AnimeItem])
async def get_animes():
    return [
        {
            "id": 1,
            "title": "FullMetal Alchemist Brotherhood",
            "number_of_episodes": 64,
            "author": {"id": 1, "name": "Hiromu Arakawa"},
            "director": {"id": 1, "name": "Yasuhiro Irie"},
            "start_date": "2009/04/05",
            "end_date": "2010/07/04",
        }
    ]
