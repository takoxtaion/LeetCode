class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        elif digits[-1] == 9 and len(set(digits)) != 1:
            for i in range(1, len(digits) + 1):
                if digits[-i] != 9:
                    digits[-i] += 1
                    return digits
                digits[-i] = 0  
        else:
            new_list = [1]
            for n in digits:
                new_list.append(0)
            return new_list