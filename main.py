from stats import count_book_words

def main():
    book_path = "books/frankenstein.txt"
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
    print(f"--- Begin report of {book_path} ---")
    print(f"{book_words_count} words found in the document\n\n")

    list_of_dictionaries = convert_dict_to_sorted_list_of_dicts(book_characters_counter)

    for dict in list_of_dictionaries:
        key = list(dict.keys())[0]
        print(f"The '{key}' character was found {dict[key]} times")

    print("--- End report ---")

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
