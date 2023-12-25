class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        new_set = set(nums)
    
        len_array = len(nums)
        len_set = len(new_set)
    
        if len_array == len_set:
            return False
        else:
            return True
        