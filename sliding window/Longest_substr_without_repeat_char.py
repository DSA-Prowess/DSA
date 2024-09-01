class Solution:
    #def lengthOfLongestSubstring(self, s: str) -> int:
        # hashMap = {}
        # result = 0
        # left = 0
        # right = 0
        # for i in range(len(s)):
        #     if s[i] in hashMap:
        #         left = max(left, hashMap[s[i]]+1)
        #     right +=1
        #     hashMap[s[i]] = i
        #     result = max(right-left, result)
        # return result 
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0 
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l +=1
            charSet.add(s[r])
            res = max( res, r -l +1)
        return res 




if __name__ == "__main__":
    obj = Solution()
    s = "abcabcbb"
    res = obj.lengthOfLongestSubstring(s)
    print(res)