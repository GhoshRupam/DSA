class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        len1 = len(word1)
        len2 = len(word2)
        i = 0
        j = 0
        ans =""
        while i<len1 or j<len2:
            if i<len1:
                ans +=word1[i]
            if j<len2:
                ans +=word2[j]
            i+=1
            j+=1
        return ans
            
            
            
        