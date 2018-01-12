import re

from terms_loader import get_processed_relatives
from trigger_searcher import get_triggers, letters


def get_relativities(text, context_borders):
    result = []
    relative_words = get_processed_relatives()
    for i in context_borders:
        context = str(text[i[0]:i[1]])
        current_result = False
        for word in relative_words:
            position = context.find(word)
            if position != -1:
                if (position == 0) or not context[position-1] in letters:
                    current_result = True
                    break
        result.append(current_result)
    return result


text, context_borders, triggers = get_triggers()
rels = get_relativities(text, context_borders)
for i in range(len(rels)):
    context = context_borders[i]
    print(text[context[0]:context[1]], triggers[i], rels[i], sep="=")
    # print('--------------------')