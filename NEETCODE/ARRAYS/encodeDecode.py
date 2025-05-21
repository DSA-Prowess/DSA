class Solution:
    # intuition encode the string based
    # 
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res

if __name__ == "__main__":
    sol = Solution()
    strs = ["hello", "world"]
    # print(sol.encode(strs))
    print(sol.decode(sol.encode(strs)))