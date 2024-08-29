#KOKO eating banannas
#value of k , at most koko can eat one entire pile of bananas 

import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left , right = 1 , max(piles)
        res = right
        while left <=right :
            k = (left+right) // 2
            hours = 0
            for p in piles :
                hours += math.ceil(p/k)

            if hours<=h:
                res = min(res,k)
                right = k-1
            else:
                left = k+1

        return res 





if __name__== "__main__":
    """
    Minimum speed k= ? , that koko can use to eat all of these piles(4 piles) in 8 hours
    """
    piles = [3,6,7,11]
    #take for example k = 1 [3/1 = 3hrs , 6/1 = 6 hrs] {9 hrs } k = 1 is not going to work 
    # k !=0 not eating any piles , k can be max in our pile ( k = 11) { 1 hr} every single pile in 4 hrs[k= [1..11]], k<=8 hrs 
    # apply binary serch in p
    h = 8
    obj = Solution()
    res = obj.minEatingSpeed(piles, h)
    print(res)