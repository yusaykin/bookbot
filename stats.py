def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_characters(book):
    lowercase_book = book.lower()
    char_count = {}
    for b in lowercase_book:
        if b in char_count:
            char_count[b] += 1
        else:
            char_count[b] = 1
    return char_count 



