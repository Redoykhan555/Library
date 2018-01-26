from random import choices
import heapq

class Node:
    __slots__ = ['ind','left','right','data']
    def __init__(self,data,i):
        self.ind = i  #index of splitting dimension
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self,k=0,ps=None,dist_func=None):
        if ps:
            self.k = len(ps[0])
            self.size = len(ps)
            self.root = self.build(ps,0)
            ps.append(self.root.data)
        else:         
            self.k = k
            self.size = 0
            self.root = None
        if dist_func: self._dist = dist_func
        else:
            self._dist = lambda a,b:sum((a[i]-b[i])**2 for i in range(self.k))
        
    def insert(self,p,node=None):
        if not self.root:
            self.root = Node(p,0)
            self.size = 1
            return
        
        if not node:
            node=self.root
            self.size += 1

        if p[node.ind]<=node.data[node.ind]:
            if node.left: self.insert(p,node.left)
            else: node.left = Node(p,(node.ind+1)%self.k)

        else:
            if node.right: self.insert(p,node.right)
            else: node.right = Node(p,(node.ind+1)%self.k)

    def build(self,ps,ind):
        if not ps: return None
        mid = ps.pop()
        
        left,right=[],[]
        for p in ps:
            if p[ind]<=mid[ind]: left.append(p)
            else: right.append(p)

        root = Node(mid,ind)
        root.left = self.build(left,(ind+1)%self.k)
        root.right = self.build(right,(ind+1)%self.k)
        return root

    def traverse(self,root,dep=0,sp=""):
        if not root: print(sp,"-"*6);return
        print(sp,root.ind,root.data)
        self.traverse(root.left,dep+1,sp+" "*6)
        self.traverse(root.right,dep+1,sp+" "*6)

    def _kNN(self,node,p,k,ans):
        if not node: return
        #print(node.ind,node.data,ans)
        if p[node.ind]<=node.data[node.ind]:
            self._kNN(node.left,p,k,ans)
        else:
            self._kNN(node.right,p,k,ans)

        heapq.heappush(ans,(-self._dist(node.data,p),node.data))
        if len(ans)>k:
            heapq.heappop(ans)

        biggest_dist = -ans[0][0]
        if (p[node.ind]-node.data[node.ind])**2>=biggest_dist:
            if len(ans)>=k: return ans

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
import matplotlib.pyplot as plt
        
dist = lambda a,b:sum((a[i]-b[i])**2 for i in range(D))
def NN_test(tree,tr,ps,D,R,K=2):
    ee,rr = [],[]
    for i in range(20):
        p = tuple(choices(range(R),k=D))
        try:
            s = clock()
            a = tree.kNN(p,K)
            t = clock()
            c = tr.search_knn(p,K)
            y = clock()
            print(t-s,y-t)
            ee.append(t-s);rr.append(y-t)
            tree.bal = 0
            assert set(x[1] for x in a)==set(x[0].data for x in c)
        except Exception as e:
            print(set((x[1],-x[0]) for x in a),
                  set((x[0].data,x[1]) for x in c))
            raise e
    return ee,rr

R = int(10**9)
def gen_test_data(N,D):
    global R
    a = [choices(range(R),k=N) for i in range(D)]
    ps = list(zip(*a))

    print("starting...")
    s = clock()
    t = Tree(ps=ps)
    #t.traverse(t.root)
    ttt = clock()
    print("ME:",ttt-s)
    ttt = clock()
    tr = kd.create(ps)
    w = clock()
    print("GIT:",w-ttt)
    a,b = NN_test(t,tr,ps,D,R)
    return a,b



N = int(1*10**5)
D = 12

ds = [3,6,10,20]

for i,d in enumerate(ds):
    a,b = gen_test_data(N,d)
    plt.subplot(4,1,i+1)
    plt.plot(range(20),a,label='mee')
    plt.plot(range(20),b,label='git')
    plt.legend()
    plt.title(str(d)+" dims")

plt.tight_layout(pad=0.7, w_pad=0.25, h_pad=1.5)
plt.show()
#print(t.bal,t.size)

























