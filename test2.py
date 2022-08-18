# No. of pens
n = 3 

# Final config.
y = [500,300,200]
T = 1000

# Initial config
x = [0,0,0]

# Variance function
def var(x,y,n):
    c = [x[i]/y[i] for i in range(n)]
    s = 0
    su = 0
    for i in c:
        s+=i*i
        su+=i
    return (s/n) - (su/n)**2

# Updating x for every time t<T
for i in range(T+1):

    print("Time",i,"->",end=" ")
    for j in x:
        print(j,end=" ")
    print()

    c = 0  
    xc = list(x)
    xc[0]+=1
    s = var(xc,y,n)
    
    for i in range(n):
        xc = list(x)
        xc[i]+=1
        if var(xc,y,n)<s:
            c = i
            s = var(xc,y,n)
    x[c]+=1