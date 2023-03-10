#Dict
#1.Write a Python program to find the key of the maximum value in a dictionary
def max_of_dict(dict):
    key_max_value = max(dict, key=dict.get)
    return key_max_value

#2. Write a Python program to transform a dictionary into a list of tuples.
def transform_dict_to_list(dict):
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


def common_adding (dict1, dict2):
    new_dict={}
    for i in dict1.keys():
        for j in dict2.keys():
            if i == j:
                new_dict[i]= dict1[i]+dict2[j]
            else:
                new_dict[i]=dict1[i]

    return (new_dict)


#Write a Python program to get the top three items in a shop.

def top_items(dict):
    top = dict[0]
    top_items={}
    count=0
    while count <3:
        for i in dict.keys():
            if dict[i]>top:
                top_items[i]=dict.valus()
                count+=1
    return top_items


#Write a Python program to sort Counter by value.



            





print(max_of_dict({'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}))
print(transform_dict_to_list({'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}))
print(to_dict(['a', 'b', 'c', 'd', 'e', 'f'],[1, 2, 3, 4, 5]))
print(find_length_of_dict_values({1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}))
print(verify_values_in_dict({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}))
print(print_dict_line_by_line({1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}))
print(sort_list_alphabetically({'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}))
print(sum_dict({'data1':100,'data2':-54,'data3':247}))
print(generate_dictionary(7))
