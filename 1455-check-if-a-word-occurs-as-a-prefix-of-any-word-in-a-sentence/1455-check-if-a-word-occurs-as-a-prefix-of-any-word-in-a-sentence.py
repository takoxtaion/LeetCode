class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        output = -1
        sentence = sentence.split()
        for i in sentence:
            if i.startswith(searchWord):
                output = sentence.index(i) + 1
                break
        return output
            