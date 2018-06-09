import random

class Node:
    def __init__(self,v,col,par):
        self.col = col 
        self.v = v
        self.left = None 
        self.right = None
        self.par = par

    def __repr__(self):
        x = "root" if self.par==None else str(self.par.v)
        return str(self.v)+" "+self.col+" "+x

class Tree:
    def __init__(self):
        self.root = None

    def _insert(self,v,root):
        if v<root.v:
            if root.left: return self._insert(v,root.left)
            else : root.left = Node(v,'r',root);return root.left
        else:
            if root.right : return self._insert(v,root.right)
            else :root.right = Node(v,'r',root);return root.right

    def _rotate_left(self,X):
        right = X.right
        X.right = right.left
        if right.left: right.left.par = X
        right.left = X
        right.par = X.par
        X.par = right
        if right.par==None: return
        if right.par.right==X: right.par.right = right
        else: right.par.left = right

    def _rotate_right(self,X):
        left = X.left
        X.left = left.right
        if left.right: left.right.par = X
        left.right = X
        left.par = X.par
        X.par = left
        if left.par==None: return
        if left.par.left==X: left.par.left = left
        else: left.par.right = left

    def _repair(self,N):
        if N.par==None: N.col = 'b';return #root
        if N.par.col=='b':return 
        P = N.par
        G = P.par
        U = G.left if G.right==P else G.right
        if U and U.col=='r':
            P.col = 'b'
            U.col = 'b'
            G.col = 'r'
            return self._repair(G)

        if G.left and N==G.left.right:
            self._rotate_left(P)
            N = N.left
            
        elif G.right and N==G.right.left:
            self._rotate_right(P)
            N = N.right
           
        P = N.par
        G = P.par
        if N==P.left:
            self._rotate_right(G)
        else:
            self._rotate_left(G)

        P.col = 'b'
        if P.par==None: self.root=P
        G.col = 'r'  

    def insert(self,v):
        #print("ins:",v)
        if self.root==None:
            self.root = Node(v,'b',None)
            N = self.root
        else:
            N = self._insert(v,self.root)


        self._repair(N)


#--------Test-----------------------------------------

def traverse(root,li):
    if root==None: return
    traverse(root.left,li)
    li.append(root.v)
    traverse(root.right,li)
    return li

def inorder(root):
    if root==None: return
    inorder(root.left)
    print(root)
    inorder(root.right)

def preorder(root):
    if root==None: return
    print(root)
    preorder(root.left)
    preorder(root.right)

def test(n):
    li = [random.randint(1,100) for i in range(n)]
    t = Tree()
    for k in li:
        t.insert(k)
    x = traverse(t.root,[])
    assert x==sorted(li)

"""N=20
li = [random.randint(1,100) for i in range(N)]
li=[96, 95, 69, 35, 84, 83, 73, 4, 55, 25, 77, 51, 94, 41, 54, 69, 72, 5, 7, 78]
t = Tree()
for k in li:
    t.insert(k)
    print("\n\n")
"""
test(80000)







        

    
