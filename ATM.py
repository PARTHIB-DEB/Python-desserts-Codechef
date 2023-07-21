for i in range(int(input())):
    N,K=map(int,input().split())
    withdraw_list=input().split()
    print(withdraw_list)
    s=""
    for j in range(0,len(withdraw_list)):
        if int(withdraw_list[j])>=K:
            s+=str(1)
        else:
            s+=str(0)
        K-=int(withdraw_list[j])
    print(s)