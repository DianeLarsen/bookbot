import sys
from stats import count_words, count_characters, char_sorted, char_dict_to_list, final_report


def main():
    file_string = ""
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_string = sys.argv[1]
    def get_book_text():
        with open(sys.argv[1]) as f:
            file_contents = f.read()
        return file_contents
    file_as_string = get_book_text()
    word_count = count_words(file_as_string)
    char_count = count_characters(file_as_string)
    char_dict = char_dict_to_list(char_count)
    sorted_dict = char_sorted(char_dict)
    final_report(file_string, word_count, sorted_dict)
main()