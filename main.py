from stats import *
import sys

def get_book_text(filename):
    file_contents = ""
    with open(filename) as file:
        file_contents = file.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    word_count = count_words(get_book_text(sys.argv[1]))
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    sorted_words = sort_dict(count_characters(get_book_text(sys.argv[1])))
    for c in sorted_words:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["count"]}")
    print("============= END ===============")

main()