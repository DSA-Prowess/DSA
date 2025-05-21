"""
80. Remove Duplicates from Sorted Array II

"""

from typing import List, Optional
class Solution:
    def removeDuplicates(self, nums:List[int]) -> int:
        left , right = 0, 0 
        while right < len(nums):
            count = 1 
            while right +1 < len(nums) and nums[right] == nums[right+1]:
                count += 1
                right += 1

            for i in range(min(2,count)):
                nums[left] = nums[right]
                left +=1
            right +=1 
        return left

if __name__ == "__main__": # can be used to call within same module.

    obj = Solution()
    nums = [1,1,1,2,2,3]
    print(obj.removeDuplicates(nums))
    print(nums)