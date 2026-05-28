"""
Задача 2. Форматирование ФИО.

Функция возвращает:
- "Фамилия И.О.", если отчество указано;
- "Фамилия Имя", если отчества нет.
"""

def format_name(last, first, middle=None):
    if middle is None:
        return f"{last} {first}"
    return f"{last} {first[0]}.{middle[0]}."


m = int(input())

for _ in range(m):
    parts = input().split()
    if len(parts) == 2:
        print(format_name(parts[0], parts[1]))
    else:
        print(format_name(parts[0], parts[1], parts[2]))
