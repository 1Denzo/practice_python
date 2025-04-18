from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, NumberRange
from task2 import NumberLength

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message='Email обязателен для заполнения.'),
        Email(message='Неверный формат email.')
    ])
    phone = IntegerField('Phone', validators=[
        DataRequired(message='Телефон обязателен для заполнения.'),
        NumberLength(min=10, max=10, message='Телефон должен содержать 10 символов.'),
        NumberRange(min=0, message='Телефон должен быть положительным числом.')
    ])
    name = StringField('Name', validators=[
        DataRequired(message='Имя обязательно для заполнения.')
    ])
    address = StringField('Address', validators=[
        DataRequired(message='Адрес обязателен для заполнения.')
    ])
    index = IntegerField('Index', validators=[
        DataRequired(message='Индекс обязателен для заполнения.'),
        NumberRange(min=0, message='Индекс должен быть положительным числом.')
    ])
    comment = TextAreaField('Comment')