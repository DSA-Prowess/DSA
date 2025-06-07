from typing import List 
from collections import deque 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        # We are using deque because adding and removing is O(1)
        q = deque() # index
        left = right = 0
        
        #nums = [1,3,-1,-3,5,3,6,7]

        while right < len(nums):
            # pop smaller values from q, if smaller value exist in our queue
            # before inseriting in the queue ,c heck the above condition
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)
            
            #remove left val from window, left window kai bahar chala gya
            if left > q[0]:
                q.popleft()
                
            if (right+1) >=k: # =1 kyuki 0 sai start horha base, comparing to k 
                output.append(nums[q[0]])
                # left is only going to be incremented once our window is size k
                left+=1
            right+=1 # right always going to increment.
            
        return output

        #Slightly less optimized but btter solution
        #def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # heap = []
        # output = []
        # for i in range(len(nums)):
        #     heapq.heappush(heap, (-nums[i], i))
        #     if i >= k - 1:
        #         while heap[0][1] <= i - k:
        #             heapq.heappop(heap)
        #         output.append(-heap[0][0])
        # return output
        