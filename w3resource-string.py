#STRING
#1.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
def change_occurrences(s):
    first_char = s[0]
    modified_string = first_char + s[1:].replace(first_char, '$')
    return modified_string

#2.Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
def swap_and_concatenate(a, b):
    a_swapped = b[:2] + a[2:]
    b_swapped = a[:2] + b[2:]
    return a_swapped + ' ' + b_swapped

#3. Write a Python function that takes a list of words and return the longest word and the length of the longest one
def find_longest_word(words_list):
    longest_word = ""
    max_length = 0
    for word in words_list:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    return (longest_word, max_length)

#4. Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
def sort_distinct_words(words):
    words_list = words.split(',')
    unique_words = sorted(set(words_list))
    return(','.join(unique_words))

#5. Write a Python function to insert a string in the middle of a string. 
def insert_string_middle(string, insert):
    mid = len(string) // 2
    return string[:mid] + string + string[mid:]
    
#6. Write a Python program to find string similarity between two given strings
def srtings_similarity(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    return len(set1 & set2) / len(set1 | set2)

#7.  Write a Python program to extract numbers from a given string
def wrap_text(string, width):
    lines = []
    line = ""
    words = string.split()
    for word in words:
        if len(line) + len(word) <= width:
            line += word + " "
        else:
            lines.append(line)
            line = word + " "
    lines.append(line)
    return "\n".join(lines)

#8. Write a Python program to find the longest common sub-string from two given strings.
def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    result = 0
    end = 0
    length = [[0 for x in range(n+1)] for y in range(m+1)]
    for i in range(m):
        for j in range(n):
            if str1[i] == str2[j]:
                length[i+1][j+1] = length[i][j] + 1
                if length[i+1][j+1] > result:
                    result = length[i+1][j+1]
                    end = i + 1
    return str1[end-result:end]

#9. Write a Python program to split a string on the last occurrence of the delimiter.
def split_on_last(string, delimiter):
    parts = string.rsplit(delimiter, 1)
    if len(parts) == 1:
        return parts[0], ""
    return parts[0], parts[1]


#10.Write a Python program to lowercase the first n characters in a string. 
def lowercase_first_n_chars(string, n):
    return string[:n].lower() + string[n:]


print (lowercase_first_n_chars("HOLAAMIgsdvsjh",4))
print (split_on_last("w,3,r,e,s,o,u,r,c,e",2))
print (longest_common_substring("abcdefgh","xswerabcdwd"))
print (wrap_text("ed 12 black 45 green"),3)
print (srtings_similarity("Python Exercises", "Python Exercisess"))
print (insert_string_middle('{{}}', 'PHP'))
print (sort_distinct_words('red, white, black, red, green, black'))
print (find_longest_word('red, white, black, red, green, blackfsdfdsf'))
print (swap_and_concatenate('abc', 'xyz'))
print (change_occurrences("restart"))
