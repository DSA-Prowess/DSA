from typing import List


# Below is Brute Force O(n2) solution
# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         n = len(nums)
#         res = float("inf")

#         for i in range(n):
#             curSum = 0
#             for j in range(i, n):
#                 curSum += nums[j]
#                 if curSum >= target:
#                     res = min(res, j - i + 1)
#                     break
        
#         return 0 if  res == float("inf") else res

class Solution:
   def minSubArrayLen(self, target: int, nums: List[int]) -> int:
       """
       Find minimum length of contiguous subarray with sum >= target.
       Uses sliding window (two pointers) approach.
       
       Time: O(n), Space: O(1)
       """
       # Edge case: empty array
       if not nums:
           return 0
           
       # Edge case: single element >= target
       if len(nums) == 1:
           return 1 if nums[0] >= target else 0
       
       # Initialize result to impossible value for comparison
       min_length = float('inf')
       
       # Sliding window pointers
       left = 0
       current_sum = 0
       
       # Expand window with right pointer
       for right in range(len(nums)):
           # Add current element to window sum
           current_sum += nums[right]
           
           # Contract window from left while sum >= target
           while current_sum >= target:
               # Calculate current window size
               current_window_size = right - left + 1
               
               # Update minimum length found so far
               min_length = min(min_length, current_window_size)
               
               # Remove leftmost element and shrink window
               current_sum -= nums[left]
               left += 1
               
               # Early termination: found minimum possible length
               if min_length == 1:
                   return 1
       
       # Return result: 0 if no valid subarray found, otherwise min length
       return 0 if min_length == float('inf') else min_length


# Test cases covering unique edge cases
if __name__ == "__main__":
   sol = Solution()
   
   # EDGE CASE 1: Empty array
   print(sol.minSubArrayLen(7, []))  # 0 - no elements
   
   # EDGE CASE 2: Single element cases
   print(sol.minSubArrayLen(4, [5]))     # 1 - single element >= target
   print(sol.minSubArrayLen(4, [3]))     # 0 - single element < target
   
   # EDGE CASE 3: No valid subarray (all elements sum < target)
   print(sol.minSubArrayLen(15, [1, 2, 3, 4]))  # 0 - total sum = 10 < 15
   
   # EDGE CASE 4: Entire array needed
   print(sol.minSubArrayLen(11, [1, 2, 3, 5]))  # 4 - need whole array
   
   # EDGE CASE 5: First element alone satisfies target
   print(sol.minSubArrayLen(4, [4, 1, 1, 1, 1]))  # 1 - immediate match
   
   # EDGE CASE 6: Last element alone satisfies target
   print(sol.minSubArrayLen(4, [1, 1, 1, 4]))  # 1 - match at end
   
   # EDGE CASE 7: All elements are same
   print(sol.minSubArrayLen(6, [2, 2, 2, 2]))  # 3 - need 3 elements of value 2
   
   # EDGE CASE 8: Target is 0 or negative (unusual but possible)
   print(sol.minSubArrayLen(0, [1, 2, 3]))  # 1 - any element >= 0
   
   # EDGE CASE 9: Very large numbers
   print(sol.minSubArrayLen(100000, [99999, 1, 1]))  # 2 - need first + one more
   
   # EDGE CASE 10: Multiple valid subarrays of same min length
   print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # 2 - multiple solutions: [4,3] or [2,4]
   
   # REGULAR TEST CASES
   print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # 2 - [4,3]
   print(sol.minSubArrayLen(4, [1, 4, 4]))           # 1 - [4]
   print(sol.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # 0 - impossible