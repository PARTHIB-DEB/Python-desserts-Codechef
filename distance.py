# cook your dish here
for _ in range(int(input())):
    R=int(input())
    for i in range(1,4):
        X,Y=map(int,input().split())
        if X+Y>R:
            print("no")
            break
    else:
        print("yes")