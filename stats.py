
def count_words(text):
    book = text.split()
    return len(book)

def count_symbol_frequency(text):
    book = text.lower()
    frequency = {}

    for symbol in book:
        if(symbol in frequency):
            frequency[symbol] += 1
        else:
            frequency[symbol] = 1

    return frequency
