from pydantic import BaseModel, conint
from server.schemas.staff import StaffItem


class AnimeItemBase(BaseModel):
    title: str
    number_of_episodes: conint(gt=0)
    author: StaffItem
    director: StaffItem
    start_date: str
    end_date: str


class AnimeItem(AnimeItemBase):
    id: int
