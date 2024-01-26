import sys


def score_sentence(gvn_str):
    capital_count = 0
    score = 0
    for i, character in enumerate(gvn_str):
        if character.isupper():
            capital_count += 1
            score += i

    return capital_count, score



capital_count, score = score_sentence(sys.argv[1])
print(capital_count)
print(score)
