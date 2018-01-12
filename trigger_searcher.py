import re

from search_utils import *
from terms_loader import *


def get_triggers():
    terms = get_processed_terms()
    context_borders = []
    triggers = []

    with open('text.txt', 'r', encoding="utf-8") as f:
        text = f.read()
        for term in terms:
            word_reg = re.compile(term)
            iterable = word_reg.finditer(text)
            for i in iterable:
                span_start = i.span()[0]
                span_end = i.span()[1]
                if text[span_start-1].lower() in letters:
                    continue
                triggers.append(text[span_start:span_end])
                start = find_first_pre(text, terminator, span_start)
                finish = find_first_after(text, terminator, span_end)
                context_borders.append([start, finish])
    return text, context_borders, triggers


def print_triggers_with_context():
    text, context_borders, triggers = get_triggers()
    for i in range(len(context_borders)):
        context = context_borders[i]
        print(text[context[0]:context[1]], "   |   ", triggers[i])
        print('--------------------')


# print_triggres_with_context()
