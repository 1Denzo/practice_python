#Задача 1. Список процессов.
# С помощью команды ps можно посмотреть список запущенных процессов.
# С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.
# Запустите эту команду и сохраните выданный результат в файл:
# $ ps aux > output_file.txt
# Столбец RSS показывает информацию о потребляемой памяти в байтах.
# Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом 
# выполнения команды ps aux, а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
# Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.

RSS_COLUMN_INDEX = 5
size_names = ['B', 'KB', 'MB', 'GB', 'TB']

def get_summary_rss(output_file):
    all_rss = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[1:]
        for line in lines:
            columns = line.split()
            if len(columns) < RSS_COLUMN_INDEX:
                continue
            try:
                rss = int(columns[RSS_COLUMN_INDEX])
                all_rss += rss
            except ValueError:
                continue

    return all_rss

def convert_to_size(bytes):
    index = 0

    while bytes >= 1024 and index < len(size_names) - 1:
        bytes /= 1024.0
        index += 1

    return f"{bytes:.2f} {size_names[index]}"
    
if __name__ == '__main__':
    from pathlib import Path

    file_path = Path(input(f"PS AUX output file path:"))
    if file_path.exists() and file_path.is_file():
        rss_mem_sum = get_summary_rss(file_path)
        rss_mem_size = convert_to_size(rss_mem_sum)
        print(f"RSS Summary: {rss_mem_size}")
    else:
        print("No such PS AUX output file...")