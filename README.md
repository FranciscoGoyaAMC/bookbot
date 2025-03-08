# BookBot

BookBot é um analisador de texto simples escrito em Python. O programa lê um arquivo de texto, conta o número de palavras e calcula a frequência de caracteres alfabéticos, exibindo os resultados de forma ordenada.

## Funcionalidades

- Contagem do número total de palavras em um texto.
- Contagem da ocorrência de cada caractere alfabético (ignorando diferenciação entre maiúsculas e minúsculas).
- Exibição dos caracteres ordenados por frequência.

## Requisitos

- Python 3.x

## Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/FranciscoGoyaAMC/bookbot.git
   cd bookbot
   ```

2. Execute o programa passando o caminho do arquivo de texto como argumento:
   ```bash
   python3 main.py <caminho_do_arquivo>
   ```
   Exemplo:
   ```bash
   python3 main.py books/sample.txt
   ```

## Exemplo de Saída

```plaintext
============ BOOKBOT ============
Analyzing book found at books/sample.txt...
----------- Word Count ----------
Found 12000 total words
--------- Character Count -------
a: 1024
b: 523
c: 467
...
============= END ===============
```

## Estrutura do Projeto

```
bookbot/
│── main.py        # Arquivo principal do programa
│── stats.py       # Módulo com funções de análise de texto
│── books/         # Diretório opcional para armazenar livros
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou sugerir novos recursos! Basta abrir uma issue ou enviar um pull request.
