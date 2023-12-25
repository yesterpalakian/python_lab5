'''1. Импортировать датасет.
2. Взять 1000 значений из выбранного датасета.
3. Проверить данные на пропуски.
4. Проверить на нормальность распределения и выбросы.
Использовать для проверки нормальности распределения ящики с усами
(логарифмическую шкалу) и гистограммы.
5. Заполнить пропуски и обработать аномальные значения.
6. Определить сколько в выборке 1, 2, 3 …комнатных квартир.
7. Построить сводную таблицу: подписи строк – районы, подписи
колонок – комнаты, пересечение строк и столбцов – количество квартир в этом
районе.
8. Итоговый обработанный массив без выбросов и пропусков
сохраните в файл surname.csv
9. Вышлите итоговый вый файл на проверку преподавателю.'''

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def gaps_check(test):
    for j, dat in test.items():
        skip = test[test[j].isnull()]
        if not skip.empty:
            print("B " + str(j) + " были замечены пропуски")


def distribution_and_emissions_check(test):
    for i in range(len(test.columns)):
        print(str(1 + 1) + "|" + (test.columns[i]))
    number_of_graf = int(input("Выберите величину: ")) - 1
    values_of_graf = test.columns[number_of_graf]
    entered_graf = int(input(" 1 | Ящик с усами\n 2 | Гистограмма \n"))

    if entered_graf == 1:
        plt.title(test.columns[number_of_graf])
        plt.boxplot(test[values_of_graf])
    elif entered_graf == 2:
        plt.title(test.columns[number_of_graf])
        plt.hist(test[values_of_graf])
    plt.show()


def fill_gaps(test):
    for col_name, data in test.items():
        skips = test[test[col_name].isnull()]
        if not skips.empty:
            test[col_name] = input("Чем заменить пропуски в " + str(col_name) + " :")


def get_number_of_rooms(test):
    amount_of_flats = pd.pivot_table(test, values="Id", index=["Rooms"], aggfunc=np.size, fill_value=0)
    print("Количество квартир:\n "
          + str(amount_of_flats))


def build_table(toread):
    frame_info = pd.pivot_table(data_inter, values="Id", index=["DistrictId"],
                                columns=["Rooms"], aggfunc=np.size, fill_value=0)
    print("Сводная таблица:\n" + str(frame_info))
    toread.to_csv("surname.csv")


data_inter = pd.read_csv("test.csv", sep=",")
data_inter = data_inter.head(1000)
while True:
    print(" 1 - Проверка на пропуски\n"
          " 2 - Проверить на нормальность распределения и выбросы\n"
          " 3 - Заполнить пропуски и обработать аномальные значения \n"
          " 4 - Определить сколько в выборке 1, 2, 3 ...комнатных квартир\n"
          " 5 - Построить сводную таблицу\n"
          " 6 - Выход")
    try:
        while True:
            choice = int(input("Выберите пункт: "))
            if not 1 <= choice <= 6:
                raise ValueError

            if choice == 1:
                gaps_check(data_inter)
                break
            elif choice == 2:
                distribution_and_emissions_check(data_inter)
                break
            elif choice == 3:
                fill_gaps(data_inter)
                break
            elif choice == 4:
                get_number_of_rooms(data_inter)
                break
            elif choice == 5:
                build_table(data_inter)
                break
            elif choice == 6:
                exit(0)
    except ValueError:
        print("Некорректный ввод")