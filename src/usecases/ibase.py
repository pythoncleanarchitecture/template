from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class IBaseRequestDTO:
    ...


@dataclass
class IBaseResponseDTO:
    ...


class IBaseUseCase(ABC):

    @abstractmethod
    def __init__(self, req: IBaseRequestDTO) -> None:
        self.req = req

    @abstractmethod
    def execute(self) -> IBaseResponseDTO:
        ...
