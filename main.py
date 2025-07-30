from stats import count_words, count_symbol_frequency, create_sorted_list
import sys

def get_book_text(path_to_book):
    with open(path_to_book) as text:
        book = text.read()
        return book

def generate_freq_report(freq_list, word_count, path_to_book):
    print("============ BOOKBOT ============")
    print("Analyzing book found at", path_to_book)
    print("----------- Word Count ----------")
    print("Found", word_count, "total words")
    print("--------- Character Count -------")
    
    for i in range(0, len(freq_list)):
        print(freq_list[i]["char"], ": ", freq_list[i]["num"], sep="")
    

def main():

    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    try:

        path_to_book = sys.argv[1]

        book = get_book_text(path_to_book)
    
        symbol_count = count_symbol_frequency(book)

        sorted_list = create_sorted_list(symbol_count)

        generate_freq_report(sorted_list, count_words(book), path_to_book)

    except Exception as e:
        print(f"Error encountered: {e}")

main()
