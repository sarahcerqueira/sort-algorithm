from app.templates.sortTemplate import *

class MergerSort(SortTemplate):

    def sort(datatosort:list)->list:
        if len(datatosort) > 1:
            left = datatosort[0:len(datatosort) // 2]
            right = datatosort[len(datatosort) // 2: len(datatosort)]

            MergerSort.sort(left)
            MergerSort.sort(right)
            MergerSort.__merge(datatosort, left, right)

        return datatosort

    @staticmethod
    def __merge(datatosort:list, left:list, right:list)->None:
        l = 0
        r = 0
        i = 0

        while i < len(datatosort):
            if l >= len(left):
                datatosort[i] = right[r]
                r += 1
            elif r >= len(right):
                datatosort[i] = left[l]
                l += 1
            else:
                if left[l] < right[r]:
                    datatosort[i] = left[l]
                    l += 1
                else:
                    datatosort[i] = right[r]
                    r += 1

            i += 1


