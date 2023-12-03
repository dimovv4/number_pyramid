n = int(input())
counter = 1
for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(counter, end = ' ')
        counter += 1
        if counter > n:
            break
    if counter > n:
        break
    print()
