class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left , right = 0 , len(nums)
        
        while left <= right :
            mid = (left+right) //2
            if target == nums[mid]:
                return mid 
            
            # left sorted portion 
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid +1
                else:
                    right = mid -1
            #right sorted porttion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid -1 
                else:
                    left = mid +1
        return -1


if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    obj = Solution()
    res = obj.search(nums, target)
    print(res)