import re
for i in range(int(input())):
    try:
        re.compile(input())
        print("True")
    except:
        print("False")
