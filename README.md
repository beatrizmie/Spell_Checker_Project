# Spell_Checker_Project
### Projeto Corretor Ortográfico para a disciplina de Processamento de Linguagem Natural - Insper 2021.1

Beatriz Mie Kotsubo Kuwabara

Gabriel Zanetti Traumuller Kawall

O projeto consiste na construção de um vocabulário a partir do dataset de documentos da Wikipedia em português e de um corretor ortográfico baseado na ideia de Peter Norvig, feita em três passos:
1. Para uma palavra dada (possivelmente escrita errado), gerar todas as variantes da palavra que estajam a uma pequena distância de edição desta (distância 1 ou 2);
2. Consultar o dicionário de palavras corretas e verificar quais palavras da lista de variantes está no vocabulário;
3. Se alguma variante fizer parte do dicionário, eis aí a palavra corrigida!

A aqruitetura do projeto está dividida em três arquivos principais.
1. `limpa_texto.py` limpa o dataset da Wikipedia, removendo caracteres estranhos ao texto. Para rodar o arquivo, digite no terminal dentro da pasta do projeto:
```
python limpa_texto.py
```
2. `common_words.py` faz mais uma filtragem do vocabulário, e seleciona apenas as 10.000 palavras mais comuns. Para rodar o arquivo, digite:
```
python common_words.py
```
3. `corretor.py` é o programa que lê a frase a ser corrigida, implementa o corretor de Norvig e retorna a frase corrigida. Para rodar o arquivo, digite:
```
python corretor.py
```

Exemplos de testes:
- eu pposso corrigr paavrs
- gotto uito de baquet
- essta mçã é vrmeha
- trablo bemo legau