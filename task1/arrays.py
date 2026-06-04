#Q1
arr = list(map(int, input().split()))
first = second = float('-inf')

for i in arr:
    if i > first:
        second = first
        first = i
    elif i != first and i > second:
        second = i

print(second if second != float('-inf') else -1)

#Q2
arr = list(map(int, input().split()))
k = int(input())

n = len(arr)
k = k % n  

def reverse(l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

reverse(0, n - 1)
reverse(0, k - 1)
reverse(k, n - 1)
print(arr)