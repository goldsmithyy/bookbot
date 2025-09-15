def get_book_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def main():
    from stats import get_word_count
    file_contents = get_book_text("books/frankenstein.txt")
    get_word_count(file_contents)  
main()