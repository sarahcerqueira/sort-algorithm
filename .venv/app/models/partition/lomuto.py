from app.templates.partitionTemplate import *

class Lomuto(PartitionTemplate):

    def partition(dataList:list, indexStart: int, indexEnd:int)->int:
        pivot = dataList[indexEnd]
        s = indexStart
        i = indexStart

        while i < indexEnd:
            if dataList[i] <= pivot:
                dataList[i], dataList[s] = dataList[s], dataList[i]
                s = s + 1
            i += 1

        dataList[indexEnd], dataList[s] = dataList[s], dataList[indexEnd]

        return s