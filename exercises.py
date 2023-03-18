ml = [1,2,3,"1","4",[1,2,3]]
    
def sum_integers(ml):
    total = 0
    for element in ml:
        try:
            total += int(element)
        except (ValueError, TypeError):
            if isinstance(element, list):
                total += sum_integers(element)
    return total


sum_integers(ml)

#string input - hashvel tarery


def count_letters(str):
    letter_count = {}
    for letter in str:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count


#naxadasutyun, erkar bareri qanak 4+ words


def words(str):
    count = 0
    lst = str.split()
    for i in lst:
        if i.length()>4:
            count+=1


