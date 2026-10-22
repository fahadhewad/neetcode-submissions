class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stored_values = {}

        for i in range(len(nums)):
            remainder = target - nums[i]

            if remainder in stored_values:
                return [stored_values.get(remainder), i]
            else:
                stored_values[nums[i]] = i
        else:
            return [0,0]