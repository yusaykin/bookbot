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
def sort_on(item):
    return item["num"]
def sorted_char_count(char_counts_dict):
    empty_list = []
    empty_dict = {}
    for char, count in char_counts_dict.items():
        empty_list.append({"char": char, "num": count})

    empty_list.sort(reverse=True, key=sort_on)
    return empty_list



