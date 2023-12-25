class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        new_dist = {}
        new_dist1 = {}
        if len(s) != len(t):
            return False
        for i in range(0,len(s)):
            if new_dist.get(s[i]):
                new_dist[s[i]]+=1
            else:
                new_dist[s[i]] =  1
            
            if new_dist1.get(t[i]):
                new_dist1[t[i]]+=1
            else:
                new_dist1[t[i]] =  1
        
        if new_dist == new_dist1:
            return True
        else:
            return False
            
        