def read_file (file):
    with open(file, 'r') as f:
        content = f.readlines()
    return content

def pure_words (list):
    ml = [el.strip("(){}[],.0123456789") for el in list]
    return [el for el in ml if el.isalpha()]

  
def word_count(list):
    all_freq = {}
    for i in list:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq



def write_result(filename, dict):
    with open(filename, 'w') as f: 
        for key, value in dict.items(): 
            f.write('%s:%s\n' % (key, value))


def main():

    fname = "a.txt"
    content = read_file(fname)
    words = pure_words(content)
    output_file = "new.txt"
    words.sort()
    count = word_count(words)
    write_result(output_file,count)

main()


