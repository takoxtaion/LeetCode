class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        output = False
        if len(s) == len(goal):
            if goal in 2 * s:
                output = True
        return output
