import heapq

class MaxStack:
    class Node:
        __slots__ = ("val", "prev", "next", "alive", "id")
        def __init__(self, val, id_):
            self.val = val
            self.prev = None
            self.next = None
            self.alive = True
            self.id = id_

    def __init__(self):
        # DLL with head/tail sentinels
        self.head = self.Node(0, -1)
        self.tail = self.Node(0, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

        # Max-heap: (-val, -id, node)
        self.heap = []
        self.next_id = 0

    # ===== DLL helpers =====
    def _add_to_tail(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def _remove_node(self, node):
        # unlink from DLL and mark dead
        node.prev.next = node.next
        node.next.prev = node.prev
        node.alive = False

    def _clean_heap(self):
        # discard dead nodes at heap top
        while self.heap and not self.heap[0][2].alive:
            heapq.heappop(self.heap)

    # ===== API =====
    def push(self, x: int) -> None:
        node = self.Node(x, self.next_id)
        self.next_id += 1
        self._add_to_tail(node)
        heapq.heappush(self.heap, (-x, -node.id, node))  # O(log n)

    def pop(self) -> int:
        node = self.tail.prev              # O(1)
        self._remove_node(node)            # O(1)
        return node.val

    def top(self) -> int:
        return self.tail.prev.val          # O(1)

    def peekMax(self) -> int:
        self._clean_heap()                 # amortized O(log n) when needed
        return -self.heap[0][0]            # O(1) after cleanup

    def popMax(self) -> int:
        self._clean_heap()
        _, _, node = heapq.heappop(self.heap)  # O(log n)
        self._remove_node(node)                # O(1)
        return node.val

        
