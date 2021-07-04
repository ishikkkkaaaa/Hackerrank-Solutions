from collections import namedtuple

n = int(input())
head = input().split()

title = namedtuple("title", head)
sum = 0

for i in range(n):
    sum += int(title(*input().split()).MARKS)
print(sum/n)
