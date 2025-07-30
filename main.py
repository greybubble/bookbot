from stats import count_words, count_symbol_frequency, create_sorted_list

def get_book_text(path_to_book):
    with open(path_to_book) as text:
        book = text.read()
        return book

def main():

    path_to_frank = "books/frankenstein.txt"

    frankenstein = get_book_text(path_to_frank)
    print(count_words(frankenstein), "words found in the document")
    
    symbol_count = count_symbol_frequency(frankenstein)

    # print(symbol_count)

    sorted_list = create_sorted_list(symbol_count)

    print(sorted_list)

main()
