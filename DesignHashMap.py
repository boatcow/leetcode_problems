# 706. Design HashMap

# https://leetcode.com/problems/design-hashmap/

# Create a HashMap that stores key as a Number and value as a Number.

# Similar to Design HashSet problem 

# Create an Array with big size 10**4 for instance , we can store a number at number%10**4 position
# but ofcourse if someone wants to store 1,10001 in this case 1%10**4 == 10001*10**4 , so we need to handle collisions
# to handle collisions and to know what key maps to what value , we store key and value in the LinkedList.

class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key  # We also store Key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for i in range(1000)]
        
    def hashcode(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hashcode(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)
         
    def get(self, key: int) -> int:
        cur = self.map[self.hashcode(key)].next
        while cur and cur.key != key:
            cur = cur.next
        if cur:
            return cur.val
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self.hashcode(key)]
        while cur.next and cur.next.key != key:
            cur = cur.next
        if cur and cur.next:
            cur.next = cur.next.next
