import sys
from stats import count_book_words

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    book_words_count = count_book_words(book_text)
    book_characters_counter = count_characters(book_text)
    print_report(book_words_count, book_characters_counter, book_path)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def count_characters(book_text):
    counter = {}
    book_text = book_text.lower()
    for char in book_text:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter

def print_report(book_words_count, book_characters_counter, book_path):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_words_count} total words")
    print("--------- Character Count -------")

    list_of_dictionaries = convert_dict_to_sorted_list_of_dicts(book_characters_counter)

    for dict in list_of_dictionaries:
        key = list(dict.keys())[0]
        print(f"'{key}': {dict[key]}")

    print("============= END ===============")

def convert_dict_to_sorted_list_of_dicts(book_characters_counter):
    list_of_dictionaries = []
    for char in book_characters_counter:
        if char.isalpha():
            list_of_dictionaries.append({char:book_characters_counter[char]})

    list_of_dictionaries.sort(key=sort_on, reverse=True)
    return list_of_dictionaries

def sort_on(dict):
    key = list(dict.keys())[0]
    return dict[key]

main()
