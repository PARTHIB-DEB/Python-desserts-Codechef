for _ in range(int(input())):
    my_string=list(input())
    l=my_string[1:]+my_string[:1]
    # print(l)
    r=my_string[:-1]+my_string[-1:]
    # print(r)
    if l==r:
        print("YES")
    else:
        print("NO")
    # print(my_string[1:])
    # print(my_string[:1])
    # print(my_string[-1:])
    # print(my_string[:-1])