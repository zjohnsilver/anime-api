from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_animes():
    return [
        {
            "title": "FullMetal Alchemist Brotherhood",
            "number_of_episodes": 64,
            "author": {"name": "Hiromu Arakawa"},
            "director": {"name": "Yasuhiro Irie"},
            "start_time": "2009/04/05",
            "end_time": "2010/07/04",
        }
    ]
