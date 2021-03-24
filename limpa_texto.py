import re
import json

arquivo = '/home/gabriel/Insper/PROCESSAMENTO DE LINGUAGEM NATURAL/Aula04/dump_small.jsonln'

data = []
with open(arquivo, 'r') as file:
    for line in file:
        data.append(json.loads(line))


def limpa_url(texto):
    # Regex obtida de https://www.geeksforgeeks.org/python-check-url-string/
    pattern = r"""
        (?i)  # Ignore case.
        \b  # Inicio de palavra.
        (?:
            https?://
        |
            www
            \d{0,3}
            [.]
        |
            [a-z0-9.\-]+
            [.]
            [a-z]{2,4}
            /
        )
        (?:
            [^\s()<>]+
        |
            \(
            (?:
                [^\s()<>]+
            |
                \(
                [^\s()<>]+
                \)
            )*
            \)
        )+
        (?:
            \(
            (?:
                [^\s()<>]+
            |
                \(
                [^\s()<>]+
                \)
            )*
            \)
        |
            [^\s`!()\[\]{};:'\".,<>?«»“”‘’]
        )
    """
    repl = ''
    matcher = re.compile(pattern, re.VERBOSE)
    return matcher.sub(repl, texto)


def limpa_meta(texto):
    pattern = r"(?:^|\n){[{|\|](?!.*?}}).+(?:\n+.+)+?\n[}|\|]}"
    repl = r" "
    matcher = re.compile(pattern)
    texto = matcher.sub(repl, texto)

    pattern = r"(?:^|\n){[{|\|].+(?:\n+.+)+?\n[}|\|]}"
    repl = r" "
    matcher = re.compile(pattern)
    texto = matcher.sub(repl, texto)

    return texto


def limpa_math(texto):
    pattern = r"<math>(?:.|\s)*?</math>"
    repl = r" "
    matcher = re.compile(pattern)
    texto = matcher.sub(repl, texto)

    return texto


def limpa_ref(texto):
    pattern = r"<ref>(?:.|\s)*?</ref>|<ref(?:.|\s)*?/>|<ref(?:.|\s)*?>(?:.|\s)*?</ref>"
    repl = r" "
    matcher = re.compile(pattern)
    texto = matcher.sub(repl, texto)

    return texto


def limpa_gallery(texto):
    pattern = r"<gallery>(?:.|\s)*?</gallery>"
    repl = r" "
    matcher = re.compile(pattern)
    texto = matcher.sub(repl, texto)

    return texto


def limpa_br(texto):
    pattern = r"<br\s+?/>"
    repl = r" "
    matcher = re.compile(pattern)
    texto = matcher.sub(repl, texto)

    return texto


def limpa_small(texto):
    pattern = r"<small>(?:.|\s)*?</small>"
    repl = r" "
    matcher = re.compile(pattern)
    texto = matcher.sub(repl, texto)

    return texto


def limpa_big(texto):
    pattern = r"<big>(?:.|\s)*?</big>"
    repl = r" "
    matcher = re.compile(pattern)
    texto = matcher.sub(repl, texto)

    return texto


def limpa_sup(texto):
    pattern = r"<sup>(?:.|\s)*?</sup>"
    repl = r" "
    matcher = re.compile(pattern)
    texto = matcher.sub(repl, texto)

    return texto


def limpa_center(texto):
    pattern = r"<center>|</center>"
    repl = r" "
    matcher = re.compile(pattern)
    texto = matcher.sub(repl, texto)

    return texto


def limpa_marks(texto):
    pattern = r"<.*?>|</.*?>"
    repl = r" "
    matcher = re.compile(pattern)
    texto = matcher.sub(repl, texto)

    return texto


def limpa_wikilinks(texto):
    pattern = r"\[\[(?:[^|]*?\|)*?([^|]*?)\]\]"
    repl = r"\1"
    matcher = re.compile(pattern)
    texto = matcher.sub(repl, texto)

    pattern = r"\[\[(.*?)\]\]"
    repl = r"\1"
    matcher = re.compile(pattern)
    texto = matcher.sub(repl, texto)

    pattern = r"\[(.*?)\]"
    repl = r"\1"
    matcher = re.compile(pattern)
    texto = matcher.sub(repl, texto)

    return texto


