# Searching a 2D matrix 

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows , cols = len(matrix), len(matrix[0])
        up , down = 0 , rows - 1
        while up <= down:
            row = up + ( down - up)//2
            print(row)
            if target > matrix[row][-1]:
                up = row +1
            
            elif target < matrix[row][0]:
                down = row-1
            else:
                break

        if not (up <= down):
            return False
        
        left , right = 0 , cols -1
        while left <= right:
            mid = left + (right-left) //2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid -1 
            else:
                return True
        return False







if __name__ == "__main__":
    obj = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    res = obj.searchMatrix(matrix, target)
    print(res)