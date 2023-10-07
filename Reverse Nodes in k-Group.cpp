// Recursive approach Space O(N) (Stack)
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        int size = 0;
        ListNode *temp = head;
        while(temp!=NULL){
            temp = temp -> next;
            size++;
        }
        if(size < k)    return head;   

        // Base call
        if(head == NULL)
            return NULL;

        // Step 1 - Reverse first k nodes
        ListNode *curr = head, *prev = NULL, *next = NULL;
        int count = 0;
        while(curr != NULL && count <k){
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
            count++;
        }

        // Step 2 - Use recursion to reverse rest of the nodes
        if(next!=NULL){
            head->next = reverseKGroup(next, k);
        }

        // Step 3 - Return head
        return prev;
    }
};

// Iterative approach Space - O(1)
class Solution {
public:
	ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *dummy = new ListNode(0);
        dummy->next = head;
        ListNode *before = dummy, *after = head;
        ListNode *curr = NULL, *prev = NULL, *nxt = NULL;
        while(true){
            ListNode* cursor = after;
            for(int i = 0; i < k; i++){
                if(cursor == nullptr) 
                    return dummy->next;
                cursor = cursor->next;
            }
            curr = after;
            prev = before;
            for(int i = 0; i < k; i++){
                nxt = curr->next;
                curr->next = prev;
                prev = curr;
                curr = nxt;
            }
            after->next = curr;
            before->next = prev;
            before = after;
            after = curr;
        }
    }
};
