# Задача 6. Превью файла
# Что нужно сделать
# Реализуйте endpoint, который показывает превью файла, принимая на вход два параметра: SIZE (int) и RELATIVE_PATH — и возвращая первые SIZE символов файла по указанному в RELATIVE_PATH пути.
# Endpoint должен вернуть страницу с двумя строками.
# В первой строке будет содержаться информация о файле: его абсолютный путь и размер файла в символах, а во второй строке — первые SIZE символов из файла:
# <abs_path> <result_size><br> 
# <result_text>
# где abs_path — написанный жирным абсолютный путь до файла;
# result_text — первые SIZE символов файла;
# result_size — длина result_text в символах.
# Перенос строки осуществляется с помощью HTML-тега <br>.
# Пример:
# docs/simple.txt:
# hello world!
# /preview/8/docs/simple.txt
# /home/user/module_2/docs/simple.txt 8
# hello wo
# /preview/100/docs/simple.txt
# /home/user/module_2/docs/simple.txt 12
# hello world!

from flask import Flask, request, Response
import os

app = Flask(__name__)

@app.route('/preview/<int:size>/<path:relative_path>')
def preview_file(size, relative_path):
    abs_path = os.path.abspath(relative_path)
    
    if not os.path.isfile(abs_path):
        return Response("Файл не найден.", status=404)

    with open(abs_path, 'r', encoding='utf-8') as file:
        result_text = file.read(size)
    
    result_size = len(result_text)

    response_html = f"""
    <html>
        <body>
            <p><strong>{abs_path}</strong> {result_size}</p>
            <p>{result_text}</p>
        </body>
    </html>
    """
    
    return Response(response_html, content_type='text/html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')