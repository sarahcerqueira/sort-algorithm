from app.templates.sortTemplate import *

class BubbleSortPlus(SortTemplate):

    def sort(datatosort:list)->list:
        ordering = True
        i = len(datatosort) -1
        while ordering:
            ordering = False

            for j in range(0, i):
                if datatosort[j] > datatosort[j + 1]:
                    datatosort[j], datatosort[j + 1] = datatosort[j + 1], datatosort[j]
                    ordering = True
        return datatosort
