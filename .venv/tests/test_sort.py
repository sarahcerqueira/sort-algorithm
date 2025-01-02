import unittest
from numpy import random
from app.modelos.bubbleSort import *

class TestSortAlgorithm(unittest.TestCase):

    def test_bubbleSort(self):
        self.sortList(BubbleSort)

    def sortList(self, algorithmClass:SortTemplate):
        datalist = list(random.randint(10000, size=100))
        sortedList = algorithmClass.sort(datatosort=datalist.copy())
        datalist.sort()
        self.assertListEqual(datalist, sortedList)
