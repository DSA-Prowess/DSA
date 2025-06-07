class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return "" # handling empty string

        countT, window = {}, {} # Both are empty, coutT and current window 
        for c in t:
            countT[c] = 1 + countT.get(c, 0) # creatinh hashmap , storing number of counts 

        have, need = 0, len(countT) # as demonstrated in the video.

        res  = [-1, -1] # left and right pointer , 
        resLen = float("inf")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0) #Adding the count of window 

            if c in countT and window[c] == countT[c]:
                have +=1
            
            while have == need:
                # update your result 
                if ( r-l+1) < resLen:
                    res = [l,r]
                    resLen = (r - l+1) # computing the size of the window 

                # We have to make the string small as possibly can be , lets pop froom left.
                window[s[l]] -=1
                if s[l] in countT and window[s[l]] < countT[s[l]]: # by removing a count we make it less when needed to be 
                    have -=1
                l +=1 # since we are shifting a character , left from our window


        l, r = res

        return s[l : r+1] if resLen != float("inf") else ""
