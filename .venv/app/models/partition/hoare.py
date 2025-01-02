from app.templates.partitionTemplate import *

class Hoare(PartitionTemplate):

    def partition(dataList: list, indexStart: int, indexEnd: int) -> int:
        l = indexStart
        pivot = indexEnd
        r = indexEnd - 1

        while l <= r:
            while l <= r and dataList[l] < dataList[pivot]:
                l += 1
            while l <= r and dataList[r] > dataList[pivot]:
                r -= 1
            if l <= r:
                dataList[l], dataList[r] = dataList[r], dataList[l]
                l += 1
                r -= 1

        dataList[l], dataList[pivot] = dataList[pivot], dataList[l]

        return l