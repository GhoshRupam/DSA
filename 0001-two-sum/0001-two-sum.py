class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        ans = {}
        for i in range(0,len(nums)):
            diff = target - nums[i]
            
            if diff in ans:
                return [ans[diff],i]
            else:
                ans[nums[i]] = i 
        