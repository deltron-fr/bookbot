
def get_no_of_words(text):
    num_of_words = len(text.split())
    return num_of_words

def get_char_count(text):
    char_dict = {}
    for char in text.lower(): 
        if char not in char_dict:
            char_dict[char] = 0
    
    for char in text.lower():
        char_dict[char] += 1

    return char_dict


def sorted_char_list(char_dict): 
    def sort_on(dict):
        return dict["num"]
    
    dict_list = []
    for char, count in char_dict.items():
        dict_list.append({"char": char, "num": count})

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

