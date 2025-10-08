from stats import get_num_words, count_characters, sorted_char_count 
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text
def main():
    if len(sys.argv) == 1:
     print("Usage: python3 main.py <path_to_book>")
     sys.exit(1)
    else:
      book_path = sys.argv[1]
      book = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")
    print("------- Character Count ---------")
    my_dict_result = count_characters(book)
    my_sorted_list = sorted_char_count(my_dict_result)
    for character in my_sorted_list:
      if character["char"].isalpha():
        print(f"{character['char']}: {character['num']}")
    print("============= END ===============")




main()


    