class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        flag = n
        
        if len(flowerbed) == 1:
            if flowerbed[0]==0:
                flag-=1
                if flag<=0:
                    return True
                else:
                    return False
        
        if flowerbed[0] == 0:
            if flowerbed[1] == 0:
                flag-=1
                flowerbed[0] = 1
        if flowerbed[-1] == 0:
            if flowerbed[-2] == 0:
                flag-=1
                flowerbed[-1] = 1
        for i in range(1,len(flowerbed)-1):
            
            if flowerbed[i-1]==flowerbed[i] and flowerbed[i] == flowerbed[i+1] and flowerbed[i]==0:
                flag-=1
                flowerbed[i] = 1
            
        if flag<=0:
            return True
        else:
            return False
            
    
        