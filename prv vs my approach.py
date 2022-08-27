finalcofig=[5,3,2]
initialconfig=[0,0,0]
# a=[1, 1, 1, 1, 1, 2, 2, 2 ,3 ,3]
t=10
a=[1 ,2 ,3 ,1, 1, 2, 1, 3 ,2 ,1]
aa=[1,1,1,3,1,1,1,1,2,1,1,5,1,1,1,4,1,1,1,1]
print(len(aa))

# init=[0,0,0]
prv=0
for i in range(1,t+1):
    if a[i-1]==1:
        initialconfig[0]+=1
    elif a[i-1]==2:
        initialconfig[1]+=1
    else:
        initialconfig[2]+=1

    ideal=[i*c/t for c in finalcofig]
    print(ideal)
    print(initialconfig)

    for j in range(len(ideal)):
        prv+=(ideal[j]-initialconfig[j])**2

print(prv)




