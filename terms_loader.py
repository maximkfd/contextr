def load_terms():
    terms = load_words_from_file('terms.txt')
    return terms


def get_processed_terms():
    terms = load_terms()
    result = cut_endings(terms)
    return result


def load_relatives():
    return load_words_from_file('relatives.txt')


def get_processed_relatives():
    return cut_endings(load_relatives())


def load_conjunctions():
    return load_words_from_file('conjunctions.txt')


def get_processed_conjunctions():
    conjunctions = []
    for word in load_conjunctions():
        conjunctions.append(word.lower())
    return conjunctions


def load_negations():
    return load_words_from_file('negations.txt')


def get_processed_negations():
    return load_negations()


def load_probs():
    return load_words_from_file("neutral.dictionary")


def get_processed_probs():
    return load_probs()


def cut_endings(words):
    result = []
    for term in words:
        if len(term) > 3:
            if term[-1:] in 'йеуиюаояыьв':
                term = term[:-1]
            if term[-1:] in 'йеуиюаояыь':
                term = term[:-1]
        result.append(term)
    return result


def load_words_from_file(file_name):
    terms = []
    with open(file_name, 'r', encoding='utf8') as file:
        line = file.readline()
        while line != '':
            terms.append(line[:-1])
            line = file.readline()
    return terms
