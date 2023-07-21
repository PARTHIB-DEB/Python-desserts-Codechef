for _ in range(int(input())):
    N=int(input())
    doll=list()
    for i in range(0,N):
        doll.insert(i,int(input()))
    for j in doll:
        if doll.count(j)==1:
            print(j)
            break