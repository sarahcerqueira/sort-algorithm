from app.templates.sortTemplate import *
from app.models.quickSort import *
from app.models.partition.lomuto import *

class QuickSortLomuto(SortTemplate):

    def sort(datatosort:list)->list:
        QuickSort.quickSort(datatosort, 0, len(datatosort)-1, Lomuto)
        return datatosort