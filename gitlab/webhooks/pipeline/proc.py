from gitlab.webhooks.pipeline.datamodel import PiplineDataModel
from gitlab.webhooks.processor import DataProcessor


class PipeLineDataProc(DataProcessor):
    data_model = PiplineDataModel
    model: PiplineDataModel

    def __init__(self, data: dict):
        super().__init__(data)

    def __rep(self):
        pass

    def to_message(self) -> str:
        return self.model.user.name
