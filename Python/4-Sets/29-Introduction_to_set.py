def average(array):
    # your code goes here
    result = sum(set(array))/len(set(array))
    return result


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
