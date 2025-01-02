from app.templates.sortTemplate import *

class HeapSortNotInPlace(SortTemplate):

    def sort(datatosort:list)->list:
        HeapSortNotInPlace.__buildMaxHeap(datatosort, len(datatosort))
        endIndex = len(datatosort) - 1

        while endIndex > 0:
            datatosort[0], datatosort[endIndex] = datatosort[endIndex], datatosort[0]
            HeapSortNotInPlace.__maxHeapfy(datatosort, 0, endIndex)
            endIndex -= 1

        return datatosort

    @staticmethod
    def __buildMaxHeap(datatosort:list, endIndex:int)->None:
        middle = (endIndex - 1) // 2

        while middle >= 0:
            HeapSortNotInPlace.__maxHeapfy(datatosort, middle, endIndex)
            middle -= 1

    @staticmethod
    def __maxHeapfy(datatosort:list, middle:int, endIndex:int) ->None:
        max = HeapSortNotInPlace.__max(datatosort, middle * 2 + 1, middle * 2 + 2, endIndex)

        while max < endIndex and datatosort[middle] < datatosort[max]:
            datatosort[middle], datatosort[max] = datatosort[max], datatosort[middle]
            middle = max
            max = HeapSortNotInPlace.__max(datatosort, middle * 2 + 1, middle * 2 + 2, endIndex)

    @staticmethod
    def __max(datatosort:list, left:int, right:int, endIndex:int)->int:
        if right < endIndex and left < endIndex:
            if datatosort[right] > datatosort[left]:
                return right
            else:
                return left

        elif right < endIndex:
            return right
        elif left < endIndex:
            return left

        return endIndex