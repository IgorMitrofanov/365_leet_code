""""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tail = head
        indexes = dict()
        pos = 0
        while tail:
            if tail in indexes:
                return True
            indexes[tail] = pos
            pos +=1
            tail = tail.next
        return False
    

def build_linked_list(values, pos):
    """
    values: List[int] — значения узлов
    pos: int — индекс узла, куда указывает tail.next (или -1 если цикла нет)
    returns: ListNode | None
    """
    if not values:
        return None

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]

# ---------- TESTS ----------

sol = Solution()

hasCycle = sol.hasCycle

# 0) empty list
head = build_linked_list([], -1)
assert hasCycle(head) is False

# 1) single node, no cycle
head = build_linked_list([1], -1)
assert hasCycle(head) is False

# 2) single node, self-cycle
head = build_linked_list([1], 0)
assert hasCycle(head) is True

# 3) two nodes, no cycle
head = build_linked_list([1, 2], -1)
assert hasCycle(head) is False

# 4) two nodes, tail connects to head (pos=0)
head = build_linked_list([1, 2], 0)
assert hasCycle(head) is True

# 5) example 1: [3,2,0,-4], pos=1 => True
head = build_linked_list([3, 2, 0, -4], 1)
assert hasCycle(head) is True

# 6) cycle to middle (tail connects to index 2)
head = build_linked_list([10, 20, 30, 40, 50], 2)
assert hasCycle(head) is True

# 7) no cycle, multiple nodes
head = build_linked_list([10, 20, 30, 40, 50], -1)
assert hasCycle(head) is False

# 8) values with negatives and large absolute values, no cycle
head = build_linked_list([-10**5, 0, 10**5], -1)
assert hasCycle(head) is False

# 9) cycle where tail connects to itself (last index)
head = build_linked_list([7, 8, 9], 2)
assert hasCycle(head) is True

head = build_linked_list([-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5], -1)
assert hasCycle(head) is False

print("All asserts passed.")