my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
#Индекс для перебора списка
i = 0
#Цикл while для перебора элементов
while i < len(my_list):
    if my_list[i] < 0:  #Прерываем цикл при встрече отрицательного числа
        break
    elif my_list[i] == 0:  # Пропускаем нули
        i += 1
        continue
    print(my_list[i])  # Вывод положительного числа
    i += 1