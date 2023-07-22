from dataclasses import dataclass
from src.usecases import IBaseRequestDTO, IBaseResponseDTO


@dataclass
class SampleRequestDTO(IBaseRequestDTO):
    param: str


@dataclass
class SampleResponseDTO(IBaseResponseDTO):
    status: bool
