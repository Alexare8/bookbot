import sys
from stats import *

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book = get_book_text(file_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book format at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words.")
    print("--------- Character Count -------")
    report = convert_dictionary(get_num_chars(book))
    for char in report:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

main()