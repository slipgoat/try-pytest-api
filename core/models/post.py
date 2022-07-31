from core.models.base_model import BaseModel


class Post(BaseModel):
    id: int
    title: str
    body: str
    userId: int
