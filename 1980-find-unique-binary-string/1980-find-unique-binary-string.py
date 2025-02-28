class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        my_list = [bin(i)[2:] for i in range(2**len(nums))]
        for i in range(len(my_list)):
            while(len(my_list[i])) != len(nums):
                my_list[i] = "0" + my_list[i]
            if my_list[i] not in nums:
                return my_list[i]
        