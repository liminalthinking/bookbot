import sys
from stats import get_num_words
from stats import get_char
from stats import sorted_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    file_object = get_book_text(sys.argv[1])
    print("======================BOOKBOT======================")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file_object)} total words.")
    print("----------- Character Count ----------")
    #print(get_char(file_object))
    sorted_dictionaries = sorted_dict(get_char(file_object))
    for item in sorted_dictionaries:
        if item["char"].isalpha() == False:
            continue
        else:
            print(item["char"] + ": " + str(item["num"]))
    print("======================END======================")


main()
