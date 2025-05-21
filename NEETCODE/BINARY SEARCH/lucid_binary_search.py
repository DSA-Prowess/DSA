class Solution:
    def search( self, nums, target  ):
        low = 0
        high = len(nums) - 1
        while low <= high :
            mid = low + (high - low) // 2 # to avoid overflow
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid 
        return -1 







if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    obj = Solution()
    res = obj.search(nums,target)
    print(res)