#LISTS

# 1. Write a Python program to find the second largest number in a list
def second_largest (list):
    list.sort()
    second_largest = list[1]
    return second_largest

# 2. Write a Python program to check whether a specified list is sorted or not.
def is_sorted (list):
    return all(list[i] <= list[i + 1] for i in range(len(list) - 1))

#3.Write a Python program to check if the elements of a given list are unique or not.
def is_unique (list):
    return len(list) == len(set(list))

#4.Write a Python program to remove all elements from a given list that are present in another list.
def remove_list_from_another (list1, list2):
    return [item for item in list1 if item not in list2]

#5. Write a Python program to check if a substring appears in a given list of string values
def contains_substring(string_list, substring):
    for str in string_list:
        if str in substring:
            return True
    return False

#6. Write a Python program to find all index positions of the maximum and minimum values in a given list of numbers
def min_max_index(list):
    min_value = min(list)
    max_value = max(list)
    min_index = [i for i, x in enumerate(list) if x == min_value]
    max_index = [i for i, x in enumerate(list) if x == max_value]
    return min_index, max_index

#7. Write a Python program to remove specific words from a given list.
def remove_words(word_list, words_to_remove):
    return [word for word in word_list if word not in words_to_remove]

#8. Write a Python program to sort one list based on another list containing the desired indexes.
def sort_list_based_on_indexes(list1, index_list):
    return [list1[i] for i in index_list]

#9. Write a Python program to generate a list containing the Fibonacci sequence, up until the nth term.
def generate_fibonacci(n):
    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

#10. Write a Python program to find an element that divides a given list of integers with the same sum
def find_element_with_equal_sum(lst):
    n = len(lst)
    total = sum(lst)
    for i in lst:
        if total % i == 0:
            left_sum = sum(lst[:n//i])
            right_sum = sum(lst[n//i:])
            if left_sum == right_sum:
                return i
    return None
    
#11. Write a Python program to count the lowercase letters in a given list of words
def count_lowercase_letters(words):
    count = 0
    for word in words:
        for char in word:
            if char.islower():
                count += 1
    return count
