import json
import re

from pathlib import Path
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
from tqdm import tqdm
from collections import Counter

# Lê o arquivo com as palavras


def read_data(filename):
    with open(filename, 'r') as file:
        data = [json.loads(line) for line in file]
    return data

# Limpa as palavras


def minusculas(tokens):
    return [token.lower() for token in tokens]


def remove_digitos(tokens):
    return [token for token in tokens if re.fullmatch('[^\d]*', token)]


def pega_palavras(tokens):
    return [token for token in tokens if re.fullmatch('\w+', token)]


def stop_words(tokens):
    stop_words = set(stopwords.words('portuguese'))
    return [token for token in tokens if not token in stop_words]

# Remove alguns tipos de palavras, como artigos
# https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html


def tag_words(text):
    remove_tags = ['DT', 'TO', 'IN']
    tagged = pos_tag(text)
    return [tag[0] for tag in tagged if not tag[1] in remove_tags]

# Limpa os tokens


def limpa_tokens(tokens):
    tokens = minusculas(tokens)
    tokens = remove_digitos(tokens)
    tokens = pega_palavras(tokens)
    tokens = stop_words(tokens)
    return tokens


def main():

    arquivo = 'dump_small_clean.jsonln'
    with open(arquivo, 'r') as f:
        data = list(json.load(f))

    all_words = []
    for item in tqdm(data):
        texto = item
        tokens = word_tokenize(texto)
        tokens = limpa_tokens(tokens)
        all_words += tokens

    tagged_words = tag_words(all_words)

    word_counts_list = list(Counter(tagged_words).items())
    word_counts_list_sorted = sorted(
        word_counts_list, key=lambda x: (-x[1], x[0]))

    vocab = dict(word_counts_list_sorted[0:3000])

    with open("vocab.jsonln", "w") as fp:
        json.dump(vocab, fp)

    print(vocab)
    return vocab


if __name__ == '__main__':
    main()
