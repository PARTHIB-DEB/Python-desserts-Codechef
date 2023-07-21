# length=int(input())
# my_str=input()
# my_list=[]
# for i in my_str:
#     my_list.append(i)
# # print(my_list)
# if length%2==0:
#     # n/2 times run
#     i=0
#     while(i<=length//2):
#         my_list[i],my_list[i+1] = my_list[i+1],my_list[i]
#         i+=2
#     print(my_list)

    
# else:
#     # n-1 times run
#     i=0
#     while(i<length-1):
#         my_list[i],my_list[i+1] = my_list[i+1],my_list[i]
#         i+=2
#     print(my_list)
# diff=25
# for i in range(0,len(my_list)):
#     code=ord(my_list[i])
#     if code<=122:
#         code-=diff
#         ord(my_list[i])=code
#         diff-=2
#     elif code>=97:
#         code+=diff
#         ord(my_list[i])=code
#         diff-=2
# print(my_list)

A=int(input())
B=int(input())
C=input()
if C=="+":
    print(A+B)
elif C=="-":
    print(A-B)
elif C=="*":
    print(A*B)
elif C=="/":
    print(A/B)