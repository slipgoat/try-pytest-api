from typing import TypeVar, Type

from pydantic import BaseModel as PydanticBaseModel

T = TypeVar('T', bound=PydanticBaseModel)


class BaseModel(PydanticBaseModel):

    @classmethod
    def from_dict(cls: Type[T], dict_model: dict):
        return cls(**dict_model)
