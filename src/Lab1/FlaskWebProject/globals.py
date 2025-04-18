import re
import os

class Counter:
    def __init__(self):
        self.visits = 0

cars_list = ['Chevrolet', 'Renault', 'Ford', 'Lada']
cats_list = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
counter_visits = Counter()

BOOK_FILE = os.path.abspath('war_and_peace.txt')
with open(BOOK_FILE, 'r', encoding='utf-8') as file:
    text = file.read()
words = re.findall(r'\b\w+\b', text)