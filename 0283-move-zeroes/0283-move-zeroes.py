class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        nuzero = 0
        for i in nums:
            
            if i != 0:
                nums[count] = i
                count+=1
            else:
                nuzero+=1
        for j in range(len(nums)-1,-1,-1):
            
            if nuzero!=0:
                nums[j] = 0
                nuzero-=1
                
        