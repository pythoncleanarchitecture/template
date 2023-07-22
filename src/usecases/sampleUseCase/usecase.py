from src.usecases import IBaseUseCase
from src.usecases.sampleUseCase.dto import SampleRequestDTO, SampleResponseDTO
from src.repositories.sampleRepository import SampleRepository


class SampleUseCase(IBaseUseCase):
    def __init__(self, req: SampleRequestDTO):
        self.req = req
        self.repo = SampleRepository(self.req.param)

    def execute(self) -> SampleResponseDTO:
        res = self.repo.getOperation(self.req.param)
        return SampleResponseDTO(data=res)


if __name__ == "__main__":
    uc = SampleUseCase(req=SampleRequestDTO(param="Test this"))
    res = uc.execute()
    print(res.data.key)
