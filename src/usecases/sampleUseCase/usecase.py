from src.usecases import IBaseUseCase
from src.usecases.sampleUseCase.dto import SampleRequestDTO, SampleResponseDTO


class SampleUseCase(IBaseUseCase):
    def __init__(self, req: SampleRequestDTO):
        self.req = req

    def execute(self) -> SampleResponseDTO:
        print(self.req.param)
        return SampleResponseDTO(status=True)


if __name__ == "__main__":
    uc = SampleUseCase(req=SampleRequestDTO(param="Test this"))
    uc.execute()
