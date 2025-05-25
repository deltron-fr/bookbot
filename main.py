from stats import get_no_of_words, get_char_count, sorted_char_list
import os, sys, requests 


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    print("For windows: python main.py <path_to_book>")
    sys.exit(1)


file_path = sys.argv[1]

def save_file_content():
    url = "mtch"
    response = requests.get(url)
    text = response.text

    with open(str(file_path), 'w', encoding='utf-8') as file_write:
        file_write.write(text)

if os.path.exists(file_path):
    def get_book_text(path_to_file):
        with open(path_to_file, 'r', encoding="utf-8") as f: 
            return f.read()

    def main():
        text = get_book_text(file_path)
        num_of_words = get_no_of_words(text)
        char_count = get_char_count(text)
        sorted_list = sorted_char_list(char_count)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}")
        print("----------- Word Count ----------")
        print(f"Found {num_of_words} total words")
        print("--------- Character Count -------")

        for dict in sorted_list:
            if dict['char'].isalpha():
                print(f"{dict['char']}: {dict['num']}")

        print("============= END ===============")

    main()

else:
    save_file_content()




