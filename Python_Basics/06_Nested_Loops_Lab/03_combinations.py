combinations_count = 0

n = int(input())

for x1 in range(n+1):
    for x2 in range(n+1):
        for x3 in range(n+1):
            if x1 + x2 + x3 == n:
                combinations_count += 1
print(combinations_count)
