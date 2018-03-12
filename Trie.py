class TrieNode:
    def __init__(self):
        self.childs = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    """
    @param: word: a string
    @return: nothing
    """

    def insert(self, word):
        node = self.root
        for char in word:
            child = node.childs.get(char)
            if child is None:
                child = TrieNode()
                node.childs[char] = child
            node = child
        node.is_word = True

    """
    @param: word: a string
    @return: if the word is in the trie.
    """

    def search(self, word):
        node = self.root
        for char in word:
            node = node.childs.get(char)
            if node is None:
                return False
        return node.is_word

    """
    @param: prefix: a string
    @return: if there is any word in the trie that starts with the given prefix.
    """

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            node = node.childs.get(char)
            if node is None:
                return False
        return True
