import re
from terms_loader import *
from settings import *

MAX_SYMBOLS = 200
terminator = '.;\n'  # добавить союзы
letters = 'йцукенгшщзхъфывапролджэячсмитьбю'


def find_first_pre(src, targets, position):
    src = src[position - MAX_SYMBOLS:position]
    src = src[::-1]
    date_pattern = re.compile("\\.(.|..)\\.")
    offset = 0
    if not date_pattern.search(src[:4]) is None:
        offset = 4
        src = src[offset:]
    mini = MAX_SYMBOLS
    for i in targets:
        pos = src.find(i)
        if pos == -1:
            continue
        mini = min(pos, mini)
    result_candidate = position - mini - offset
    max_conj_position = 0
    if USE_CONJUNCTIONS:
        left_context = str(src[result_candidate:position])
        for conj in get_processed_conjunctions():
            regex = '((?![а-яА-Я]).)' + conj + '((?![а-яА-Я]).)'
            pos = left_context.rfind(regex)
            if pos is not None:
                max_conj_position = max(max_conj_position, pos)

    return result_candidate + max_conj_position


def find_first_after(src, targets, position):
    src = src[position:position + MAX_SYMBOLS]
    pattern = re.compile("^(.){1,2}\\.")
    offset = 0
    if not pattern.search(src) is None:
        offset = 2
        src = src[offset:]
    mini = MAX_SYMBOLS
    for i in targets:
        pos = src.find(i)
        if pos == -1:
            continue
        mini = min(pos, mini)
    result_candidate = position + mini + offset
    min_conj_position = 0
    if USE_CONJUNCTIONS:
        right_context = str(src[position:result_candidate])
        for conj in get_processed_conjunctions():
            regex = '((?![а-яА-Я]).)' + conj + '((?![а-яА-Я]).)'
            pattern = re.compile(regex)
            pos = pattern.search(right_context)
            if pos is not None:
                min_conj_position = min(min_conj_position, pos)

    return result_candidate


def is_year(s):
    return '1900' < s < '2020'
