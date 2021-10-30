from pydantic import BaseModel


class StaffItemBase(BaseModel):
    name: str


class StaffItem(StaffItemBase):
    id: int
