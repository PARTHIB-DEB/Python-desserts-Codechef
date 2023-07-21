for _ in range(int(input(" "))):
    N=int(input())
    B_list=list(map(int,input().split(" ")))
    # print(B_list)
    if B_list.count(1)==B_list.count(0):
        print("YES")
    else:
        print("NO")