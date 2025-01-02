from app.templates.partitionTemplate import *

class QuickSort:
    @staticmethod
    def quickSort(datatosort: list, indexStart: int, indexEnd:int, partitionClass:PartitionTemplate) -> list:
        if indexStart < indexEnd:
            s = partitionClass.partition(datatosort, indexStart, indexEnd)
            QuickSort.quickSort(datatosort, indexStart, s - 1, partitionClass)
            QuickSort.quickSort(datatosort, s + 1, indexEnd, partitionClass)