class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        my_list = [i for i in nums if i != 0]
        for i in range(nums.count(0)):
            my_list.append(0)
        return my_list