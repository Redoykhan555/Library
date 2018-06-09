from random import randint

class Node:
    def __init__(self,v):
        self.v = v
        self.prev = None
        self.next = None
        self.down = None
        
    def add(self,v):
        """Add Node(v) next to self"""
        n = Node(v)
        n.next = self.next
        n.prev = self
        self.next = n
        if n.next: n.next.prev = n
        return n

    def __repr__(self):
        return str(self.v)

class SkipList:
    def __init__(self):
        self.size = 0
        self.height = 0
        self.root = None #head of topmost List

    def traverse(self,direc='next'):
        root = self.root
        while root:
            cur = root
            while cur:
                print(cur.v,end=' ')
                cur = getattr(cur,direc)
            print()
            root = root.down
                
    def insert(self,x):
        self.size += 1
        self.height += 1
        if self.root==None:
            self.root = Node(x)
            self.insert = self._insert
            return

    def _insert(self,x):
        self.size += 1
        ancestors = []
        height = self.height
        root = self.root
        while True:
            if x<root.v and root.prev:
                root = root.prev
            elif root.next and x>=root.next.v:
                root = root.next
            else:
                if root.down:  
                    ancestors.append(root)
                    root = root.down
                else:      #Level 0
                    if x>=root.v:
                        me = root.add(x)
                    else:
                        self.root = Node(x)
                        
                    break

        print(ancestors,me,self.root)
        while randint(0,1)==1: #Flip
            print("Flipped.")
            if ancestors:
                newme = ancestors.pop().add(x)
                newme.down = me
                me = newme
            else:
                print("Raising height")
                newme = Node(x)
                self.root = newme
                self.height += 1
                newme.down = me
                break


s = SkipList()

w = [5,7,1]
for a in w: s.insert(a)







