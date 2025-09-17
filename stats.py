
def count_words(text_string):
    return len(text_string.split())

def count_characters(text_string):
    char_count = {}
    for i in text_string.lower():
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count

def char_dict_to_list(char_list):
    char_dict_list = []
    for i in char_list:
        new_dict = {}
        new_dict["char"] = i
        new_dict["num"] = char_list[i]
        char_dict_list.append(new_dict)
    return char_dict_list

def sort_on(items):
    return items["num"]

def char_sorted(char_dict):
    char_dict.sort(reverse=True, key=sort_on)
    return char_dict

def final_report(file_path, words_count, chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for i in chars:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")