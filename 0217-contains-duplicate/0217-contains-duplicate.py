class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        new_set = set(nums)
        
        if len(new_set) == len(nums):
            return False
        else:
            return True
        