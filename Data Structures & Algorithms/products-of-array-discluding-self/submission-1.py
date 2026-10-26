class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)

        counter = 1
        for i in range(len(nums)):
            counter *= nums[i]
            left[i] = counter

        counter = 1
        for i in range(len(nums) - 1, -1, -1):
            counter *= nums[i]
            right[i] = counter
        
        res = [1] * len(nums)
        for i in range(len(res)):
            l = left[i - 1] if i > 0 else 1
            r = right[i + 1] if i < len(nums) - 1 else 1
            res[i] = l * r

        return res