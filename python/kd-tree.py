from random import choices
import heapq

class Node:
    def __init__(self,i,data=None):
        self.ind = i  #index of splitting dimension
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self,k):
        self.k = k
        self.size = 1
        self.root = None
        self.bal = 0
        
    def insert(self,p,node=None):
        if not node: node=self.root
        if not self.root:
            self.root = Node(0,p);return
        if p[node.ind]<=node.data[node.ind]:
            if node.left: self.insert(p,node.left)
            else: node.left = Node((node.ind+1)%self.k,p)
        else:
            if node.right: self.insert(p,node.right)
            else: node.right = Node((node.ind+1)%self.k,p)

    @staticmethod
    def build(ps,ind=0):
        if not ps: return None
        k,sample_sz = len(ps[0]),60
        mid = sorted(choices(ps,k=sample_sz))[sample_sz//2][ind]

        left,right=[],[]
        for p in ps:
            if p[ind]<=mid: left.append(p)
            else: right.append(p)

        root = Node(left.pop())
        root.left = Tree.build(left,(ind+1)%k)
        root.right = Tree.build(right,(ind+1)%k)
        return root

    def traverse(self,root,dep=0,sp=""):
        if not root: print(sp,"-"*4);return
        print(sp,root.ind,root.data[root.ind],root.data)
        self.traverse(root.left,dep+1,sp+" "*4)
        self.traverse(root.right,dep+1,sp+" "*4)

    def _dist(self,a,b):     
        return sum((a[i]-b[i])**2 for i in range(self.k))

    def _kNN(self,node,p,k,ans):
        if not node: return ans
        if p[node.ind]<=node.data[node.ind]:
            self._kNN(node.left,p,k,ans)
        else:
            self._kNN(node.right,p,k,ans)

        heapq.heappush(ans,(-self._dist(node.data,p),node.data))
        if len(ans)>k:
            heapq.heappop(ans)

        biggest_dist = -ans[0][0]
        if (p[node.ind]-node.data[node.ind])**2>=biggest_dist:
            return ans

        if p[node.ind]<=node.data[node.ind]:        
            self._kNN(node.right,p,k,ans)
        else:
            self._kNN(node.left,p,k,ans)

        return ans

    def kNN(self,p,k=1):
        return self._kNN(self.root,p,k,[])


#------------------TEST & BENCHMARK----------------------------------------------------
from time import clock
import kdtree as kd
        
dist = lambda a,b:sum((a[i]-b[i])**2 for i in range(D))
def NN_test(tree,tr,ps,D,R,K=10):
    for i in range(10):
        p = tuple(choices(range(R),k=D))
        try:
            s = clock()
            a = tree.kNN(p,K)
            t = clock()
            c = tr.search_knn(p,K)
            y = clock()
            print(t-s,y-t,tree.bal)
            tree.bal = 0
            assert set(x[1] for x in a)==set(x[0].data for x in c)
        except Exception as e:
            print(set(x[1] for x in a),set(x[0].data for x in c))
            raise e

def gen_test_data(R,N,D):
    a = [choices(range(R),k=N) for i in range(D)]
    ps = list(zip(*a))
    #print(ps)

    s = clock()
    t = Tree(D)
    for p in ps:
        t.insert(p)
    ttt = clock()
    print("ME:",ttt-s)
    ttt = clock()
    tr = kd.create(ps)
    w = clock()
    print("GIT:",w-ttt)


R = int(10**9)
N = int(3*10**1)
D = 8

a = [choices(range(R),k=N) for i in range(D)]
ps = list(zip(*a))
    #print(ps)

s = clock()
t = Tree.build(ps)
ttt = clock()
print("ME:",ttt-s)
ttt = clock()
tr = kd.create(ps)
w = clock()
print("GIT:",w-ttt)

NN_test(t,tr,ps,D,R)

#print(t.bal,t.size)







