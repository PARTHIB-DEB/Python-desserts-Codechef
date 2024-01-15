for _ in range(int(input())):
    odd_count_list = []
    for i in range(int(input())):
        item = int(input())
        if item in odd_count_list:
            odd_count_list.remove(item)
        else:
            odd_count_list.append(item)
    print(odd_count_list[0])
        