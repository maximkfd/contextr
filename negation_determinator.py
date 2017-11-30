import re

from terms_loader import *
from trigger_searcher import get_triggers


def get_negations(text, trigger_contexts):
    neg_words = get_processed_negations()
    result = []
    for positions in trigger_contexts:
        context = text[positions[0]:positions[1]]
        current_result = False
        for n_word in neg_words:
            regex = '(^|((?![а-яА-Я]).))' + n_word + '($|((?![а-яА-Я]).))'
            pattern = re.compile(regex)
            if pattern.search(context) is not None:
                current_result = not current_result
        result.append(current_result)
    return result


text, trigger_positions, triggers = get_triggers()
negs = get_negations(text, trigger_positions)
for i in range(len(negs)):
    print(text[trigger_positions[i][0]:trigger_positions[i][1]], "  |  ", triggers[i], "  |  ", negs[i])
    print("-----------------------------------------------------------------------")
