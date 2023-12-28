class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        previous_index = -1; 
        for i in range(0,len(s)):
            flag =0
            for j in range(0,len(t)):
                if s[i]==t[j] and j>previous_index:
                    previous_index = j
                    flag = 1
                    break
            if flag == 0:
                return False
        return True
        
                
                
        
        