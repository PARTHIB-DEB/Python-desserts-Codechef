# cook your dish here
for _ in range(int(input())):
    n=int(input())
    num_arr=list(map(int,input().split()))
    num_arr=list(set(num_arr))
    if len(num_arr)==1:
        print("YES")
    elif len(num_arr)==2 :
        if abs(num_arr[0]-num_arr[1])<=1:
            print("YES")
        else:
            print("NO")
    else:
        for i in range(len(num_arr)):
            if (((num_arr[i]-1) not in num_arr) and ((num_arr[i]+1) not in num_arr)):
                print("NO")
                break
        else:
            print("YES")
                