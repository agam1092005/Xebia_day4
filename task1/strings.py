#Q3
s1 = input().strip()
s2 = input().strip()

s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

if len(s1) != len(s2):
    print("false")
else:
    freq = {}
    for i in s1:
        freq[i] = freq.get(i, 0) + 1
    for i in s2:
        if i not in freq:
            print("false")
            break
        freq[i] -= 1
        if freq[i] < 0:
            print("false")
            break
    else:
        print("true")

#Q4
s = input().strip()

my_set = set()
l = 0
max_len = 0

for r in range(len(s)):
    while s[r] in my_set:
        my_set.remove(s[l])
        l += 1
    my_set.add(s[r])
    max_len = max(max_len, r - l + 1)

print(max_len)