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
    bool isPalindrome(ListNode* head) {
        vector<int> num;
        vector<int> rev;
        int store = 0;
        bool check = true;
        
        ListNode* temp = head;
        
        while(temp != NULL){
            store = temp->val;
            num.push_back(store);
            rev.push_back(store);
            temp = temp->next;
        }
        
        reverse(rev.begin(), rev.end());
        
        for(int i = 0; i < num.size(); i++){
            if(num[i] == rev[i]){
                check = true;
            }else{
                check = false;
                return check;
            }
        }
        return check;
    }
};