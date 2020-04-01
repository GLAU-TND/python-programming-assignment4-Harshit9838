#problem 2


j=eval(input())
def file(a):
    try:
        for n in a:
            if type(a[n])==type({}):
                for i in a[n]:
                    a[n+i]=a[n][i]
                s.pop(n)
                file(a)
        else:
            print(a)
    except RuntimeError:
         pass
         
            
file(i)

