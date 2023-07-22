from dataclasses import dataclass
from src.usecases import IBaseRequestDTO, IBaseResponseDTO
from src.entities.sample import SampleEntity


@dataclass
class SampleRequestDTO(IBaseRequestDTO):
    param: str


@dataclass
class SampleResponseDTO(IBaseResponseDTO):
    data: SampleEntity
