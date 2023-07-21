for _ in range(int(input())):
    N,P,X,Y=map(int,input().split(" "))
    position_list=input().split(" ")
    # for i in range(len(position_list)):
    #     position_list[i]=int(position_list[i])
    # print(position_list[P-1])
    if position_list[P-1]==0:
        print(P+X)
        break
    elif position_list[P-1]==1:
        print(P+Y)
        break