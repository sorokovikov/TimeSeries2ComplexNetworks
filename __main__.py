from matplotlib import pyplot as plt
from input_output import *

import math
import myplots
import networkx as nx
import numpy as np
import os.path
import pandas as pd
import random


interval_start: int = None
interval_stop: int = None
df: pd.DataFrame = None


def show_main_menu():
    action = input_menu_action('\nВас приветствует программа конвертирования временных рядов в комплексные сети.\n'
                               'Выберите и введите номер действия:\n'
                               '1. Загрузить файл (формат .csv);\n'
                               '2. Демонстрационный режим;\n'
                               '3. Выход.')
    if action == 1:
        load_csv_file()
    elif action == 2:
        show_demo_menu()
    elif action == 3:
        print('\nВыход.')
        exit(0)
    else:
        print('\nНеверный ввод. Введите номер действия.')
        show_main_menu()


def show_data_menu():
    action = input_menu_action('\nВыберите и введите номер действия над данными:\n'
                               '1. Построить график временного ряда;\n'
                               '2. Построить график комплексной сети;\n'
                               '3. Построить граф комплексной сети;\n'
                               '4. Вернуться в главное меню ->')
    if action == 1:
        data = get_investigated_data()
        print('\nПостроение графика...')
        build_time_series(data)
        show_data_menu()
    elif action == 2:
        data = get_investigated_data()
        print('\nПостроение графика...')
        build_complex_network(data)
        show_data_menu()
    elif action == 3:
        data = get_investigated_data()
        print('\nПостроение графика...')
        build_complex_network_graph(data)
        show_data_menu()
    elif action == 4:
        show_main_menu()
    else:
        print('\nНеверный ввод. Введите номер действия.')
        show_data_menu()


def load_csv_file():
    file_path = input_file_path()
    if os.path.isfile(file_path):
        global df
        df = pd.read_csv(file_path, header=0)
        show_data_menu()
    else:
        print('\nФайл с таким именем не найден.')
        show_main_menu()


def get_investigated_data():
    print('\nВыберите и введите номер столбца, по которму требуется построить график:')
    columns = df.columns.values
    count = 1
    for column in columns:
        if count < len(columns):
            print(f'{count}. {column};')
        else:
            print(f'{count}. {column}.')
        count = count + 1
    column_number = input_number() - 1
    if 0 <= column_number < len(columns):
        data = get_interval_menu()
        return data[:, column_number]
    else:
        print('\nНеверный ввод. Введите номер столбца.')
        return get_investigated_data()


def get_interval_menu():
    """
    Позволяет выбрать интервал данных для построения: весь столбец или конкретный интервал.
    Есть возможность вернуться в меню выбора столбца.
    :return: Интервал данных
    """
    global interval_start
    global interval_stop
    action = input_menu_action('\nВыберите и введите объем данных:\n'
                               '1. Весь столбец;\n'
                               '2. Ввести интервал;\n'
                               '3. Использовать ранее введенный интервал.')
    if action == 1:
        return df.to_numpy()
    elif action == 2:
        return get_data_interval(df.to_numpy())
    elif action == 3:
        if interval_stop is None:
            print('\nВы еще не вводили интервал.')
            return get_interval_menu()
        else:
            data = df.to_numpy()
            return data[interval_start:interval_stop]
    else:
        print('\nНеверный ввод. Введите номер выбранного объема данных.')
        return get_interval_menu()


def get_data_interval(data):
    global interval_start
    global interval_stop
    data_length = len(data)
    start = input_number(text=f'\nВведите индекс для начала интервала (1-{data_length - 1}):') - 1
    if start < 0 or start >= data_length - 1:
        print(f'Неверный ввод ("{start + 1}"). Начало интервала должно быть больше 0 и '
              'меньше длины стобца на 1.')
        return get_data_interval(data)
    if (data_length - start - 1) > 1:
        ending = f'{start + 2}-{data_length}'
    else:
        ending = f'{data_length}'
    stop = input_number(text=f'\nВведите индекс для конца интервала ({ending}):')
    if stop <= start + 1 or stop > data_length:
        print(f'Неверный ввод ("{stop}"). Конец интервала должен быть больше начала и меньше или равен длине столбца.')
        return get_data_interval(data)
    interval_start = start
    interval_stop = stop
    return data[start:stop]


def build_time_series(data):
    figure, ax = plt.subplots()
    myplots.time_series(data, ax)
    plt.show()


def build_complex_network(data):
    figure, ax = plt.subplots()
    myplots.complex_network(data, ax)
    plt.show()


def build_complex_network_graph(data):
    figure, ax = plt.subplots()
    myplots.complex_network_graph(data, ax)
    plt.show()


def random_sample():
    size = 100
    y = np.empty(size)
    for i in range(size):
        y[i] = random.random() * 100

    figure, axs = plt.subplots(2)
    myplots.time_series(y, axs[0])
    myplots.complex_network(y, axs[1])
    plt.show()


def show_demo_menu():
    start = -5
    stop = 5
    size = 100
    step = (stop - start) / size
    x = np.arange(start, stop, step=step)
    y = np.empty(size)
    for i in range(size):
        y[i] = 1 / math.sqrt(2 * math.pi) * math.exp(-0.5 * (x[i] ** 2))

    action = input_menu_action('\nВыберите и введите номер действия:\n'
                               '1. Построить временной ряд (нормальное распределение);\n'
                               '2. Построить комплексную сеть (нормальное распределение);\n'
                               '3. Построить графики на основе случайно сгенерированной выборки;\n'
                               '4. Вернуться в главное меню ->')
    if action == 1:
        print('\nПостроение графика...')
        build_time_series(y)
        show_demo_menu()
    elif action == 2:
        print('\nПостроение графика...')
        build_complex_network(y)
        show_demo_menu()
    elif action == 3:
        print('\nПостроение графика...')
        random_sample()
        show_demo_menu()
    elif action == 4:
        show_main_menu()
    else:
        print('\nНеверный ввод. Введите номер выбранного действия.')
        show_demo_menu()

if __name__ == '__main__':
    show_main_menu()
