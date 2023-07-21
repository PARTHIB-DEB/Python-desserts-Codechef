for _ in range(int(input())):
    N=int(input())
    string=input()
    str_list=list(set(list(string)))
    s=""
    i=0
    while(i<=len(str_list)-1):
        s=s+str_list[i]
        i+=1
    print(s)
    # s=str_list[0]
    # for i in range(1,len(str_list)):
    #     if ord(str_list[i-1])<ord(str_list[i]):
    #         s=s+str_list[i-1]
    #     else:
    #         str_list[i-1],str_list[i]=str_list[i],str_list[i-1]
    #         s=s+str_list[i-1]
    # print(s)