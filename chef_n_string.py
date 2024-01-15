for _ in range(int(input())):
    friends=list(input())
    p=0
    i=1
    while(i<=len(friends)-1):
        if friends[i-1]!=friends[i]:
            p+=1
            i+=2
        else:
            i+=1
    print(p)
            

            
        
    
    