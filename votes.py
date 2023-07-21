for _ in range(int(input())):
    N,K=map(int,input().split(" "))
    vote=list(map(int,input().split(" ")))
    dump=0
    count=0
    for i,j in enumerate(vote):
        if i+1 != j and dump!=j:
            count+=1
    print(count)
    # if count==K:
    #     print("1")
    # else:
    #     print("0")