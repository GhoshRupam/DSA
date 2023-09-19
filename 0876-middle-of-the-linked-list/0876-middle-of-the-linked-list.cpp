/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        
        ListNode* temp = head;
        int length =1;
        while(temp->next != NULL )
        {
            temp = temp->next;
            length++;
        }
        int middle = length/2;
      
        
        while(head->next != NULL && middle>0)
        {
          
            head = head->next;
            middle--;
           
        }
        return head;
        
       
        
    }
};