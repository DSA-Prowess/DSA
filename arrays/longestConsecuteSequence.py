# Longest consecutive sequence

class Solution:
    def longest_consecutive(self, nums : list[int]):
        numSet = set(nums)
        longest = 0
        for num in nums:
            if (num-1) not in numSet:
                lenght = 1
                while (lenght +num) in numSet:
                    lenght +=1
                longest = max(lenght, longest)
        return longest



if __name__ == "__main__":  
    nums = [100,4,200,1,3,2]
    nums1 = [0,3,7,2,5,8,4,6,0,1]
    obj = Solution()
    print(obj.longest_consecutive(nums))
    print(obj.longest_consecutive(nums1))