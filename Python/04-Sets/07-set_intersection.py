n = int(input())
english = set(map(int, input().split()))

b = int(input())
french = set(map(int, input().split()))

intersection = english & french

print(len(intersection))
