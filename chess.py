# 1) ход ладьи
# 2) ход слона
# 3) ход коня

# ***********************************************************************************************************************
################## *** Вариант 1 *** ##################
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")
print("\n" + "Программа завершена!")

################## *** Вариант 1 *** ##################
def rook_move(start, end):
    # Функция для валидации позиции
    def is_valid_position(position):
        return len(position) == 2 and 'a' <= position[0] <= 'h' and 1 <= int(position[1]) <= 8

    try:
        # Получение столбца и строки из позиций
        start_column = start[0]
        start_row = int(start[1])
        end_column = end[0]
        end_row = int(end[1])

        # Проверка на валидность позиций
        if not is_valid_position(start) or not is_valid_position(end):
            return "Позиции выходят за пределы доски 8x8"

        # Проверка на возможность хода ладьи
        if start_column == end_column or start_row == end_row:
            return f"Ладья может совершить ход с {start_column}{start_row} на {end_column}{end_row}"
        else:
            return f"Ладья не может совершить ход с {start_column}{start_row} на {end_column}{end_row}"
    except ValueError:
        return "Ошибка: некорректный ввод позиции"


# Ввод начальной и конечной позиции (например, e2 и e4)
start_position = input("Начальная позиция (например, e2): ")
end_position = input("Конечная позиция (например, e4): ")
print(rook_move(start_position, end_position))

# ***********************************************************************************************************************
