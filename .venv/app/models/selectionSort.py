from app.templates.sortTemplate import *

class SelectionSort(SortTemplate):

    def sort(datatosort:list)->list:
        size = len(datatosort)
        for i in range(0, size - 1):
            min = i
            for j in range(i + 1, size):
                if datatosort[j] < datatosort[min]:
                    min = j
            datatosort[i], datatosort[min] = datatosort[min], datatosort[i]

        return datatosort
