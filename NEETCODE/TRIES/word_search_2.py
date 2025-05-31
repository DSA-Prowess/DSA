from typing import List, Optional

# Brute force , DFS on exactly each words m.n*4^(m*n)

class TrieNode:
    def __init__(self):
        self.children = {} # key(value): child nodes (values for trie node)
        self.is_word = False

    def add_word(self, word):
        cur = self # here root node is the self here 
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

class Solution:
    def find_words(self, board:List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add_word(w) # here as you see we are passing self as object root to call add_word

        rows , cols = len(board), len(board[0]) # dimensions of the board 
        res , visit = set() , set()
        
        def dfs(r, c, node, word): # curr node in a Trie and what is the word so far you have seen 
            if (r < 0 or c < 0 or r >= rows or c >= cols
                or (r,c ) in visit or board[r][c] not in node.children):
                return 
            visit.add((r,c)) # visiting
            node = node.children[board[r][c]] # updating node with the current character that we visited in board [r][c]
            word += board[r][c]
            if node.is_word:
                res.add(word)

            
            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)
            visit.remove((r,c))  # backtracking 




        # Nested loop for our grid 
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        
        return list(res)
        
if __name__ == "__main__":
    
    res = Solution()
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    board = [["a","b"],["c","d"]]
    words = ["abcb"]
    result = res.find_words(board, words)
    print(result)