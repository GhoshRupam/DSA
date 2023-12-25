class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
          length = len(nums)
          result = []  
        
          for i in range(0, 2 * length):
                if i < length:
                    result.append(nums[i])
                else:
                    result.append(nums[i - length])
        
          return result
        