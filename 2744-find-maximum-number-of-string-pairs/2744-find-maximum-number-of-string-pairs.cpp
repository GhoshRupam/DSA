class Solution {
public:
    int maximumNumberOfStringPairs(vector<string>& words) {
        
        
        int result =0;
        for(int i=0;i<words.size();i++)
        {
            string temp = words[i];
    
            swap(temp[0],temp[1]);
            
            for(int j=i+1;j<words.size();j++)
            {
                if(words[j] == temp)
                {
                    result++;
                }
            }
        }
        return result;
        
        
    }
};