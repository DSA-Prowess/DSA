from typing import List
import collections
class MaxSlidingWindow:
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        output = []
        # We are using deque because adding and removing is O(1)
        q = collections.deque() # index
        left = right = 0
        
        #nums = [1,3,-1,-3,5,3,6,7]

        while right < len(nums):
            # pop smaller values from q, if smaller value exist in our queue
            # before inseriting in the queue ,check the above condition and in q we store only indexes
            while q and nums[q[-1]] < nums[right]:
                q.pop()


            q.append(right)
            
            #remove left val from window, left window kai bahar chala gya
            if left > q[0]: # out of bounds
                q.popleft()
                
            if (right+1) >=k: # =1 kyuki 0 sai start horha base, comparing to k 
                output.append(nums[q[0]]) # maximim is the leftmost position of the queue.
                # left is only going to be incremented once our window is size k
                left+=1
            right+=1
            
        #return output
        print(output)
        output = []
        print(output)
        # Below is the BRute force solution 
        for i in range(len(nums) - k + 1):
            maxi = nums[i]
            for j in range(i, i + k ):
                maxi = max(maxi, nums[j])
            output.append(maxi)
        return output



if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    result_obj = MaxSlidingWindow()
    result = result_obj.max_sliding_window(nums , k)
    print(result)
