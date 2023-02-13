
# 1. Գրել ֆունկցիա որը կվերդարձնի ստացած արգումենտներից թվերի գումարը։
def sum_of_args(*args):
    return sum(arg for arg in args if str(arg).isdigit())

# 2.  Գրել ֆունկցիա որը կվերդարձնի ստացած արգումենտներից տողերի քանակը։
def count_of_strings(*args):
    return sum(1 for arg in args if isinstance(arg, int))

# 3. , Գրել ֆունկցիա որը կվերադարձնի ստասած արգումենտների միջին թվաբանականը։
def avarage_of_args(*args):
    return sum([arg for arg in args if isinstance(arg, int)]) / len([arg for arg in args if type(arg) == int]) 

# 4. Գրել ֆունկցիա որը կստանա արգումենտ և կվերադարձնի այդ
# արգումենտերի հետ կատարած մաթեմատիկական գործողությունների արդյունքները։
def arithmetics(*args):
    sum_result = sum(args)
    mult_result = 1
    for arg in args:
        mult_result *= arg

    differences = []
    for i in range(len(args)):
        for j in range(i+1, len(args)):
            differences.append(args[i] - args[j])
  
    divisions = []
    for i in range(len(args)):
        for j in range(i+1, len(args)):
            if args[j] != 0:
                divisions.append(args[i] / args[j])
  
    return sum_result, mult_result, differences, divisions


# 5. Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնի
# այն դարձված ամբողջությամբ մեծատառ ֆունկցիան օգտագործել չի (upper կարելի ։)
def to_uppercase(string):
    return ''.join([chr(ord(c) - 32) if ord(c) in range(97, 123) else c for c in string])

# 6. Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնի
# այն դարձված ամբողջությամբ փոքրատառ ֆունկցիան օգտագործել չի (lower կարելի ։)
def to_lowercase(s):
    return ''.join([chr(ord(c) + 32) if ord(c) in range(65, 91) else c for c in s])

# 7. Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնի
# այն դարձված բոլոր բառերի առաջին տառերը մեծատառ ֆունկցիան (title օգտագործել չի կարելի ։ )
def title_to_upper(string):
    words = string.split()
    capitalized_words = [word[0].upper() + word[1:] for word in words]
    return ' '.join(capitalized_words)

# 8. Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնի այն դարձված հակառակ։
def string_reversed(str):
    return str[::-1]

# 9. Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և թիվ։ Այն պետք է 
# վերադարձնի տրված թվերի արանքում եղած ենթատողը։ 
def mid_string(str, num1, num2):
    return str[num1:num2]

# 10. Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաերկար բառը։
def longest_word_sentence(mstr):
    new_list = mstr.split()
    sorted_list = sorted(new_list, key=lambda x: len(x), reverse=True)
    return sorted_list[0]
    
# 11. Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաշատ
# օգտագործված տառը։
def most_used_letter(sentence):
    sentence = sentence.lower()
    letter_counts = {}
    for letter in sentence:
        if letter.isalpha():
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1

    return max(letter_counts, key=letter_counts.get)

# 12. Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաերկար բառում ամենաշատ օգտագործված տառը։
def most_used_letter_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len).lower()

    letter_counts = {}
    for letter in longest_word:
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return max(letter_counts, key=letter_counts.get)

# 13. Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և թիվ։
# Կվերադարձնի այդ թվին համապատասխն ինդեքսում եղած էլէմենտները՝ սկզբից և վերջից։
def string_with_index(string, index):
    return string[index] + string[-index]

# 15․ Գրել ֆունկցիա որը որպես արգումենտ կստանա թիվ և կստուգի
# պոլինդրոմ է այն թե ոչ։ 
def num_is_polindrom(num):
    return str(num)==str(num)[::-1]

# 16․ Գրել ֆունկցիա որը որպես արգումենտ կստանա թիվ և կվերադարձնի
# իրեն ամենամոտ պոլինդրոմ թիվը։
def closest_palindrome(n):
    def num_is_polindrom(num):
        return str(num) == str(num)[::-1]

    if num_is_polindrom(n):
        return n

    left = n - 1
    right = n + 1

    if num_is_polindrom(left):
        return left

    return closest_palindrome(right)

# 17․ Գրել ֆունկցիա որը որպես արգումենտ կստանա թիվ և կվերադարձնի իր
# առաջին և վերջին թվանշանների արտադրյալը։
def mult_of_index(num):
    num_str = str(num)
    return int(num_str[0]) * int(num_str[-1])

# 18.Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի
# լիստում եղած տողերի քանակությունը։
def string_count_list(list):
    return sum(1 for el in list if isinstance(el, str))

# 19. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի
# լիստում առկա թվերից առավելագույնը։
def max_list(list):
   return max(el for el in list if isinstance(el, int))           

# 20. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի
# այդ լիստում առկա երկնիշ զույգ թվերը։
def even_list (list):
    return [el for el in list if isinstance(el, int) and 9 < el < 100 and el % 2 == 0]

# 21. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի այդ լիստում առկա թվերի միջին թվաբանականը։
def list_average(lst):
    total = sum(el for el in lst if isinstance(el, int))
    count = len([el for el in lst if isinstance(el, int)])
    return total / count if count != 0 else None
    
