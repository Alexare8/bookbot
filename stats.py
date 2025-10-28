def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    output = {}
    for char in text.lower():
        if char not in output:
            output[char] = 1
        else:
            output[char] += 1
    return output

def sort_on(items):
    return items["num"]

def convert_dictionary(char_counts):
    output = []
    for item in char_counts:
        if item.isalpha():
            output.append({"char": item, "num": char_counts[item]})
    output.sort(reverse=True, key=sort_on)
    return output

