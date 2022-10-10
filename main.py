import csv
# задаю переменные
count = count_30 = count_1 = 0
author_name = ''
author_name = input('Введите имя автора: ')
# открытие файла для записи
f = open('list_of_20.txt', 'w+')
# открытие csv файла
with open('books.csv') as File:
    reader = csv.reader(File)

    # поиск по автору + кол-во записей
    for row in reader:
        count += 1
        # получаем строку
        line = ''.join(row).replace(";;", ";").split(";")
        # находим кол-во записей с названием длиннее 30
        if len(line[1]) > 30:
            count_30 += 1
        # реализация задачи 4
        if author_name in line and line[7] < '200':
            count_1 += 1
            print(str(count_1) + ') ' + line[1].replace('#', '') + ', '
                       + line[2] + ', ' + line[3] + ', ' + line[4] + ', '
                       + line[5] + ', ' + line[6] + ', ' + line[7])
        # реализация задачи 5
        if 1 < count <= 20:
            ln = str(count) + ' ' + line[3] + ' ' + line[1].replace('#','') + ' - ' + line[6]
            # запись в файл
            f.write(ln + '\n')
# закрытие файла для записи + вывод всех ответов
f.close()
print('\nОтветы на вопросы')
print('2) ', count)
print('3) ', count_30)


