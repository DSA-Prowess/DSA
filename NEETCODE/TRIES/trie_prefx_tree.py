class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

    
class Tries:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word:str) -> None:
        cur = self.root 
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True 

    def search(self, word: str) -> bool:
        cur = self.root 
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end_of_word


    def starts_with(self, prefix:str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True 
    



if __name__ == "__main__":
    trie = Tries();
    trie.insert("apple");
    print(trie.search("apple"));   # return True
    print(trie.search("app"));     # return False
    print(trie.starts_with("app")); # return True
    trie.insert("app");
    print(trie.search("app"));     # return True