
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

def sort_characters_by_count(character_counts):
    char_list = []
    for char, count in character_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})

    def get_count(item):
        return item["count"]

    char_list.sort(reverse=True, key=get_count)
    return char_list

def formatted_report(book_path, word_count, sorted_char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count ---------")
    for item in sorted_char_list:
        print(f"{item['char']}: {item['count']}")
    print("============= END =============")