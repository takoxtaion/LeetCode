class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in a:
                return [a[diff], i]
            a[n] = i

        return []

        


            
            