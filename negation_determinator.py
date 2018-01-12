import re

from relativity_definitor import get_relativities
from settings import USE_NEUTRAL
from terms_loader import *
from trigger_searcher import get_triggers

import numpy as np


def get_negations(text, trigger_contexts):
    neg_words = get_processed_negations()
    probability_words = get_processed_probs()
    result = []
    for positions in trigger_contexts:
        context = text[positions[0]:positions[1]]
        current_result = True
        if USE_NEUTRAL:
            for p_word in probability_words:
                regex = '(^|((?![а-яА-Я]).))' + p_word + '($|((?![а-яА-Я]).))'
                pattern = re.compile(regex)
                if pattern.search(context) is not None:
                    result.append(current_result)
                    continue
        for n_word in neg_words:
            regex = '(^|((?![а-яА-Я]).))' + n_word + '($|((?![а-яА-Я]).))'
            pattern = re.compile(regex)
            if pattern.search(context) is not None:
                current_result = not current_result
        result.append(current_result)
    return result


text, trigger_positions, triggers = get_triggers()
negs = get_negations(text, trigger_positions)
rels = get_relativities(text, trigger_positions)

nprel = np.array(rels)
npborder = np.array(trigger_positions)
nptriggers = np.array(triggers)
npnegs = np.array(negs)
nppositions = np.array([])
for i in trigger_positions:
    nppositions = np.append(nppositions, i[0])
indicies = nppositions.argsort()
nprel = nprel[indicies]
npborder = npborder[indicies]
nptriggers = nptriggers[indicies]
npnegs = npnegs[indicies]
for i in range(len(negs)):
    print(text[npborder[i][0]:npborder[i][1]], nptriggers[i], npnegs[i], nprel[i], sep="=")
    # print("-----------------------------------------------------------------------")
