import numpy

n, m = input().split()
a = []
for i in range(int(n)):
    my_array = input().split()
    a.append(my_array)
lis1 = numpy.array(a, int)
print(numpy.transpose(lis1))
print(lis1.flatten())
