import sys
from stats import get_num_of_words, get_book_text, get_character_count, sort_characters_by_count, formatted_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    try:
        with open(book_path) as f:
            text = get_book_text(f)
            num_of_words = get_num_of_words(text)
            character_count = get_character_count(text)
            sorted_characters = sort_characters_by_count(character_count)
            formatted_report(book_path, num_of_words, sorted_characters)
    except FileNotFoundError:
        print(f"Error: The file '{book_path}' was not found.")
        sys.exit(1)

main()