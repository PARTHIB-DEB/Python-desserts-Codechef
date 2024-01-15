# cook your dish here
for _ in range (int(input())):
    n,k=map(int,input().split())
    weights=list(map(int,input().split()))
    min_no_items = min(k,(n-k))
    son_bag=0
    i=1
    while i<=min_no_items:
        item=min(weights)
        son_bag+=item
        weights.remove(item)
        i+=1
    parent_bag=sum(weights)
    print(parent_bag-son_bag)