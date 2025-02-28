class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = True if len(nums) != len(set(nums)) else False
        return result