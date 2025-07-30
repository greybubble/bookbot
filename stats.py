
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

def sort_on(items):
    return items["num"]

def create_sorted_list(dict):
    sorted_list = []
    for entry in dict:
        if(entry.isalpha()):
            char_count = {}
            char_count["char"] = entry
            char_count["num"] = dict[entry]
        
            sorted_list.append(char_count)

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
        