for _ in range(int(input())):
    N,K,S=map(int,input().split(" "))
    length=N+K-1
    # Distinct array = [1,3,5,......]
    array_list=[i for i in range(1,2*N,1) if i%2!=0]
    for i in range(0,len(array_list)):
        sum=0
        temp=array_list[0]
        odd_sum=S-K*array_list[0]
        array_list.remove(array_list[0])
        for j in array_list:
            sum=sum+j
        if odd_sum == sum:
            print(temp)
            break