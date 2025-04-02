def get_book_text(filepath):
    file_contents = filepath.read()
    return file_contents

def get_num_of_words(book_text):
    words = book_text.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        text = get_book_text(f)
        num_of_words = get_num_of_words(text)

        print(f"{num_of_words} words found in the document")



main()