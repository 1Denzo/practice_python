from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import ValidationError
from typing import Optional

def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: IntegerField):
        number_str = str(field.data)
        if not (min <= len(number_str) <= max):
            raise ValidationError(message or f'Длина числа должна быть от {min} до {max} символов.')
    return _number_length

class NumberLength:
    def __init__(self, min: int, max: int, message: Optional[str] = None):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form: FlaskForm, field: IntegerField):
        number_str = str(field.data)
        if not (self.min <= len(number_str) <= self.max):
            raise ValidationError(self.message or f'Длина числа должна быть от {self.min} до {self.max} символов.')
