from typing import List, Optional

class MaxWater: # Camel case convention
    def max_area(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        max_area = float("-inf")
        while left < right:

            area = min(height[left], height[right])*(right-left)
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
            max_area =  max(max_area, area)
        return max_area if max_area != float("-inf") else -1

    # # Brute Force solution
        # maxArea = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         width = j - i
        #         area = min(height[i], height[j])*width 
        #         maxArea = max(maxArea, area)
        # return maxArea
        

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    
    obj = MaxWater()
    print(obj.max_area(height))