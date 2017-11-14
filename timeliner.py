import re

from search_utils import *

terminator = '.;\n'

with open('text.txt', 'r', encoding='utf8') as file:
    text = file.read()
    year = re.compile("\d\d\d\d")
    iterable = year.finditer(text)
    for i in iterable:
        span_start = i.span()[0]
        span_end = i.span()[1]
        if not is_year(text[span_start:span_end]):
            continue
        start = find_first_pre(text, terminator, span_start)
        finish = find_first_after(text, terminator, span_end)
        print(text[start - 1:finish])
        print('', '-----------------', '', sep='\n')
