def main():
    book_path = "books/frankenstein.txt"

    # read file
    text = get_book_text(book_path)

    word_count = get_num_words(text)

    # built dict of all characters
    character_dict = get_chars_dict(text)

    # convert char dict into list of dicts of each char and count
    character_list = chars_dict_to_sorted_list(character_dict)

    # print report
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")

    for char in character_list:
        character = char["character"]
        count = char["count"]
        print(f"The \'{character}\' character was found {count} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(dict):
    return dict["count"]


def chars_dict_to_sorted_list(dict):
    character_list = []
    for char in dict:
        if char.isalpha():
            char_dict = {}
            char_dict["character"] = char
            char_dict["count"] = dict[char]
            character_list.append(char_dict)   
    character_list.sort(reverse=True, key=sort_on)
    return character_list


def get_chars_dict(text):
    character_dict = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char not in character_dict:
            character_dict[lowered_char] = 1
        else:
            character_dict[lowered_char] += 1
    return character_dict


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


main()