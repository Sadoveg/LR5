"""
Задача 5. Длина неубывающего фрагмента.

Найти максимальную длину подряд идущего неубывающего подотрезка.
"""

n = int(input())

if n == 0:
    print(0)
else:
    numbers = list(map(int, input().split()))
    best = 1
    current = 1

    for i in range(1, n):
        if numbers[i] >= numbers[i - 1]:
            current += 1
        else:
            best = max(best, current)
            current = 1

    best = max(best, current)
    print(best)
