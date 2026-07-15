class Node:
    def __init__(self, key:int, value:int):
        self.key = key
        self.value = value
        self.prev = None
        self.nect = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _insert_to_head(self, node: Node) -> None:
        first = self.head.next
        
        self.head.next = node
        node.prev = self.head
        first.prev = node
        node.next = first
        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map[key]
        self._remove(node)
        self._insert_to_head(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._remove(node)
            self._insert_to_head(node)
            return

        if len(self.map) >= self.capacity:

            tail = self.tail.prev
            self._remove(tail)
            del self.map[tail.key]

        new_node = Node(key, value)
        self._insert_to_head(new_node)
        self.map[key] = new_node


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)