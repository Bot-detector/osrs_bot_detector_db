from pydantic import BaseModel


class LabelBase(BaseModel):
    label: str


class LabelCreate(LabelBase):
    pass


class LabelResponse(LabelBase):
    id: int
