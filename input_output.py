def input_number(text=None):
    if text:
        print(text)
    try:
        number = int(input('> '))
    except ValueError:
        print('\nНеверный ввод. Введите число.')
        return input_number(text)
    return number


def input_menu_action(menu):
    return input_number(text=menu)


def input_file_path():
    print('\nВведите имя файла, расположенного в одном каталоге с исполняемым файлом, или '
          'абсолютный путь к файлу:')
    return input('> ')
