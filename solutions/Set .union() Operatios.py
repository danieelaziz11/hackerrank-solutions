n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

result = english.union(french)

print(len(result))