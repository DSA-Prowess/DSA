class Solution:
   def checkInclusion(self, s1: str, s2: str) -> bool:
       # Edge case: s1 longer than s2, impossible to find permutation
       if len(s1) > len(s2):
           return False
           
       # Edge case: empty s1, any string contains empty permutation
       if not s1:
           return True
       
       # Build frequency map for s1 (target pattern we need to match)
       count1 = {}
       for c in s1:
           count1[c] = 1 + count1.get(c, 0)
       
       # Number of unique characters in s1 that we need to match exactly
       need = len(count1)
       
       # Try every possible starting position in s2
       for i in range(len(s2)):
           # Reset for each new starting position
           count2 = {}  # Current window's character frequencies
           cur = 0      # Number of characters we've matched exactly
           
           # Extend window from current starting position
           for j in range(i, len(s2)):
               # Add current character to our window
               count2[s2[j]] = 1 + count2.get(s2[j], 0)
               
               # Early termination: if we have more of any character than needed
               # No point continuing this window as it can never match
               if count1.get(s2[j], 0) < count2[s2[j]]:
                   break
               
               # Check if we've achieved perfect match for this character type
               if count1.get(s2[j], 0) == count2[s2[j]]:
                   cur += 1
               
               # Success: we've matched all required character frequencies
               if cur == need:
                   return True
                   
               # Optimization: if window size exceeds s1 length, break
               # (permutation must have same length)
               if j - i + 1 == len(s1):
                   break
       
       return False

# Test cases with edge cases
if __name__ == "__main__":
   sol = Solution()
   
   # Basic positive case
   print(sol.checkInclusion("ab", "eidbaooo"))  # True - "ba" found at index 3-4
   
   # Basic negative case  
   print(sol.checkInclusion("ab", "eidboaoo"))  # False - no valid permutation
   
   # Edge case: s1 longer than s2
   print(sol.checkInclusion("abcd", "abc"))     # False - impossible
   
   # Edge case: empty s1  
   print(sol.checkInclusion("", "abc"))         # True - empty permutation exists
   
   # Edge case: empty s2 with non-empty s1
   print(sol.checkInclusion("a", ""))           # False - can't find 'a' in empty string
   
   # Edge case: identical strings
   print(sol.checkInclusion("abc", "abc"))      # True - exact match
   
   # Edge case: single character match
   print(sol.checkInclusion("a", "ab"))         # True - 'a' found at index 0
   print(sol.checkInclusion("a", "ba"))         # True - 'a' found at index 1
   print(sol.checkInclusion("a", "b"))          # False - 'a' not found
   
   # Edge case: duplicate characters in s1
   print(sol.checkInclusion("aab", "abaa"))     # True - "aba" found at index 1-3
   
   # Edge case: all characters same
   print(sol.checkInclusion("aa", "aaaa"))      # True - "aa" found multiple places
   
   # Edge case: permutation at very end
   print(sol.checkInclusion("ab", "cdddba"))    # True - "ba" at end
   
   # Edge case: no common characters
   print(sol.checkInclusion("ab", "cd"))        # False - completely different chars