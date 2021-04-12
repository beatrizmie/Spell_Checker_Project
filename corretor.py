import sys
import json
import numpy as np

ADD_COST = 1
DEL_COST = 1
REPL_COST = 1

LOWERCASE = [chr(x) for x in range(ord('a'), ord('z') + 1)]
UPPERCASE = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
LOWERCASE_OTHERS = ['ç', 'á', 'â', 'à', 'ã', 'é', 'ê', 'í', 'ó', 'ô', 'õ', 'ú']
UPPERCASE_OTHERS = [x.upper() for x in LOWERCASE_OTHERS]
LETTERS = LOWERCASE + UPPERCASE + LOWERCASE_OTHERS + UPPERCASE_OTHERS


def read_data(filename):
    with open(filename, 'r') as file:
        data = [json.loads(line) for line in file]
    return data


def levenshtein(s1, s2):
    n1 = len(s1) + 1
    n2 = len(s2) + 1
    D = np.zeros((n1, n2))
    D[:, 0] = np.arange(n1)
    D[0, :] = np.arange(n2)

    for r in range(1, n1):
        for c in range(1, n2):
            cost_add = D[r, c - 1] + ADD_COST
            cost_del = D[r - 1, c] + DEL_COST
            if s1[r - 1] == s2[c - 1]:
                cost_sub = D[r - 1, c - 1]
            else:
                cost_sub = D[r - 1, c - 1] + REPL_COST
            D[r, c] = min([cost_add, cost_del, cost_sub])
    return D[n1 - 1, n2 - 1]


def levenshtein_2(s1, s2):
    n1 = len(s1) + 1
    n2 = len(s2) + 1
    previous = np.arange(n2)
    current = np.zeros(n2)
    for r in range(1, n1):
        current[0] = r
        for c in range(1, n2):
            cost_add = current[c - 1] + ADD_COST
            cost_del = previous[c] + DEL_COST
            if s1[r - 1] == s2[c - 1]:
                cost_sub = previous[c - 1]
            else:
                cost_sub = previous[c - 1] + REPL_COST
            current[c] = min([cost_add, cost_del, cost_sub])
        previous, current = current, previous
    return previous[-1]


def edit1(text):
    words = []

    # Fase 1: as remoções.
    for p in range(len(text)):
        new_word = text[:p] + text[p + 1:]
        if len(new_word) > 0:
            words.append(new_word)

    # Fase 2: as adições.
    for p in range(len(text) + 1):
        for c in LETTERS:
            new_word = text[:p] + c + text[p:]
            words.append(new_word)

    # Fase 3: as substituições.
    for p in range(len(text)):
        orig_c = text[p]
        for c in LETTERS:
            if orig_c != c:
                new_word = text[:p] + c + text[p + 1:]
                words.append(new_word)

    return set(words)


def edit2(words1, text):
    words2 = set()
    for w in words1:
        candidate_words2 = edit1(w)
        candidate_words2 -= words1
        words2.update(candidate_words2)
    words2 -= set([text])
    return words2


def main():

    arquivo = 'vocab.jsonln'
    with open(arquivo, 'r') as f:
        vocab = json.load(f)

    # frase = ' '.join(sys.argv[1:])
    frase = input("Digite uma frase: ")
    words = frase.split(" ")

    for i, word in enumerate(words):

        if word not in vocab:
            words1 = edit1(word)
            candidatos_1 = [w for w in words1 if w in vocab]

            if (len(candidatos_1) == 0):
                words2 = edit2(words1, word)
                candidatos_2 = [w for w in words2 if w in vocab]
                w = 0

                for jw in candidatos_2:
                    if w == 0:
                        w = jw
                    else:
                        if vocab[jw] > vocab[w]:
                            w = jw

                words[i] = w

            else:
                w = 0
                for jw in candidatos_1:

                    if w == 0:
                        w = jw
                    else:
                        if vocab[jw] > vocab[w]:
                            w = jw

                words[i] = w

    print("Você quis dizer:", *words, "?")

if __name__ == '__main__':
    main()
