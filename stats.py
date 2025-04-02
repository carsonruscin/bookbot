

def get_book_text(filepath):
    file_contents = filepath.read()
    return file_contents

def get_num_of_words(book_text):
    words = book_text.split()
    return len(words)

def get_character_count(book_text):
    count_dict = {}

    for char in book_text:
        lowercase_char = char.lower()
        if lowercase_char in count_dict:
            count_dict[lowercase_char] += 1
        else:
            count_dict[lowercase_char] = 1

    return count_dict