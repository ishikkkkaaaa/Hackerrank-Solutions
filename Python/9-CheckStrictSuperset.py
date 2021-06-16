""" 
if lengths =! of subset n super then not strict superset

  """

l = set(map(int, input().split()))
# no. of test cases
n = int(input())
val = "True"
for i in range(n):
    # store the set of elements
    l1 = set(map(int, input().split()))

    # if len of l and l1 is same or not
    if len(l1.difference(l)) == 0:
        val = "True"
    else:
        val = "False"
        break
print(val)
