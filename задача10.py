# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

def minimum_number_of_turns(sequence):
    emblem = 0
    tails = 0

    for coin in sequence:
        if coin == 'Г':
            emblem += 1
        else:
            tails += 1
    return min(emblem, tails)

sequence = input("Enter the sequence of coins (E - emblem, T - tails): ")
result = minimum_number_of_turns(sequence)
print(f"Minimum number of turns: {result}")

