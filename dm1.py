#!/usr/bin/python
import scipy.sparse
import scipy.sparse.csgraph
import scipy.sparse.linalg
filename = "facebook_combined.txt"
N=4039
adj = scipy.sparse.dok_matrix((N,N));
print(adj)
f=open(filename)
for l in f.readlines():
    x,y=tuple(l.split(' '))
    a,b=int(x),int(y)
    adj[a,b]=1
    adj[b,a]=1
lapl = scipy.sparse.csgraph.laplacian(adj)
eigenvals,eigenvects = scipy.sparse.linalg.eigsh(lapl.tocsc(),k=2,which='LM',sigma=0)
s=[]
for i in range(N):
    if(eigenvects[i][1]<0):
        s.append(-1)
    else:
        s.append(1)
print s
print 'Community 1 :'
n=0
for i in range (N):
    if(s[i]==-1):
        n=n+1
        print i
print 'Total Community 1 : '+str(n)
print 'Community 2 :'
n=0
for i in range(N):
    if(s[i]==1):
        print i
        n=n+1
print 'Total Community 2 : '+str(n)
##Connectivity
I,J,_ = scipy.sparse.find(adj)
connectivity = 0
for i in range(len(I)):
    if(s[I[i]]!=s[J[i]]):
        connectivity=connectivity+1
connectivity=connectivity/2
print 'Connectivity of the graph : '+str(connectivity)
