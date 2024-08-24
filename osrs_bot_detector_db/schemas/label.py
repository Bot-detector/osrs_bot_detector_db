from pydantic import BaseModel


class LabelBase(BaseModel):
    label: str


class LabelCreate(LabelBase):
    pass


class LabelUpdate(LabelBase):
    id: int


class LabelResponse(LabelBase):
    id: int
