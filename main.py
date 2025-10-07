from stats import get_num_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text
def main():
  book = get_book_text('books/frankenstein.txt')
  print(f"Found {get_num_words(book)} total words")
  chars = count_characters(book)
  print(chars)

main()


    