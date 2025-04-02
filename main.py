from stats import get_num_of_words, get_book_text, get_character_count


def main():

    with open("books/frankenstein.txt") as f:
        text = get_book_text(f)
        num_of_words = get_num_of_words(text)
        character_count = get_character_count(text)

        print(f"There are {num_of_words} words in this text "
              f"and each unique character and its count are listed here! \n{character_count}")

main()