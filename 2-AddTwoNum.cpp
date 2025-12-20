#include <iostream>
#include <string>
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
 };
 
class Solution {
public:
    int carry = 0;
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode();
        if(!l1 && !l2) 
            if(carry > 0){
                dummy->val = carry;
                carry = 0;
                return dummy;
            }
            else{
                return nullptr;
            }    
            
        else if(!l1){
            dummy->val = l2->val + carry;
            carry = 0;
            if(dummy->val >= 10){
                carry = (dummy->val)/10;
                dummy->val = (dummy->val)%10;
            }
            dummy->next = addTwoNumbers(l1, l2->next);
            return dummy;

        }
        else if(!l2){
            dummy->val = l1->val+ carry;
            carry = 0;
            if(dummy->val >=10){
                carry = (dummy->val)/10;
                dummy->val = (dummy->val)%10;
            }
            dummy->next = addTwoNumbers(l1->next, l2);
            return dummy;
        }
        else{
            dummy->val = l1->val + l2->val + carry;
            carry = 0;
            if(dummy->val >= 10){
                carry = (dummy->val)/10;
                dummy->val = (dummy->val)%10;
            }
            dummy->next = addTwoNumbers(l1->next, l2->next);
            return dummy;
        }

    }
};

int main() {
    Solution s;
    ListNode* l1 = new ListNode();
    l1->val = 2;
    ListNode* l1_1 = new ListNode();
    l1_1->val = 4;
    l1->next = l1_1;
    ListNode* l1_2 = new ListNode();
    l1_2->val = 3;
    l1_1->next = l1_2;
    ListNode* l2 = new ListNode();
    l2->val=5;
    ListNode* l2_1 = new ListNode();
    l2_1->val = 6;
    l2->next = l2_1;
    ListNode* l2_2 = new ListNode();
    l2_2->val = 4;
    l2_1->next = l2_2;
    ListNode* result = s.addTwoNumbers(l1, l2);
    return 0;
}