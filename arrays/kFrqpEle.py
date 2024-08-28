# Top K frequen elements
# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        count = Counter(nums)
        #return [key for key, value in count.most_common(k)]
        for k,v in count.items():
            print(k,v)

if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    print(sol.topKFrequent(nums, k))
    nums = [1]
    k = 1
    print(sol.topKFrequent(nums, k))
    nums = [1,2,3,4,5,6,7,8,9,10]
    k = 3
    print(sol.topKFrequent(nums, k))
    nums = [1,1,1,2,2,3]
    k = 3
    print(sol.topKFrequent(nums, k))
    nums = [1,1,1,2,2,3]
    k = 1
    print(sol.topKFrequent(nums, k))
    nums = [1,1,1,2,2,3]
    k = 4
    print(sol.topKFrequent(nums, k))
