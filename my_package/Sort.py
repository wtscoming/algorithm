'''
排序
'''
class Sort(object):
    def __init__(self):
        super().__init__()
    
    # 冒泡排序法
    @staticmethod
    def bubble_sort(alist):
        for i in range(len(alist) - 1):
            for j in range(len(alist) - i - 1):
                if alist[j] > alist[j + 1]:
                    alist[j], alist[j + 1] = alist[j + 1], alist[j]
        return alist
    
    # 选择排序法
    @staticmethod
    def select_sort(alist):
        for i in range(len(alist) - 1):
            min_position = i
            for j in range(i + 1, len(alist)):
                if alist[j] < alist[min_position]:
                    min_position = j
            if min_position != i:
                alist[i], alist[min_position] = alist[min_position], alist[i]
        return alist

    # 插入排序
    @staticmethod
    def insert_sort(alist):
        for i in range(1, len(alist)):
            tmp = alist[i]
            pos = i
            while pos > 0 and alist[pos - 1] > tmp:
                alist[pos] = alist[pos - 1]
                pos -= 1
            alist[pos] = tmp
        return alist

    # 归并排序
    @staticmethod
    def merge_sort(alist):
        if len(alist) > 1:
            mid = len(alist) // 2
            left = alist[:mid]
            right = alist[mid:]
            # 分别归并排序左右两部分
            Sort.merge_sort(left)
            Sort.merge_sort(right)
            # 合并部分有序的子序列
            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    alist[k] = left[i]
                    i += 1
                else:
                    alist[k] =  right[j]
                    j += 1
                k += 1
            # 将剩余部分接上
            while i < len(left):
                alist[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                alist[k] = right[j]
                j += 1
                k += 1
        return alist
    
    # 快速排序
    @staticmethod
    def quick_sort(alist):
        Sort.quick_sort_helper(alist, 0, len(alist) - 1)
        return alist

    @staticmethod
    def quick_sort_helper(alist, first, last):
        if first < last:
            split_point = Sort.partition(alist, first, last)
            Sort.quick_sort_helper(alist, first, split_point - 1)
            Sort.quick_sort_helper(alist, split_point + 1, last)

    @staticmethod
    def partition(alist, first, last):
        left = first + 1
        right = last
        while left <= right:
            while left <= right and alist[left] <= alist[first]:
                left += 1
            while left <= right and alist[right] >= alist[first]:
                right -= 1
            if left <= right:
                alist[left], alist[right] = alist[right], alist[left]
        alist[first], alist[right] = alist[right], alist[first]
        return right
