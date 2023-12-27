class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        print(nums)
        if k==1:
            return 0
        minValue = 999999 
        s,e = 0,k-1;
        while e < len(nums):
            
            if(nums[e] - nums[s]) <minValue:
                minValue = (nums[e] - nums[s])
            s+=1
            e+=1
                
        return minValue
            
            
            
        