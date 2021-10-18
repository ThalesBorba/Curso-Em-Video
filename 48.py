n = 0
for c in range(1, 501):
    if not c % 2 == 0 and c % 3 == 0:
        n = n + c
print(n)
