import sys
class Node:
   def __init__(self,data):
        self.data = data
        self.next=None

   def create(self,k):
        l = Node(k[0])
        p=l
        for i in range(1,len(k)):
            l.next=Node(k[i])
            l=l.next
        return p

def reverse(head):
    prev=None
    cur=head
    next=head.next
    while(next!=None):
        cur.next = prev
        prev=cur
        cur=next
        next=cur.next
    cur.next=prev
    return cur

def main():
    n = int(raw_input())
    k=[]
    for i in range(n):
        k.append(raw_input())
    l = Node(k[0])
    p=l
    head  = p
    for i in range(1,len(k)):
        l.next=Node(k[i])
        l=l.next
   
    while(p!=None):
        print(p.data)
        p=p.next
        

    p = reverse(head)
    while(p!=None):
       print(p.data)
       p=p.next

    #dprint(k)
main()
