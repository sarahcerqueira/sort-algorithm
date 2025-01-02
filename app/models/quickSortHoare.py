from app.templates.sortTemplate import *
from app.models.quickSort import *
from app.models.partition.hoare import *

class QuickSortHoare(SortTemplate):

    def sort(datatosort:list)->list:
        QuickSort.quickSort(datatosort, 0, len(datatosort)-1, Hoare)
        return datatosort