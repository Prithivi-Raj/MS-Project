# No. of pens
n = 5

# Final config.
y = [16,1,1,1,1]
T = 20

# Initial config
x = [0]*n

# anss=[0, 1, 2, 0, 1, 0, 0, 2, 1, 0, 0]

# Variance function
def var(x,y,n):
    c = [x[i]/y[i] for i in range(n)]
    s = 0
    su = 0
    for i in c:
        s+=i*i
        su+=i
    return (s/n) - (su/n)**2


ress=[]
minvar=0
prvad=0
prv=0
# Updating x for every time t<T
for i in range(1,T+2):
    ideal=[cc*i/(T) for cc in y]

    print("Time",i-1,"->",end=" ")
    
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
        # print(var(xc,y,n),"indvar")
        if var(xc,y,n)<s:
            c = i
            
            s = var(xc,y,n)
    minvar+=s
    print(s)
    x[c]+=1
    for i in range(len(x)):
        prv+=(x[i]-ideal[i])**2
        prvad+=(x[i]/y[i]-ideal[i]/y[i])**2
    ress.append(c)

print(ress)
print(minvar)
print(prv)
print(prvad)
# print(ress==anss*100)