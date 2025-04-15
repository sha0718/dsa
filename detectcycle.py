class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Helper function to create a cycle in the linked list
def create_cycle(head, pos):
    if pos == -1:
        return head
    cycle_node = None
    current = head
    index = 0
    tail = None

    while current:
        if index == pos:
            cycle_node = current
        tail = current
        current = current.next
        index += 1

    if tail:
        tail.next = cycle_node
    return head

# Test case 1: No cycle
head1 = create_linked_list([3, 2, 0, -4])
print("Cycle Detected (no cycle):", has_cycle(head1))  # Output: False

# Test case 2: Create cycle at position 1 (node with value 2)
head2 = create_linked_list([3, 2, 0, -4])
head2 = create_cycle(head2, 1)
print("Cycle Detected (with cycle):", has_cycle(head2))  # Output: True
