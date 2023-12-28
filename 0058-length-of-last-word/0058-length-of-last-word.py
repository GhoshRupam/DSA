class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        if len(s)==1:
            return 1
        first_char = -1
        count = 0
        
        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":
                first_char = i
                print(first_char)
                
            if first_char != -1 and s[i]!=" ":
                count+=1
            if first_char!=-1 and s[i]==" ":
                break
        return count
            
   
        