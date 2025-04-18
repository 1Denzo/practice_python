# Задача 4. Хорошего дня!
# Что нужно сделать
# Реализуйте endpoint /hello-world/<имя>, который возвращает строку «Привет, <имя>. Хорошей пятницы!». Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом, на русском языке.
# Пример запроса, сделанного в субботу:
# /hello-world/Саша  →  Привет, Саша. Хорошей субботы!
# Советы и рекомендации
#     • Текущий день недели можно узнать так:

# from datetime import datetime 
# weekday = datetime.today().weekday()

# Обратите внимание, что weekday() возвращает число от 0 до 6.
#     • Как лучше хранить названия дней недели? Посмотрите, сколько памяти занимают кортеж, список и словарь с одними и теми же данными с помощью метода getsizeof из модуля sys:

# import sys 
#  
# print(sys.getsizeof(weekdays_tuple)) 
# print(sys.getsizeof(weekdays_list)) 
# print(sys.getsizeof(weekdays_dict))

from flask import Flask
from datetime import datetime

app = Flask(__name__)

weekdays = {
    0: ('понедельника', 'его'),
    1: ('вторника', 'его'),
    2: ('среды', 'ей'),
    3: ('четверга', 'его'),
    4: ('пятницы', 'ей'),
    5: ('субботы', 'ей'),
    6: ('воскресенья', 'его')
}

@app.route('/hello_world/<name>')
def hello_world(name):
    weekday = datetime.today().weekday()
    day, good_form = weekdays[weekday]
    greeting = f"Привет, {name}. Хорош{good_form} {day}!"
    return greeting


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')