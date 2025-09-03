# Linked lists


## 141. Linked list cycle

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

 

### Approach 1: Using slow and fast pointers

If we select any given node, we can try to find out whether there is a cycle by moving a pointer until we either reach the end of the list or come back to the selected node, but there might also be a cycle after the selected node, which will result in an infinite loop.

The infinite loop issue can be resolved by using a slow and a fast pointer. The slow pointer makes a move of one node at each iteration while the fast pointer makes a move of two. If there is any cycle in the list, both the slow and fast pointers will end up within it. At this point, the fast pointer, moving twice as fast as the slow one, will inevitably come back to the same value as the slow one. We can detect this equality to determine there is a cycle. If the fast pointers reaches the end of the list, it means that there is no cycle.

The time complexity is O(n), because it takes at most n iterations for the slow pointer to get in the cycle, and also at most n iterations for the fast pointer to join the slow pointer. 



![141_1](README.assets/141_1_.png)



```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                return True

        return False
```

Time: O(n) - Space: O(1)



## 2. Add two numbers

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



**Example:**

- Input: `l1 = [2,4,3]`, ` l2 = [5,6,4]`
- Output: `[7,0,8]`



### Approach 1: Build the result by computing digit and carry iteratively

Move a pointer along the list iteratively.

As long as one of the list contains a digit:

- compute the value
- deduce the digit and carry
- add a new node to the result

If `l1` and `l2`  reached the end but the carry is not zero, we should add a final node with its value.



![2_1](README.assets/2_1_.png)



```python
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        preres = ListNode(0)
        curres = preres
        carry = 0

        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry = val // 10
            digit = val % 10

            curres.next = ListNode(digit)
            curres = curres.next

        return preres.next
```

Time: O(n) - Space: O(n)
