class Solution:
   def checkInclusion(self, s1: str, s2: str) -> bool:
       # Edge case: s1 longer than s2, impossible to find permutation
       if len(s1) > len(s2):
           return False
       
       # Edge case: empty s1, any string contains empty permutation
       if not s1:
           return True
           
       # Build frequency map for s1 (target pattern)
       s1_count = {}
       for char in s1:
           s1_count[char] = s1_count.get(char, 0) + 1
       
       # Sliding window approach - fixed size window of len(s1)
       window_size = len(s1)
       s2_count = {}
       
       # Initialize first window
       for i in range(window_size):
           char = s2[i]
           s2_count[char] = s2_count.get(char, 0) + 1
       
       # Check if first window matches
       if s1_count == s2_count:
           return True
       
       # Slide window through rest of s2
       for i in range(window_size, len(s2)):
           # Add new character (right side of window)
           new_char = s2[i]
           s2_count[new_char] = s2_count.get(new_char, 0) + 1
           
           # Remove old character (left side of window)
           old_char = s2[i - window_size]
           s2_count[old_char] -= 1
           # Clean up zero counts to match dictionary comparison
           if s2_count[old_char] == 0:
               del s2_count[old_char]
           
           # Check if current window matches target
           if s1_count == s2_count:
               return True
       
       return False
   


# Test cases with edge cases
if __name__ == "__main__":
   sol = Solution()
   
   # Basic positive case
   print(sol.checkInclusion("ab", "eidbaooo"))  # True - "ba" found
   
   # Basic negative case  
   print(sol.checkInclusion("ab", "eidboaoo"))  # False - no "ab" permutation
   
   # Edge case: s1 longer than s2
   print(sol.checkInclusion("abcd", "abc"))     # False
   
   # Edge case: empty s1
   print(sol.checkInclusion("", "abc"))         # True
   
   # Edge case: identical strings
   print(sol.checkInclusion("abc", "abc"))      # True
   
   # Edge case: single character
   print(sol.checkInclusion("a", "ab"))         # True
   print(sol.checkInclusion("a", "b"))          # False
   
   # Edge case: duplicate characters in s1
   print(sol.checkInclusion("aab", "abaa"))     # True - "aba" or "aab" found
   
   # Edge case: s1 at end of s2
   print(sol.checkInclusion("ab", "cdab"))      # True
   
   # Edge case: multiple valid permutations
   print(sol.checkInclusion("ab", "abab"))      # True - "ab" at start