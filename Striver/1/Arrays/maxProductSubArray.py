#   Leetcode 152. Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # res = max(nums)
        # curMin, curMax = 1, 1

        # for n in nums:
        #     if n == 0 :
        #         curMin, curMax = 1, 1
        #         continue
        #     temp = curMax*n
        #     curMax = max(n*curMax, n*curMin, n)
        #     curMin = min(temp, n*curMin, n)
        #     res = max(res, curMax)

        # return res
        prefix = 1
        suffix = 1 
        #res = -9999999999999999999999
        res  = float("-inf")
        for i in range(len(nums)):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            prefix = prefix * nums[i]
            suffix = suffix * nums [len(nums)-(i+1)]

            res = max(res, max(prefix, suffix))

        return res 


if __name__ == "__main__":
    obj1 = Solution()
    nums =  [2,3,-2,4]
    print(obj1.maxProduct(nums))


            
