#Write a Python program to generate a list of numbers in the arithmetic
# progression starting with the given positive integer and up to the specified limit.
def arith_list (start,end, iteration):
    ar_list = []
    ar_list[0]=start
    for i in range (1,end):
        ar_list[i]=ar_list[i-1]+iteration 
    return ar_list

#Write a Python program to sum the missing numbers in a given list of integers.

def sum_missing_numbers(nums):
    start = min(nums)
    end = max(nums)
    return sum(range(start, end+1)) - sum(nums)
        
 #Write a Python program to check if the elements of the first list are contained in the second one regardless of order. 

def contains_list(list1,list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.issubset(set2)


