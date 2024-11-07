import re


def count_characters(text: str):
    cleaned_text_list = [char for char in list(text.lower()) if char != ' ']
    count = dict()
    for char in cleaned_text_list:
        if re.match(r'^[a-zA-Z]$', char):
            if char in count.keys():
                count[char] += 1
            else:
                count[char] = 1
    sorted_char_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_char_count.items():
        print(f"the {key} character  was found {value} times")
    print("--- End report ---")
    return count


with open('books/frankenstein.txt') as f:
    file_contents=f.read()
    words=file_contents.split()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")
    dict_count = count_characters(file_contents)

