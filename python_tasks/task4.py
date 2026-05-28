"""
Задача 4. Объединение списков без дубликатов.

Порядок сохраняется:
сначала элементы первого списка, затем второго.
"""

n = int(input())
first = list(map(int, input().split())) if n > 0 else []

m = int(input())
second = list(map(int, input().split())) if m > 0 else []

seen = set()
result = []

for number in first + second:
    if number not in seen:
        result.append(number)
        seen.add(number)

print(*result)
