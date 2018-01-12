from negation_determinator import get_negations
from relativity_definitor import get_relativities
from time_definitor import get_times
from trigger_searcher import get_triggers


def load_expert(filename="expert.data", separator="	"):
    expert_negation = []
    expert_relativity = []
    expert_time = []
    with open(filename, 'r') as file:
        text = file.readlines()
        for line in text:
            line = line.replace("\n", "")
            splited = line.split(separator)
            expert_negation.append(splited[0] == 'True')
            expert_relativity.append(splited[1] == 'True')
            expert_time.append(splited[2] == 'True')
    return expert_negation, expert_relativity, expert_time


def f_score_for_arrays(expert, y):
    tp = 0.000001
    tn = 0
    fp = 0
    fn = 0
    for a, b in zip(expert, y):
        if a == b:
            if a:
                tp += 1
            else:
                tn += 1
        else:
            if a:
                fn += 1
            else:
                fp += 1
    recall = tp / (tp + fp)
    precision = tp / (tp + fn)
    return 2 * precision * recall / (precision + recall)


def calc_f_score():
    expert_negation, expert_relativity, expert_time = load_expert()
    text, trigger_positions, triggers = get_triggers()
    negs = get_negations(text, trigger_positions)
    rels = get_relativities(text, trigger_positions)
    times = get_times(text, trigger_positions)
    print("Negations: ", f_score_for_arrays(expert_negation, negs))
    print("Relativity: ", f_score_for_arrays(expert_relativity, rels))
    print("Times: ", f_score_for_arrays(expert_time, times))


calc_f_score()
