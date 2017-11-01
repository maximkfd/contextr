def load_terms():
    terms = []
    with open('terms.txt', 'r', encoding='utf8') as file:
        line = file.readline()
        while line != '':
            terms.append(line[:-1])
            line = file.readline()
    return terms

def get_processed_terms():
    terms = load_terms()
    result = []
    for term in terms:
        if len(term) > 3:
            if term[-1:] in 'йеуиюаояыв':
                term = term[:-1]
            if term[-1:] in 'йеуиюаояы':
                term = term[:-1]
        result.append(term)
    return result
