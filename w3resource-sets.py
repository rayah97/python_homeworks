#Sets
#1.Write a Python program to create set difference.
def set_difference(set1, set2):
    return set1 - set2

#2. Write a Python program to find elements in a given set that are not in another set.
def find_elements_not_in_set(set1, set2):
    result = []
    for item in set1:
        if item not in set2:
            result.append(item)
    return result

#3.Write a Python program to check if two given sets have no elements in common
def no_common_elements(set1, set2):
  for element in set1:
    if element in set2:
      return False
  return True

#4. Write a Python program to check if a given value is present in a set or not.
def is_value_in_set(value, set):
    return value in set


#5. Write a Python program to remove item(s) from a given set. 
def remove_item(my_set, items_to_remove):
  for item in items_to_remove:
    if item in my_set:
      my_set.remove(item)
  return my_set

#6.  Write a Python program to find the maximum and minimum values in a set.
def find_min_max(set):
    s = list(set)
    return (min(s), max(set))

#7.Write a Python program to remove an item from a set if it is present in the set.
def remove_item_from_set(s, item):
    if item in s:
        s.remove(item)
    return s


print(set_difference(["green", "blue"],["blue", "yellow"]))
print(find_elements_not_in_set(["green", "blue"],["blue", "yellow"]))
print(no_common_elements(["green", "blue"],["blue", "yellow"]))
print(is_value_in_set("blue",["green", "blue"]))
print(remove_item([0, 1, 3, 4, 5],"5"))