from typing import List, Optional

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right =  i+1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -=1
                
                    # tricky duplicate condition
                    while left < right and nums[left] == nums[left-1]: # skip duplicates
                        left +=1
                    # Check of third element duplicate is not required.
                    # while left < right and nums[right] == nums[right+1]: #Skip duplicates 
                    #     right -=1
                    # [-2,-2,0,0,2,2]( left and right pointers )
                elif total < 0:
                    left +=1
                else:
                    right -=1

        return res 

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    
    obj = Solution()
    print(obj.threeSum(nums))
    # expected Output: [[-1,-1,2],[-1,0,1]]