from re import A


finalconfig=[5,2,3]
t=10
# []=None,None,None
ans=[[None for i in range(len(finalconfig))]for j in range(t)]



for i in range(t):
    ptr=-1
    temp=[0]*len(finalconfig)
    tt=[0]*len(finalconfig)
    for j in range(len(finalconfig)):
        print(ans[i][j])



        # ptr+=1
        # p=j*i/t
        # pp=j*i//t
        # print(p,pp)
        # if int((p-pp)*10)==0:
        #     # print('hi1',i)
        #     temp[ptr]=pp
        # elif int((p-pp)*10)>=5:
        #     # print('hi2',i)
        #     temp[ptr]=pp+1
        # else:
        #     # print('hi3',i)
        #     temp[ptr]=pp
        # tt[ptr]=p


    # print(temp,sum(temp),i)
    # print(tt,i)
    

    # temp=[j*i/t for j in finalconfig]
    # print(temp)
    
    
