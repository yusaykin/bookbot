def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text
def main():
  book = get_book_text('books/frankenstein.txt')
  print(book)
    
    

main()
    