from abc import ABC, abstractmethod

class SearchI(ABC):

    @abstractmethod
    def find_all_hrefs(self) -> None:
        pass
    @abstractmethod
    def get_all_href(self) -> list:
        pass