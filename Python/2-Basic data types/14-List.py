n = int(input())
l = []

for i in range(n):
    x = input().split(" ")
    #opr = x[0]
    opr = ' '
    if opr == "insert":
        l.insert(int(x[1]), int(x[2]))
    if opr == "print":
        print(l)
    if opr == "remove":
        l.remove(int(x[1]))
    if opr == "append":
        l.append(int(x[1]))
    if opr == "sort":
        l.sort()
    if opr == "pop":
        if len(l) != 0:
            l.pop()
    if opr == "reverse":
        l.reverse()
