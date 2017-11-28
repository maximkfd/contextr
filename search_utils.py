import re

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
    return position - mini - offset


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
    return position + mini + offset


def is_year(s):
    return '1900' < s < '2020'
