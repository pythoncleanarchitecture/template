from src.providers.sampleProvider import SampleProvider
from src.entities.sample import SampleEntity


class SampleRepository:
    def __init__(self, key: str):
        self.key = key
        self.provider = SampleProvider()

    def getOperation(self, searchKey: str) -> SampleEntity:
        return SampleEntity(key=self.provider.getOperation(searchKey))
