def get_word_count(file_contents):
    word_count = 0
    word_list = file_contents.split()
    for words in word_list:
        num = len(word_list)
    print(f"Found {num} total words")
def get_letter_count(contents):
        letter_dict = {}
        contents_lowercase = str.lower(contents)
        for letter in contents_lowercase:
             if letter not in letter_dict:
                  letter_dict[letter] = 0
             letter_dict[letter] += 1
        return letter_dict
def sort_on(letters):
     return letters["num"]
def list_conversion(letter_dict):
     letters = []
     for key in letter_dict:
          value = letter_dict[key]
          letters.append({"char" : key, "num" : value})
     letters.sort(reverse=True, key=sort_on)
     return letters
