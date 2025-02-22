import sys
from stats import count_words, count_char, sort_chars

def get_book_text(filepath):
    #Lê o conteúdo de um arquivo e retorna como texto
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)    



def main():
    #Executa a análise do livro e exibe o relatório.

    # Verifica se o argumento foi passado corretamente
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    num_words = count_words(book_text)
    char_counts = count_char(book_text)
    sorted_chars = sort_chars(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_info in sorted_chars:
        print(f"{char_info['char']}: {char_info['count']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
