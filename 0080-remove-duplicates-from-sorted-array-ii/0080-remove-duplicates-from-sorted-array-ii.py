class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        dist = {}
        
        for i in range(0,len(nums)):
            if dist.get(nums[i]) :
                dist[nums[i]] += 1
            else:
                dist[nums[i]] = 1
        
        flag = 0
        for j in dist:
            if dist[j]>=2:
                nums[flag] = j
                nums[flag+1] = j
                flag+=2
            else:
                nums[flag] = j
                flag+=1
        return flag
                
        