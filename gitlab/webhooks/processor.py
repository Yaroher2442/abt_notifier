from typing import Type, Dict

from pydantic import BaseModel


class DataProcessor:
    data_model: Type[BaseModel]
    model: BaseModel

    def __init__(self, data: Dict):
        self.model = self.data_model(**data)

    def __rep(self):
        pass

    def to_message(self) -> str:
        pass
