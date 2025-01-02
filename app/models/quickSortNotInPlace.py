from app.templates.sortTemplate import *

class QuickSortNotInPlace(SortTemplate):

    def sort(datatosort:list)->list:
        if len(datatosort) > 1:
            pivot = datatosort[0]
            left = []
            right = []
            middle = [pivot]
            i = 1

            while i < len(datatosort):
                if datatosort[i] < pivot:
                    left.append(datatosort[i])
                elif datatosort[i] > pivot:
                    right.append(datatosort[i])
                else:
                    middle.append(datatosort[i])

                i += 1

            left = QuickSortNotInPlace.sort(left)
            right = QuickSortNotInPlace.sort(right)

            return left + middle + right
        else:
            return datatosort