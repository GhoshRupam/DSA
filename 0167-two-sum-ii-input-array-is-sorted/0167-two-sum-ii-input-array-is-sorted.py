class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        dist = {}
        
        for i,num in enumerate(numbers):
            
            if target-num in dist:
                return [dist[target-num]+1,i+1]
            dist[num] = i
            
        