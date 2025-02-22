def count_words(book_text):
    #Conta o número de palavras no texto
    words = book_text.split()
    return len(words)


def count_char(book_text):
    #Conta o número de cada caractere no texto
    chars = {}
    text = book_text.lower()
    for char in text:
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

    return chars

def sort_on(char_dict):
    return char_dict['count']


def sort_chars(count_char):
    char_list = [{'char': char, 'count': count} for char, count in count_char.items()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list

