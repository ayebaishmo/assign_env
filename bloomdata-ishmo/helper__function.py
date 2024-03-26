import random 
def random_phrase():
    adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
    nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']

    adjectives = random.choice(adjectives)
    nouns = random.choice(nouns)
    return adjectives + nouns

