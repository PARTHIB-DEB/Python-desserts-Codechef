# cook your dish here
sticks,max_diff=map(int,input().split())
sticks_arr=[]
for i in range(sticks):
    item=int(input())
    sticks_arr.append(item)
p=0
i=1
while(i<=len(sticks_arr)-1):
    if sticks_arr[i-1]-sticks_arr[i]<=max_diff:
        p+=1
        i+=2
    else:
        i+=1
print(p)
        
            

            
        
    
    