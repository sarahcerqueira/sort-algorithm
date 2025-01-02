from app.templates.sortTemplate import *

class InsertionSort(SortTemplate):

    def sort(datatosort:list)->list:
        size = len(datatosort)
        for i in range(1, size):
            aux = datatosort[i]
            j = i - 1
            while j >= 0 and aux < datatosort[j]:
                datatosort[j + 1] = datatosort[j]
                j -= 1
            datatosort[j + 1] = aux
        return datatosort