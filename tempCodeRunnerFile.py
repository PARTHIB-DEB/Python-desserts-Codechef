l=my_string[1:]+my_string[:1]
    print(l)
    r=my_string[:-1]+my_string[-1:]
    print(l)
    if l==r:
        print("YES")
    else:
        print("NO")