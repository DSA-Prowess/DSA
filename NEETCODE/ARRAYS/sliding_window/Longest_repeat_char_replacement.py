class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        left = 0
        maxf = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0 )
            maxf = max(maxf, count[s[right]])

            if ( right - left +1 ) - maxf > k:
                count[s[left]]-=1 
                left +=1
            
            res = max(res, right-left +1)
            print(count)
        return res 



if __name__ == "__main__":
    s = "ABAB"
    k = 2
    s = "AABABBA"
    k = 1
    obj = Solution()
    print(obj.characterReplacement(s,k))






if __name__ == "__main__":
    obj = Solution()
    s = "ABAB"
    k = 2
    res = obj.characterReplacement(s, k )
    print(res)