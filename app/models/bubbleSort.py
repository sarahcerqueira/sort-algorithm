from app.templates.sortTemplate import *

class BubbleSort(SortTemplate):

    def sort(datatosort:list)->list:
        i = len(datatosort) - 1
        while i > 0:
            for j in range(0, i):
                if datatosort[j] > datatosort[j + 1]:
                    datatosort[j], datatosort[j + 1] = datatosort[j + 1], datatosort[j]
            i -= 1
        return datatosort
