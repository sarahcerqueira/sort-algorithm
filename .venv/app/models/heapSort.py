from app.templates.sortTemplate import *
from heapq import heapify, heappop

class HeapSort(SortTemplate):

    def sort(datatosort:list)->list:
        sortedList = []
        heapify(datatosort)
        size = len(datatosort)
        i = 0

        while i < size:
            sortedList.append(heappop(datatosort))
            i += 1

        return sortedList