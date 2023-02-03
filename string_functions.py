def custom_strip(string):
    start = 0
    end = len(string) - 1
    while start <= end and string[start] == ' ':
        start += 1
    while end >= start and string[end] == ' ':
        end -= 1
    return string[start:end + 1]



def custom_split(string, delimiter):
    words = []
    word = ""
    for char in string:
        if char == delimiter:
            words.append(word)
            word = ""
        else:
            word += char
    words.append(word)
    return words



def to_uppercase(string):
    result = ''
    for char in string:
        if char >= 'a' and char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result


def to_lowercase(string):
    result = ""
    for char in string:
        if ord(char) >= 65 and ord(char) <= 90:
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def replace_string(string, old, new):
    result = ""
    n = len(old)
    i = 0
    while i < len(string):
        if string[i:i+n] == old:
            result += new
            i += n
        else:
            result += string[i]
            i += 1
    return result


def find_substring(string, target):
    n = len(target)
    for i in range(len(string) - n + 1):
        if string[i:i+n] == target:
            return i
    return -1


def count_substring(string, substring):
    count = 0
    for i in range(len(string) - len(substring) + 1):
        found = True
        for j in range(len(substring)):
            if string[i + j] != substring[j]:
                found = False
                break
        if found:
            count += 1
    return count


def is_digit(string):
    for char in string:
        if char < '0' or char > '9':
            return False
    return True


def is_alpha(string):
    for char in string:
        if ord(char) < 65 or (90 < ord(char) < 97) or ord(char) > 122:
            return False
    return True

def find_index(string, substring):
    for i in range(len(string) - len(substring) + 1):
        found = True
        for j in range(len(substring)):
            if string[i + j] != substring[j]:
                found = False
                break
        if found:
            return i
    return -1



print(custom_strip("  Hello, World!  "))
print (custom_split("hello,world", ","))
print (to_uppercase("Rayah"))
print (to_lowercase ("HELLO"))
print (replace_string (" Hello moon", "moon", "sun"))
print (find_substring("Hello my dear dear friend", "dear"))
print (is_digit("hello"))
print (is_alpha("hello"))
print (find_index("hello, world", "ll"))
print (count_substring("hello, world, world", "world"))