def limpa_templates(texto):
    conta = 0
    spans_proibidos = []
    for item in re.finditer(r'{{|}}', texto):
        if item[0] == '{{':
            if conta == 0:
                inicio = item.span()[0]
            conta += 1
        else:
            conta -= 1
            if conta == 0:
                fim = item.span()[1]
                spans_proibidos.append((inicio, fim))
    texto_limpo = ''
    inicio = 0
    for span in spans_proibidos:
        fim, novo_inicio = span
        texto_limpo += texto[inicio:fim]
        inicio = novo_inicio
    texto_limpo += texto[inicio:]
    return texto_limpo


def limpa_outras_linguas(texto):
    pattern = r"\s[^A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]+\s"
    repl = r" "
    matcher = re.compile(pattern)
    texto = matcher.sub(repl, texto)

    return texto


def limpa_iniciais(texto):
    pattern = r"[A-Z]\."
    repl = r""
    matcher = re.compile(pattern)
    return matcher.sub(repl, texto)


def limpa_acronimos(texto):
    pattern = r"[A-Z][a-z]*[A-Z]+"
    repl = r""
    matcher = re.compile(pattern)
    return matcher.sub(repl, texto)


def limpa_abreviacoes(texto):
    pattern = r"\w +\.(?=\s+[a-z0-9])"
    repl = r""
    matcher = re.compile(pattern)
    return matcher.sub(repl, texto)


def limpa_aspas(texto):
    pattern = r"""['"“]+"""
    repl = r" "
    matcher = re.compile(pattern, re.VERBOSE)
    return matcher.sub(repl, texto)


def limpa_parenteses(texto):
    pattern = r"\(|\)"
    repl = r" "
    matcher = re.compile(pattern)
    return matcher.sub(repl, texto)


def limpa_alphanumeric(texto):
    pattern = r"\S*\d+\S*"
    repl = r" "
    matcher = re.compile(pattern)
    texto = matcher.sub(repl, texto)
    return texto


def limpa_barra(texto):
    pattern = r"(\w+)/(\w+)"
    repl = r'\1 \2'
    matcher = re.compile(pattern, re.VERBOSE)
    texto = matcher.sub(repl, texto)
    return texto


def limpa_pontuacoes(texto):
    pattern = r"\*|=+|;+|:+|[–—]+|\s[][-]+\s|\.+|,+"
    repl = r" "
    matcher = re.compile(pattern)
    return matcher.sub(repl, texto)


def limpa_letras_avulcas(texto):
    pattern = r"\s[^AEIOUaeiou]\s"
    repl = r" "
    matcher = re.compile(pattern)
    return matcher.sub(repl, texto)


def so_palavras(texto):
    pattern = r"(?:^|\n|\s)[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]*[^A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ -`'’]+[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]*"
    repl = r" "
    matcher = re.compile(pattern)
    return matcher.sub(repl, texto)


def coloca_em_uma_linha(texto):
    pattern = r"\s+"
    repl = r' '
    matcher = re.compile(pattern, re.VERBOSE)
    texto = matcher.sub(repl, texto)
    return texto


def limpa_texto(texto):
    texto = limpa_meta(texto)
    texto = limpa_wikilinks(texto)
    texto = limpa_templates(texto)
    texto = limpa_math(texto)
    texto = limpa_ref(texto)
    texto = limpa_gallery(texto)
    texto = limpa_br(texto)
    texto = limpa_small(texto)
    texto = limpa_big(texto)
    texto = limpa_sup(texto)
    texto = limpa_center(texto)
    texto = limpa_marks(texto)
    texto = limpa_outras_linguas(texto)
    texto = limpa_url(texto)
    texto = limpa_iniciais(texto)
    texto = limpa_acronimos(texto)
    texto = limpa_abreviacoes(texto)
    texto = limpa_aspas(texto)
    texto = limpa_parenteses(texto)
    texto = limpa_alphanumeric(texto)
    texto = limpa_barra(texto)
    texto = limpa_pontuacoes(texto)
    texto = limpa_letras_avulcas(texto)
    texto = so_palavras(texto)
    texto = coloca_em_uma_linha(texto)

    return texto
