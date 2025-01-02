from abc import ABC

class PartitionTemplate(ABC):
    @staticmethod
    def partition(dataList: list, indexStart: int, indexEnd: int) -> int:
        pass