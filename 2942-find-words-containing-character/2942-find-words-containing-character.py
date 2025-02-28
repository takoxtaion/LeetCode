class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        output = []
        for index, i in enumerate(words):
            if x in i:
                output.append(index)            
        return output

                    

