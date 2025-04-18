# Задача 2. Средний размер файла
#  Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):
# $ ls -l | python3 get_mean_size.py
# Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l, а возвращает средний размер файла в каталоге.
# Советы и рекомендации
#     • Конвейер (pipe) — это механизм передачи данных со стандартного потока вывода одной программы на стандартный поток ввода другой программы. Пример запуска конвейера:

# $ ls -R | grep “\.txt” | wc -w 
# 1)      2)             3)

# 1) Получаем рекурсивно все файлы в текущем каталоге.
# 2) Получаем из них файлы с расширением .txt.
# 3) Получаем общее количество слов в .txt-файлах.
#     • Получить входные данные можно следующим образом:

# import sys 
#  
# data = sys.stdin.read()

SIZE_COLUMN_INDEX = 4

def get_mean_size(ls_output):
    total_size = 0
    file_count = 0

    for line in ls_output.strip().split('\n'):
        columns = line.split()

        if len(columns) < SIZE_COLUMN_INDEX:
            continue

        try:
            total_size += int(columns[SIZE_COLUMN_INDEX])
            file_count += 1
        except (ValueError, IndexError):
            continue

    if file_count == 0:
        return None
    
    return total_size / file_count

if __name__ == '__main__':
    import sys

    ls_output = sys.stdin.read()
    mean_size = get_mean_size(ls_output)

    if mean_size is None:
        print("No files for handling")
    else:
        print(f"Average: {mean_size:.2f} bytes")