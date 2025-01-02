import unittest
from app.models.mergerSort import MergerSort
from numpy import random
from app.models.bubbleSort import *
from app.models.bubbleSortPlus import *
from app.models.insertionSort import *
from app.models.selectionSort import *
from app.models.quickSortLomuto import *
from app.models.quickSortHoare import *
from app.models.quickSortNotInPlace import *
from app.models.mergerSort import *
from app.models.heapSortInPlace import *
from app.models.heapSort import *


class TestSortAlgorithm(unittest.TestCase):

    def test_bubbleSort(self):
        self.sortList(BubbleSort)

    def test_bubbleSortPlus(self):
        self.sortList(BubbleSortPlus)

    def test_insertionSort(self):
        self.sortList(InsertionSort)

    def test_selectionSort(self):
        self.sortList(SelectionSort)

    def test_quickSortLomuto(self):
        self.sortList(QuickSortLomuto)

    def test_quickSortHoare(self):
        self.sortList(QuickSortHoare)

    def test_quickSortNotInPlace(self):
        self.sortList(QuickSortNotInPlace)

    def test_mergerSort(self):
        self.sortList(MergerSort)

    def test_heapSortNotInPlace(self):
        self.sortList(HeapSortNotInPlace)

    def test_heapSort(self):
        self.sortList(HeapSort)

    def sortList(self, algorithmClass:SortTemplate):
        datalist = list(random.randint(10000, size=100))
        sortedList = algorithmClass.sort(datatosort=datalist.copy())
        datalist.sort()
        self.assertListEqual(datalist, sortedList)
