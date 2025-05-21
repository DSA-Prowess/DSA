class PrefixSum:
    def __init__(self, nums):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left-1] if left > 0 else 0 
        return (preRight - preLeft)
    

if __name__ == "__main__":
    nums = [-2,0,3,-5,2,-1]
    obj = PrefixSum(nums)

    print(obj.rangeSum(0,2))
    print(obj.rangeSum(2,5))
    print(obj.rangeSum(0,5))