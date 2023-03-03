import os
import argparse 

def  read_data_from_file(filename):
    with open(filename, 'r') as file:
        data = file.read().splitlines()

def check_file(filename):
    if not os.path.isfile(filename):
        print ("file not found")
        exit()


def count (list):
    count = 0
    for item in list:
        count += len(item)
    print(count)
   


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, help='input text file name')
    args = parser.parse_args()
    check_file(args.file)
    data = read_data_from_file(args.file)
    count(data)


    

    







