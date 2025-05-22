class MinWindowSubstring:
    def min_window(self, s: str, t: str) -> str:
        if t == "" : return ""
        count_t , window = {}, {}

        for c in t:
            count_t[c] = 1 + count_t.get(c,0)

        have, need = 0, len(count_t)

        res = [-1,-1]
        res_len = float("inf")
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c,0) #Adding the count of window 
            if c in count_t and window[c] == count_t[c]:
                have +=1

            while have == need:
                # update your result 
                if (right -left +1 ) < res_len:
                    res = [left,right]
                    res_len = right - left + 1

                window[s[left]] -=1 
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -=1
                left +=1

        l , r = res
        return s[l: r+1] if res_len != float("inf") else ""



if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    result_obj = MinWindowSubstring()
    result = result_obj.min_window(s,t)
    print(result)
