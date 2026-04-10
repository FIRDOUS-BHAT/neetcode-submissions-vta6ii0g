class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums:
            tracker  = {}
            
            for key, num in enumerate(nums):
                if num in tracker:
                    tracker[num] += 1
                    return True
                else:
                    tracker[num] = 1    
        return False

        