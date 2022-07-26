class Node(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
            
            
class LL:
    
    def __init__(self):
        self.head = None
        self.numb = None
    
    def add(self, l):
        newlist = Node(l)
        if self.head is None:
            self.head = newlist
            return
        endlist = self.head
        while(endlist.next):
            endlist = endlist.next
        endlist.next = newlist
        
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        prev = self.numb
        return self.numb
        
    def sum(self):
        ptr = self.head
        sum = 0
        while (ptr != None):
            if sum == 0:
                sum += ptr.val
                ptr = ptr.next
            if sum < 10 and sum > 0:
                sum += (ptr.val*10)
                ptr = ptr.next
            else:
                sum += (ptr.val*100)
                ptr = ptr.next
        print(sum)
    
    def printLL(self):
        cur = self.head
        while(cur):
          print(cur.val)
          cur = cur.next


lis = LL()
lis.add(2)
lis.add(4)
lis.add(3)
lis.reverse()
lis.sum()
lis.printLL()