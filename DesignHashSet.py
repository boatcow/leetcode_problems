# 705. Design HashSet

# https://leetcode.com/problems/design-hashset/

# Create a HashSet that stores numbers.

# Create an Array with big size 10**4 for instance , we can store a number at number%10**4 position
# but ofcourse if someone wants to store 1,10001 in this case 1%10**4 == 10001*10**4 , so we need to handle collisions
# to handle collisions we use a Linked List and add it to that.

class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

class MyHashSet:

    def __init__(self):
        self.arr=[ListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        index=key%len(self.arr)
        curr=self.arr[index]
        while curr.next:
            if curr.next.val==key:
                return
            curr=curr.next
        curr.next=ListNode(key)

    def remove(self, key: int) -> None:
        index=key%len(self.arr)
        curr=self.arr[index]
        while curr.next:
            if curr.next.val==key:
                curr.next=curr.next.next
                return
            curr=curr.next
       
    def contains(self, key: int) -> bool:
        index=key%len(self.arr)
        curr=self.arr[index]
        while curr.next:
            if curr.next.val==key:
                return True 
            curr=curr.next
        return False     
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)