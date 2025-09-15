def get_word_count(file_contents):
    word_count = 0
    word_list = file_contents.split()
    for words in word_list:
        num = len(word_list)
    print(f"{num} words found in the document")