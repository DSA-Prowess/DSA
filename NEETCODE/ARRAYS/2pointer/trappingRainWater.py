from typing import List, Optional

class TrapRainWater:

    def trap_water(self, height: List[int]) -> int:
        res = 0
        if not height:
            return 0 # instead this we can raisError
        left ,right = 0 , len(height)-1
        left_max, right_max = height[left], height[right]
        #Determine rain water equation trap rain water min(maxL,maxR) - h[i]
        while left < right:
            if left_max < right_max:
                left +=1
                left_max = max(left_max, height[left])
                res += left_max - height[left]
            else:
                right -=1
                right_max = max(right_max, height[right])
                res += right_max - height[right]
        return res 


if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height = [4,2,0,3,2,5]
    
    obj = TrapRainWater()
    print(obj.trap_water(height))
    # expected Output: [[-1,-1,2],[-1,0,1]]