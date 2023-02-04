#Dict

#1.Write a Python program to find the key of the maximum value in a dictionary
def max_of_dict(dict):
    key_max_value = max(dict, key=dict.get)
    return key_max_value

#2. Write a Python program to transform a dictionary into a list of tuples.
def transform_dict_to_list (dict):
    list_of_tuples = list(dict.items())
    return list_of_tuples


#3.Write a Python program to combine two lists into a dictionary. The elements of the first one serve as keys and the elements of the second one serve as values. Each item in the first list must be unique and hashable.
def to_dict(list1,list2):
    dictionary = {list1[i]: list2[i] for i in range(len(list1))}     
    return dictionary   

#4. Write a Python program to find the length of a dictionary of values.
def find_length_of_dict_values(dictionary):
    length_of_values = {}
    for value in dictionary.values():
        length_of_values[value] = len(value)
    return length_of_values

#5.Write a Python program to verify that all values in a dictionary are the same
def verify_values_in_dict(dictionary):
    values = list(dictionary.values())
    return len(set(values)) == 1

#6.Write a Python program to print a dictionary line by line.
def print_dict_line_by_line(dictionary):
    for key, value in dictionary.items():
        print(key, ":", value)

#7. Write a Python program to sort a list alphabetically in a dictionary.
def sort_list_alphabetically(dictionary):
    for key, value in dictionary.items():
        dictionary[key] = sorted(value)
    return dictionary

#8. Write a Python program to sort a given dictionary by key.
def sort_dict_by_key(dictionary):
    return dict(sorted(dictionary.items()))

#9. Write a Python program to sum all the items in a dictionary.
def sum_dict(dict):
    return sum(dict.values())

#10.Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
def generate_dictionary(n):
    d = {}
    for i in range(1, n+1):
        d[i] = i*i
    return d