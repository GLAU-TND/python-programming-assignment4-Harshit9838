#problem 3


a=input()
b=eval(input())
n= set()
for i in b :
    if a==i[0:len(a)]:
        n.add(i)
print(n)   
