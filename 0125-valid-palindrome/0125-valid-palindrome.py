class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_str = s.lower();
        newString = ''
        for i in range(0, len(new_str)):
            if new_str[i].isalnum():
                newString += new_str[i];
        
    
        
        reverse_string = "".join(reversed(newString))
   
        if newString == reverse_string:
            return True
        else:
            return False
                
        