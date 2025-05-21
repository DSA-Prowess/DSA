
def maxProductArray(nums):
    """
    This function takes a list of integers and returns the maximum product of any contiguous subarray.
    :param nums: List[int]
    :return: int
    """
    # if not nums:
    #     return 0

    # max_product = nums[0]
    # min_product = nums[0]
    # result = nums[0]

    # for i in range(1, len(nums)):
    #     if nums[i] < 0:
    #         max_product, min_product = min_product, max_product

    #     max_product = max(nums[i], max_product * nums[i])
    #     min_product = min(nums[i], min_product * nums[i])

    #     result = max(result, max_product)

    # return result
    maxNum = float('-inf')
    maxNum2 = float('-inf')
    for i in range(len(nums)):
        if nums [i] > maxNum:
            maxNum = nums[i]
    """Finding second maximum number in the list"""
    for i in range(len(nums)):
        if nums[i] > maxNum2 and nums[i] < maxNum:
            maxNum2 = nums[i]
    print(f"Maximum number is {maxNum} and second maximum number is {maxNum2}")
    
   

# Example usage:
if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    print(maxProductArray(nums))  # Output: 6 (subarray [2, 3])
    
    nums = [-2, 0, -1]
    print(maxProductArray(nums))  # Output: 0 (subarray [0])
    
    nums = [-2, 3, -4]
    print(maxProductArray(nums))  # Output: 24 (subarray [-2, 3, -4])