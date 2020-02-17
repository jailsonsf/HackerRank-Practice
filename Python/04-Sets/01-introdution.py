def average(array):
    heights = set(array)
    sumOfHeights = sum(heights)
    totalHeights = len(heights)

    return sumOfHeights / totalHeights


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)
