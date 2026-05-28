"""
Задача 1. Сумма и среднее для смешанных значений.

Ввод:
n
n токенов: целые, вещественные числа, True/False

Вывод:
сумма и среднее. Среднее с точностью до 6 знаков.
"""

def parse_value(token):
    if token == "True":
        return 1
    if token == "False":
        return 0
    if "." in token:
        return float(token)
    return int(token)


n = int(input())
tokens = input().split()

values = [parse_value(token) for token in tokens[:n]]
total = sum(values)
average = total / n

print(total, f"{average:.6f}")
