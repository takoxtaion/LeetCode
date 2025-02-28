class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red = 0
        white = 0
        blue = 0
        for i in nums:
            if i == 0:
                red += 1
            if i == 1:
                white += 1
            if i == 2:
                blue += 1
        for i in range(red):
            nums.insert(i, 0)
        for i in range(red, red + white):
            nums.insert(i, 1)
        for i in range(red + white, red + white + blue):
            nums.insert(i, 2)
        nums[:] = nums[:int(len(nums) / 2)]