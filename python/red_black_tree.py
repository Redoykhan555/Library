class Node:
    __slots__ = ['col','v','left','right','par','size']
    def __init__(self,v,col,par):
        self.col = col 
        self.v = v
        self.left = None 
        self.right = None
        self.par = par
        self.size = 1

    def update_size(s):
        s.size = getattr(s.left,'size',0)+getattr(s.right,'size',0)+1

    def __repr__(self):
        x = "root" if self.par==None else str(self.par.v)
        return str(self.v)+" "+self.col+" "+x+" "+str(self.size)

class Tree:
    def __init__(self):
        self.root = None

    def _insert(self,v,root):
        while True:
            root.size += 1
            if v<root.v:
                if root.left: root = root.left
                else : root.left = Node(v,'r',root);return root.left
            else:
                if root.right : root = root.right
                else :root.right = Node(v,'r',root);return root.right

    def _rotate_left(self,X):
        right = X.right
        X.right = right.left
        if right.left: right.left.par = X
        right.left = X
        right.par = X.par
        X.par = right

        X.update_size();right.update_size()
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

        X.update_size();left.update_size()
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
        if self.root==None:
            self.root = Node(v,'b',None)
        self.insert = lambda v:self._repair(self._insert(v,self.root))

    def _bound(self,v,root,func):
        if root==None: return None
        if func(v,root.v):
            return self._bound(v,root.left,func) or root
        else:
            return self._bound(v,root.right,func)

    def upper_bound(self,v):
        return self._bound(v,self.root,lambda v,nv:v<nv)

    def lower_bound(self,v):
        return self._bound(v,self.root,lambda v,nv:v<=nv)

    def bigger(self,v,root): #No of elements bigger than v in tree
        ans = 0
        while root:
            if v<root.v:
                ans += getattr(root.right,'size',0)+1
                root = root.left
            else: root = root.right
        return ans    


#--------Test & Benchmark----------------------------------------
from random import choices
from time import clock


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

def postorder(root):
    if root==None: return 0
    a = postorder(root.left)
    b = postorder(root.right)
    return max(a,b)+1

def pprint(root,sp=""):
    if not root: print(sp,"-"*6);return
    print(sp,root)
    pprint(root.left,sp+" "*6)
    pprint(root.right,sp+" "*6)

def sorting_test(t):
    x = traverse(t.root,[])
    assert x==sorted(li)

def size_test(root):
    if root==None: return 0
    a = size_test(root.left)
    b = size_test(root.right)
    assert root.size==a+b+1
    return a+b+1

def bound_test(t,R=10**3+100):
    v = choices(range(R),k=1)[0]
    n = t.upper_bound(v)
    if not n:
        print("None:",v,max(traverse(t.root,[])));return
    print(v,n.v)
    assert n.v == min(filter(lambda x:x>v,traverse(t.root,[])))

def build(N,R):
    li = choices(range(R),k=N)
    t = Tree()
    for k in li:
        t.insert(k)
    return t,li

s = clock()
t,li = build(10**5,10**8)
w = clock()
print(w-s)
bound_test(t)

sorting_test(t)
size_test(t.root)
depth = postorder(t.root)
print("Depth:",depth)

