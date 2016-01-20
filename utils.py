

def generate_question(options):
    question = ""
    possibilities = list(range(len(options)))
    for i, card in enumerate(options):
        question += str(card) + "(press " + str(i) + ") "
    return question, possibilities
