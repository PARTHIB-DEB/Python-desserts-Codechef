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
    if min(freq.values())==max(freq.values()) :
        print(len(num_arr)-min(freq.values()))
    elif min(freq.values()) >=2:
        print(min(freq.values()))
    elif max(freq.values())>=2:
        for j in freq.keys():
            if freq[j]>min(freq.values()) and freq[j]>=2:
                print(freq[j])
                break
        
        