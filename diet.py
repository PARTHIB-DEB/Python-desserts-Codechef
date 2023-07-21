for _ in range(int(input())):
    N,K=map(int,input().split())
    Protein=list(map(int,input().split()))
    count=0
    rem=0
    for i in range(0,len(Protein)):
        flag=1
        if Protein[i]+rem>=K:
            rem=Protein[i]-K
        else:
            flag=0
            count+=1
    if flag==1 and (len(Protein)-count)==0:
        print("YES")
    else:
        print(f"NO {count}")
    