def longest_substring_without_repeating_characters(s: str) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    #https://leetcode.com/problems/longest-substring-without-repeating-characters/
    #The above leetcode in general is more easy to comprehend and understand
    hashMap = {}
    result = 0
    left = 0
    right = 0
    for i in range(len(s)):
         #Updating left using max(left, hashMap[s[i]] + 1)
        #We move left to hashMap[s[i]] + 1 to skip over the previous occurrence of the duplicate character.
        #However, we take max(left, hashMap[s[i]] + 1) to ensure left never moves backward.
        if s[i] in hashMap:
            left = max(left, hashMap[s[i]]+1)
        right +=1
        hashMap[s[i]] = i
        result = max(right-left, result)
    return result 


if __name__ == "__main__":
    s = "abcabcbb"
    res = longest_substring_without_repeating_characters(s)
    print(res)
