from abc import ABC,abstractmethod

class DataDownloaderI(ABC):

    @abstractmethod
    def get(self) -> str:
        pass