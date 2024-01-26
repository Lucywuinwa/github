import sys


def capcount(gvn_str):
    count = 0
    for charter in gvn_str:
        if charter.isupper():
            count += 1

    return count


def capsum(gvn_str):
    score = 0
    for i in range(len(gvn_str)):
        if gvn_str[i].isupper():
            score += i
    return score

def score_sentence(gvn_str):
    capital_count = 0
    score = 0
    for i, character in enumerate(gvn_str):
        if character.isupper():
            capital_count += 1
            score += i

    return capital_count, score

print(capcount(sys.argv[1]))
print(capsum(sys.argv[1]))

capital_count, score = score_sentence(sys.argv[1])
print(capital_count)
print(score)