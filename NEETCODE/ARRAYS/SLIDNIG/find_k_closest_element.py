from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Find k closest elements to x in sorted array.
        
        Approach: Binary search + Two pointers expansion
        Time: O(log n + k), Space: O(1)
        """
        # Edge case: return entire array if k >= array length
        if k >= len(arr):
            return arr
            
        # Edge case: empty array
        if not arr:
            return []
        
        # Binary search to find insertion point for x
        left, right = 0, len(arr)
        while left < right:  # ✅ Correct condition
            mid = left + (right - left) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        
        # Now 'left' is the insertion point
        # Set up two pointers around the insertion point
        left -= 1   # Point to element just before insertion point
        right = left + 1  # Point to insertion point or element after
        
        # Expand window to get k closest elements
        while right - left - 1 < k:
            # Boundary checks and expansion logic
            if left < 0:
                # Can't go further left, must expand right
                right += 1
            elif right >= len(arr):
                # Can't go further right, must expand left
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                # Left element is closer or equal, expand left
                left -= 1
            else:
                # Right element is closer, expand right
                right += 1
        
        # Return k elements between left and right (exclusive)
        return arr[left + 1:right]


# Test cases with edge cases
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    k = 3
    x = 3
    print(sol.findClosestElements(arr, k, x))  # [2,3,4]
    # EDGE CASE 1: x smaller than all elements
    print(sol.findClosestElements([1, 2, 3, 4, 5], 3, 0))  # [1, 2, 3]
    
    # EDGE CASE 2: x larger than all elements  
    print(sol.findClosestElements([1, 2, 3, 4, 5], 3, 10))  # [3, 4, 5]
    
    # EDGE CASE 3: x exists in array
    print(sol.findClosestElements([1, 2, 3, 4, 5], 3, 3))  # [2, 3, 4]
    
    # EDGE CASE 4: k equals array length
    print(sol.findClosestElements([1, 2, 3], 3, 2))  # [1, 2, 3]
    
    # EDGE CASE 5: k = 1 (single element)
    print(sol.findClosestElements([1, 2, 3, 4, 5], 1, 3))  # [3]
    
    # EDGE CASE 6: Array with duplicates
    print(sol.findClosestElements([1, 1, 1, 2, 2, 2], 3, 1))  # [1, 1, 1]
    
    # EDGE CASE 7: Single element array
    print(sol.findClosestElements([1], 1, 1))  # [1]
    
    # EDGE CASE 8: x between two elements (tie-breaking)
    print(sol.findClosestElements([1, 3], 1, 2))  # [1] (left wins tie)
    
    # REGULAR TEST CASES
    print(sol.findClosestElements([1, 2, 3, 4, 5], 4, 3))  # [1, 2, 3, 4]
    print(sol.findClosestElements([1, 2, 3, 4, 5], 4, -1)) # [1, 2, 3, 4]