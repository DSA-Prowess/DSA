class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        left , right = 0 , len(nums)-1

        while left <= right :
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = (left+right) //2 
            res = min (res, nums[mid])

            if nums[mid] > nums[left]:
                left = mid +1
            else:
                right = mid -1 
        return res 




if __name__ == "__main__":
    nums = [3,4,5,1,2]
    obj = Solution()
    res = obj.findMin(nums)
    print(res)