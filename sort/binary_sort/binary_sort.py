import unittest

'''
    左闭右闭区间的二分搜索
    [left,right]
    迭代法
'''
def binary_sort_left_closed_right_closed_iterative(nums,target,left,right):
    # 因为区间为左闭右闭区间.所以left 等于 right 是有意义的
    while(left <= right):
        mid = left + ((right - left) >> 1)
        if nums[mid] == target:
            return mid
        # 说明target在左区间    
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

'''
    左闭右闭区间的二分搜索
    [left,right]
    递归法
'''
def binary_sort_left_closed_right_closed_recursive(nums,target,left,right):
    mid = left + ((right - left) >> 1)
    if nums[mid] == target:
        return mid
    elif target > nums[mid]:
        return binary_sort_left_closed_right_closed_recursive(nums,target,mid + 1,right)
    elif target < nums[mid]:
        return binary_sort_left_closed_right_closed_recursive(nums,target,left,mid - 1)
            
'''
    左闭右开区间的二分搜索
    [left,right)
    迭代法
'''
def binary_sort_left_closed_right_open_iterative(nums,target,left,right):
    # 由于是左闭右开区间,所以 left = right不存在
    while(left < right):
        mid = left + ((right - left) >> 1)
        if nums[mid] == target:
            return mid
            # 由于是右开区间,所以不需要 - 1
        elif target < nums[mid]:
            right = mid
        elif target > nums[mid]:
            left = mid + 1

    return -1
        


'''
    左闭右开区间的二分搜索
    [left,right)
    递归法
'''
def binary_sort_left_closed_right_open_recursive(nums,target,left,right):
    mid = left + ((right - left) >> 1)
    if target < nums[mid]:
        return binary_sort_left_closed_right_open_recursive(nums,target,left,mid)
    elif target > nums[mid]:
        return binary_sort_left_closed_right_open_recursive(nums,target,mid + 1,right)
    else:
        return mid

class binary_test(unittest.TestCase):

    def test_binary_sort_left_closed_right_closed_iterative(self):
        nums = [0,1,2,3,4,5,6,7,8,9]
        target = 9
        self.assertEqual(binary_sort_left_closed_right_closed_iterative(nums,target,0,len(nums) - 1),target)

    def test_binary_sort_left_closed_right_closed_recursive(self):
        nums = [0,1,2,3,4,5,6,7,8,9]
        target = 9
        self.assertEqual(binary_sort_left_closed_right_closed_recursive(nums,target,0,len(nums) - 1),target)

    def test_binary_sort_left_closed_right_open_iterative(self):
        nums = [0,1,2,3,4,5,6,7,8,9]
        target = 9
        self.assertEqual(binary_sort_left_closed_right_open_iterative(nums,target,0,len(nums)),target)        

    def test_binary_sort_left_closed_right_open_recursive(self):
        nums = [0,1,2,3,4,5,6,7,8,9]
        target = 9
        self.assertEqual(binary_sort_left_closed_right_open_recursive(nums,target,0,len(nums)),target)

if __name__ == '__main__':
    unittest.main()
