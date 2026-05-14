import random
import word_bank

def generate_round():
    letter = random.choice(word_bank.letter_bank)
    rights = [w for w in word_bank.word_bank if w.lower().startswith(letter)]
    wrongs = [w for w in word_bank.word_bank if not w.lower().startswith(letter)]

    selected_rights = random.choice(rights)
    selected_wrongs = random.sample(wrongs, 24)

    final_matrix = selected_wrongs + [selected_rights]

    random.shuffle(final_matrix)
    return final_matrix, selected_rights, letter

    