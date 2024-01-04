class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        demo = {"b": 0, "a" : 0, "l" : 0, "o":0, "n" : 0}
        
        for i in text:
            if i in demo:
                demo[i] +=1
        demo["l"] = demo["l"]//2
        demo["o"] = demo["o"]//2
        
        return min(demo.values())
        