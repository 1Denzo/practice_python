# Задача 5. Максимальное число
# Что нужно сделать
# Реализуйте endpoint, начинающийся с /max_number, в который можно передать список чисел, разделённых слешем /. Endpoint должен вернуть текст «Максимальное переданное число {number}», где number<.code> — выделенное курсивом наибольшее из переданных чисел.
# Примеры:
# /max_number/10/2/9/1
# Максимальное число: 10
# /max_number/1/1/1/1/1/1/1/2
# Максимальное число: 2

from flask import Flask, jsonify
from werkzeug.exceptions import BadRequest


app = Flask(__name__)


@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    numbers_list = numbers.split('/')
    try:
        int_numbers = [int(num) for num in numbers_list]
    except ValueError:
        raise BadRequest("Все перечисленные значения должны быть числами")
    
    max_num = max(int_numbers)

    response = f"Максимальное число: <i>{max_num}</i>"
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')