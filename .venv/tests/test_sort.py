import unittest
from numpy import random
from app.models.bubbleSort import *
from app.models.bubbleSortPlus import *
from app.models.insertionSort import *
from app.models.selectionSort import *


class TestSortAlgorithm(unittest.TestCase):

    def test_bubbleSort(self):
        self.sortList(BubbleSort)

    def test_bubbleSortPlus(self):
        self.sortList(BubbleSortPlus)

    def test_insertionSort(self):
        self.sortList(InsertionSort)

    def test_selectionSort(self):
        self.sortList(SelectionSort)

    def sortList(self, algorithmClass:SortTemplate):
        datalist = list(random.randint(10000, size=100))
        sortedList = algorithmClass.sort(datatosort=datalist.copy())
        datalist.sort()
        self.assertListEqual(datalist, sortedList)
