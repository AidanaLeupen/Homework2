# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

S = int(input("Введите сумму S: "))
P = int(input("Введите произведение P: "))

found = False  # Флаг для обозначения, были ли найдены числа X и Y

for X in range(1, 1001):
    Y = S - X  # Вычисляем Y, основываясь на сумме
    if X * Y == P:  # Проверяем, является ли произведение равным P
        found = True
        print(f"Найдены числа: X = {X}, Y = {Y}")
        break

if not found:
    print("Числа X и Y не найдены.")