# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

S = int(input("Enter the sum S: "))
P = int(input("Enter the product P: "))

found = False

for X in range(1, 1001):
    Y = S - X
    if X * Y == P:
        found = True
        print(f"Numbers found: X = {X}, Y = {Y}")
        break

if not found:
    print("Numbers X and Y are not found.")

