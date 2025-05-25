from stats import get_no_of_words, get_char_count
from request_book import save_file_content
import os

if os.path.exists("./books/frankenstein.txt"):
    def get_book_text(file_path):
        with open(file_path, 'r', encoding="utf-8") as f: 
            return f.read()

    def main():
        text = get_book_text("./books/frankenstein.txt")
        return get_char_count(text)

    print(main())

else:
    save_file_content()




