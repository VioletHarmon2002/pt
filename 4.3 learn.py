#WRIte a program that asks the user to enter numbers until they enter an empty string to quit.
#Finally, the program prints out the smallest and largest number from the numbers it received.
# Инициализация переменных для минимального и максимального числа
min_number = None
max_number = None

while True:
    try:
        number = input("Syöttäkää satunnainen numero (пустая строка для завершения): ")

        # Проверка на пустую строку (завершение программы)
        if number == "":
            break

        number = int(number)

        # Если это первое число, инициализируем min и max
        if min_number is None or max_number is None:
            min_number = number
            max_number = number
        else:
            # Обновляем min и max
            if number < min_number:
                min_number = number
            if number > max_number:
                max_number = number

    except ValueError:
        print("Ошибка: Некорректный ввод. Пожалуйста, введите число.")

if min_number is not None and max_number is not None:
    print(f"Наименьшее число: {min_number}")
    print(f"Наибольшее число: {max_number}")
else:
    print("Вы не ввели ни одного числа.")








