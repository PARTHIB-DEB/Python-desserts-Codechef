import re
for _ in range(int(input())):
    f=input()
    sub=f[0:2]
    if re.match(sub,f):
        print(f"matched at {}")
    