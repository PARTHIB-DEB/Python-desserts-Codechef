# cook your dish here
for _ in range(int(input())):
    n=int(input())
    num_arr=list(map(int,input().split()))
    freq={}
    count = 1
    for i in num_arr:
        if i not in freq.keys():
            count = 1
        else:
            count = freq.get(i) + 1
        freq[i]=count
    # print(freq)
    # if min(freq.values())==max(freq.values()):
    #     if(len(freq.keys()))==1:
    #         print("yes")
    #     else:
    #         print("no")
    # else:
    #     for j in freq.keys():
    #         if freq[j]==max(freq.values()):
    #             print("yes")
    #             break
    if list(freq.values()).count(max(freq.values()))==1:
        print("yes")
    else:
        print("no")
        