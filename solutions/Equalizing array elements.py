#
# Complete the 'minOperations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER threshold
#  3. INTEGER d
#
def minOperations(arr, threshold, d):
    costs = {}

    for num in arr:
        x = num
        operations = 0

        while True:
            if x not in costs:
                costs[x] = []

            costs[x].append(operations)

            if x == 0:
                break

            x //= d
            operations += 1

    answer = float('inf')

    for x in costs:
        if len(costs[x]) >= threshold:
            costs[x].sort()
            answer = min(answer, sum(costs[x][:threshold]))

    return answer


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    threshold = int(input().strip())

    d = int(input().strip())

    result = minOperations(arr, threshold, d)
    
    print (result)


