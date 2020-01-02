'''
二分搜索
'''
class BinarySearch:
    
    @staticmethod
    def find(alist, item):
        left = 0
        right = len(alist) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if alist[mid] == item:
                return mid
            elif item < alist[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
