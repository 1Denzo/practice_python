# Задача 7. Учёт финансов
# Что нужно сделать
# Реализуйте приложение для учёта финансов, умеющее запоминать,
#  сколько денег было потрачено за день, а также показывать затраты за отдельный месяц и за целый год.
# В программе должно быть три endpoints:
#     • /add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день;
#     • /calculate/<int:year> — получение суммарных трат за указанный год;
#     • /calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц.
# Дата для /add/ передаётся в формате YYYYMMDD, где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
# Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).
# Советы и рекомендации
#     • У словаря есть метод setdefault, который возвращает значение по ключу, а если 
# такого ключа нет, инициализирует элемент заданным значением.
# Вариант с большим количеством вложенных условий:

# if year in storage: 
# if month in storage[year]: 
#         storage[year][month] += expense 
#     else: 
#         … 
# else: 
#     …

# Вариант с использованием setdefault:

# storage.setdefault(year, {}).setdefault(month, {}) 
# storage[year][month] += expense

#     • Рассмотрите несколько вариантов хранения информации.
# Какой из них будет работать наиболее эффективно? 
# Нужно ли каждый раз пересчитывать траты за год или месяц?

from collections import defaultdict
from datetime import datetime
from flask import Flask, jsonify

EXPENSE_ADD_SUCCESS = "Expense added successfully"
INVALID_DATE_FORMAT = "Invalid date format. Use YYYYMMDD."
NEGATIVE_INTEGER = "Expense must be a non-negative integer."
INVALID_KEY = "Invalid input data."

app = Flask(__name__)

app.storage = defaultdict(lambda: defaultdict(int))

@app.route('/add/<date>/<int:number>', methods=["POST"])
def add_expense(date, number):
    """
    Роут на добавление расхода
    """
    if number < 0:
        return jsonify({"error": NEGATIVE_INTEGER}), 400

    try:
        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:8])
        datetime(year, month, day)
    except ValueError:
        return jsonify({"error": INVALID_DATE_FORMAT}), 400

    app.storage[year][month] += number
    return jsonify({"message": EXPENSE_ADD_SUCCESS}), 201

@app.route('/calculate/<int:year>', methods=['GET'])
def calculate_year(year):
    """
    Считает затраты за год
    """
    if year in app.storage:
        total_expense = sum(app.storage[year].values())
        return jsonify({"year": year, "total_expense": total_expense}), 200
    return jsonify({"year": year, "total_expense": 0}), 200

@app.route('/calculate/<int:year>/<int:month>')
def calculate_month(year, month):
    """
    Считает затраты за месяц
    """
    if year in app.storage:
        total_expense = app.storage[year].get(month, 0)
        return jsonify({"year": year, "month": month, "total_expense": total_expense}), 200
    return jsonify({"year": year, "month": month, "total_expense": 0}), 200

if __name__ == "__main__":
    app.run(debug=True)