marks = []
marksheet = []
n = int(input())

for i in range(n):
    name = input()
    score = float(input())
    marks += [score]
    marksheet += [[name, score]]
second_lowest = sorted(set(marks))[1]

for i, j in sorted(marksheet):
    if j == second_lowest:
        print(i)
