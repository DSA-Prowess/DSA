class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
         self.root = TrieNode()


    def add_word(self, word:str) -> None:
        cur = self.root 
        # insert all the words in a Trie 
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word:str ) -> bool:
        #Recursive
        def dfs(j, root):
            cur =   root 
            for i in range(j, len(word)):
                c = word[i]

                if c == "." : # you can match any character 
                # Recursive side
                    for child in cur.children.values():
                        if dfs(i+1 , child): # i+1 , we are moving down a child ( skipping the .)
                            return True 
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word 
        return dfs(0, self.root)
    
if __name__ == "__main__":
    wordDictionary = WordDictionary();
    wordDictionary.add_word("bad");
    wordDictionary.add_word("dad");
    wordDictionary.add_word("mad");
    print(dir(wordDictionary))
    print(wordDictionary.root)
    print(wordDictionary.search("pad")); # return False
    print(wordDictionary.search("bad")); # return True
    print(wordDictionary.search(".ad")); # return True
    print(wordDictionary.search("b..")); # return True