def count_words(text):
    return len(text.split())

def count_characters(text):
    text_lower = text.lower()
    set_text = set(text_lower)
    dict_text = dict.fromkeys(set_text, 0)
    for c in text_lower:
        dict_text[c] += 1
    return dict_text

def sort_on(dict):
    return dict["count"]

def sort_dict(char_dict):
    char_list = []
    for k in char_dict:
        char_list.append({"char": k, "count": char_dict[k]})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list