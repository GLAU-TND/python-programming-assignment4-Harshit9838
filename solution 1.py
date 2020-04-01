#problem 1


h=eval(input())
k=int(input())
new=[]
for i in h:
    if i[0] not in new:
        new.append(i[0])
p={}
for i in new:
    p[i]=[]
for i in p:
    for j in h:
        if i==j[0]:
            p[i].append(j[1])
dct={}
s=0
for i in range (len(p)):
    for j in range (i+1,len(p)):
        r=len(set(p[list(p)[i]]) & set(p[list(p)[j]]))/float(len(set(p[list(p)[i]])| set(p[list(p)[j]])))*100
        if(i!=j):
            dct[s]=[round(r,2),list(p)[j],list(p)[i]]
            s=s+1
a=list(dct.values())
for n in range (len(a)):
        if a[n][1]>a[k][2] :
            c=a[k][1]
            a[n][1]=a[k][2]
            a[n][2]=c
a.sort(key=lambda a:a[0],reverse=True)
l=[]
for e in range (n):
    h+=[(a[e][1],a[e][2])]
print(h)                                              