# 22. Գրել ֆունկցիա որը որպես առգումենտ կստանա տողերի լիստ և
# կվերադարձնի այդ տողերի երկարությունները պարունակող լիստ։
def len_list(list):
    return [len(el) for el in list]

# 23. , Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի
# լիստում առկա թվերը դասավորված նվազման կարգով։ 
def sorted_numbers(list):
    return sorted([el for el in list if isinstance(el, int)], reverse=True)

# 24. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի
# լիստում առկա տողերը դասավորված երկարությունների նվազման կարգով։
def len_list_desc(list):
    return sorted([len(el) for el in list if isinstance(el, str)])

# 25. Գրել ֆունկցիա որը որպես արգումենտ կընդունի կընդունի տողերի լիստ
# և կվերադարձնի այն բառը որը կպարունակի ամենաշատ ձայնավորները։ 
def words_with_most_vowels(words):
    vowels = "AEIOUaeiou"
    max_vowels = 0
    most_vowel_words = []
    for word in words:
        num_vowels = sum(char in vowels for char in word)
        if num_vowels > max_vowels:
            max_vowels = num_vowels
            most_vowel_words = [word]
        elif num_vowels == max_vowels:
            most_vowel_words.append(word)
    return most_vowel_words

# 26. Գրել ֆունկցիա որը որպես արգումենտ կընդունի նախադասությունների
# լիստ և կվերադարձնի այն նախադասությունը որը կպարունակի 
# ամենաշատ բառերը։
def longest_sentence(sentences):
    longest = ""
    for sentence in sentences:
        if len(sentence) > len(longest):
            longest = sentence
    return longest

# 27. Գրել ֆունկցիա որը որպես արգումենտ կստանա տող իրականում
# նախադասություն և կվերադարձնի այդ նախադասությունում առկա 
# ամենամեծ թիվը ոչ թե թվանշանը 
# 28. Գրել ֆունկցիա որը որպես արգումենտ կստանա բառարանների լիստ՝
# մարդկանց նկարագրող և կվերադարձնի այն բառարանը որում մարդու , ,
# տարիքն ամենամեծն է։
def biggest_age(people):
    biggest = {}
    max_age = 0
    for person in people:
        for name, age in person.items():
            if age > max_age:
                max_age = age
                biggest = {name: age}
    return biggest

# 29. Գրել ֆունկցիա որը որպես արգումենտ կստանա բառարանների լիստ՝
# ուսանողների նկարագրող և կվերադարձնի այդ ուսանողների լիստը
# դասավորված աճման կարգով՝ ըստ միասվորների։
def sort_students_by_points(students):
    return sorted(students, key=lambda x: x['points'])

# 30. Գրել ֆունկցիա որը որպես արգումենտ կստանա բառարանների լիստ՝
# համալսարանների նկարագրող և կվերադարձնի այն համալսարանը որի ,
# անվանումն ամենաերկարն է։ 
def longest_university_name(university_list):
    longest_university = ""
    max_length = 0
    for university in university_list:
        if len(list(university.values())[0]) > max_length:
            longest_university = list(university.values())[0]
            max_length = len(list(university.values())[0])
    return longest_university


print(sum_of_args(1, 7, 444, "hello"))
print(count_of_strings(6,44,"hello","hh",77,"nksjd"))
print (avarage_of_args(6,44,"hello","hh",77,"nksjd"))
print(string_reversed("Lena"))
print(mid_string("HelloThere", 3,6))
print(longest_word_sentence("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"))
print (even_list([1,3,6,99,77,66,44,3,86,4,"hello", 60,111]))
print(list_average([1,3,6,99,77,66,44,3,86,4,"hello", 60,111]))
print(max_list([1,3,6,99,77,66,44,3,86,4,"hello", 60,111]))
print(len_list(["apple", "banana", "cherry"]))
print(sorted_numbers([1,3,6,99,77,66,44,3,86,4,"hello", 60,111]))
print(len_list_desc([1,3,6,99,77,66,4,"hello", 60,111,"hi","sup", "apple", "banana", "cherry"]))
print(num_is_polindrom(454))
print(num_is_polindrom(451))
print(mult_of_index(7782))
print(string_with_index("hanrapetutyun",2))
print(string_count_list([1,3,6,99,77,66,4,"hello", 60,111,"hi","sup", "apple", "banana", "cherry"]))
print(arithmetics(4,5,6))
print(to_uppercase("hello"))
print(to_lowercase("HelLo"))
print(title_to_upper("Hello dhdfgjsh skdjfhkdsj there"))
print(longest_sentence(["This is sentence 1.", "This is a longer sentence that sentence 1.", "Sentence 3 is even longer than sentence 2."]))
print(words_with_most_vowels("Hello dhdfgjsh skdjfhkdsj there"))
print(biggest_age([{"John": 30}, {"Jane": 25}, {"Bob": 40}]))
print (sort_students_by_points([{'name': 'John', 'points': 90}, {'name': 'Jane', 'points': 80},{'name': 'Jim', 'points': 95}]))
print(longest_university_name([{"univer1": "ASUEGB"},{"univer2": "Politechnic"},{"univer3": "Mankavarjakan"}]))
print(closest_palindrome(431))