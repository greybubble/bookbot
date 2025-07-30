from stats import count_words, count_symbol_frequency

def get_book_text(path_to_book):
    with open(path_to_book) as text:
        book = text.read()
        return book

def main():

    frankenstein = get_book_text("books/frankenstein.txt")
    print(count_words(frankenstein), "words found in the document")
    
    symbol_count = count_symbol_frequency(frankenstein)

    symbol_count = dict(sorted(symbol_count.items()))

    print(symbol_count)

main()
