from stats import get_word_count
from stats import get_letter_count
from stats import list_conversion
import sys
def get_book_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        file_contents = get_book_text(f"{sys.argv[1]}")
        print("----------- Word Count ----------")
        get_word_count(file_contents)  
        letter_count = get_letter_count(file_contents)
        sorted_list = list_conversion(letter_count)
        print("--------- Character Count -------")
        for lists in sorted_list:
            if lists["char"].isalpha() == True:
                print(lists["char"] + ":", lists["num"])
        print("============= END ===============")
main()