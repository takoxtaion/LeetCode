class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = []
        for j in words: 
            for i in range(len(words)): 
                if j in words[i] and j != words[i]:
                    output.append(j)
        for i in output:
            while output.count(i) != 1:
                output.remove(i)
        return output

