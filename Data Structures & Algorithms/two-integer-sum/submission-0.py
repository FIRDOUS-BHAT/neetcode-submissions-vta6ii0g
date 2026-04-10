class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for key,num in enumerate(nums):
            complement = target - num
            if complement in seen and key != seen[complement]:
                return [seen[complement], key]
            seen[num] = key

        