for _ in range(int(input())):
    flag=0
    name_length=int(input())
    snake_name=input()
    check=snake_name.split(".")
    print(check)
    for i in range(0,len(check)):
        if check[0]=="" or check[0]=="" or check[len(check)-1]=="T":
            if check[i]=="H":
                for j in range(i,len(check)):
                    if check[j]=="H":
                        flag=1
                        break
            elif check[i]=="THT":
                flag=1
                break
        else:
            flag=1
            break
    if flag==1:
        print("INVALID")
    else:
        print("VALID")