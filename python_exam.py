#1. Implement Split function

def split_string(string, separator):   
    words = []
    current_word = ""
    for char in string:
        if char == separator:
            if current_word != "":
                words.append(current_word)
            current_word = ""
        else:
            current_word += char
    if current_word != "":
        words.append(current_word)
    return words



#2. Write a function that returns non repeated unique keys from the dictionary

def unique_keys_from_dict(dict):
    keys_list = list(dict.keys())
    non_repeated_keys = []
    for key in keys_list:
        if keys_list.count(key) == 1:
            non_repeated_keys.append(key)
    return non_repeated_keys

#3. Filter the long word from the list ( long means word =4 or more chars)

def long_word_from_list(words):
    long_words=[]
    for i in words:
        if len(i)>=4:
            long_words.append(i)
    return long_words

def long_words_from_list2 (words):
    long_words = [word for word in words if len(word) >= 4]
    return long_words

def long_words_from_list3 (words):
    long_words = list(filter(lambda x: len(x) >= 4, words))
    return long_words


#Call of the functions
def main():
    long_word_from_list(['elephant', 'lion', 'tiger', 'bird', 'snake'])
    long_words_from_list2(['elephant', 'lion', 'tiger', 'bird', 'snake'])
    long_words_from_list3(['elephant', 'lion', 'tiger', 'bird', 'snake'])

    split_string("Hey there, how are you", " ")
    
  

if __name__ == '__main__':
    main()


    
    



