from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # res = ""
        # for s in strs[0]:
        #     for c in strs:
        #         if s != c  :
        #             return res 
        #     res +=s
        # return res 
        # Below logic is wrong 
        # for s in strs[0]:        # s is a CHARACTER from first string
        # for c in strs:       # c is an entire STRING from the array
        #      if s != c:       # Comparing CHARACTER vs STRING - always fails!
        # Missing index tracking 
        # No bounds checking 
        res = ""
        
        # Iterate through each character position of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]  # Current character from first string
            
            # Check this character against all other strings
            for string in strs:
                # Check bounds and character match
                if i >= len(string) or string[i] != char:
                    return res
            
            # If we reach here, all strings have the same character at position i
            res += char
            
        return res


if __name__ == "__main__":
    res = Solution()
    strs = ["dog","racecar","car"]
    strs = ["flower","flow","flight"]
    print(res.longestCommonPrefix(strs))