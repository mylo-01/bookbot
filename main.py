import sys
from stats import get_num_words, get_character_dictionary, format_char_dic

def get_book_text(filepath):
    with open(filepath) as frankenstein_book:
        return (frankenstein_book.read())

def main():
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        text = get_book_text(filepath)
        num_words = get_num_words(text)
        #get_character_dictionary(text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        print(format_char_dic(get_character_dictionary(text)))
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()