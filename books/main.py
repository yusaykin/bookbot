def main():
    book_path = "frankenstein.txt"
    text = get_book_text(book_path)
    text_lowered = text.lower()
    get_num_words(text)
    char_count_1 = char_count(text_lowered)
    chars_sorted_list = chars_dict_to_sorted_list(char_count_1)

    print(f"--- Begin report of {book_path} ---")
    print(f"{get_num_words(text)} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def char_count(input):
    count = {
    }
    for char in input:
        count[char] = count.get(char, 0) + 1
    return count

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list







main()