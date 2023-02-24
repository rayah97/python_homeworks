#!/usr/bin/env python3
import argparse 
import xlsxwriter

def read_data_from_file(filename):
    with open(filename, 'r') as file:
        data = file.read().splitlines()
    return [row.split() for row in data]

def create_workbook(data, filename):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    header_format = workbook.add_format({'bold': True, 'bg_color': 'yellow'})
    age_format = workbook.add_format({'bg_color': 'green'})
    header = data[0]
    for i, field in enumerate(header):
        worksheet.write(0, i, field, header_format)


    for i, row in enumerate(data[1:], start=1):
        for j, value in enumerate(row):
            if j == 2 and int(value) < 25:
                worksheet.write(i, j, value, age_format)
            else:
                worksheet.write(i, j, value)
    return workbook


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, help='input text file name')
    parser.add_argument('-o', '--output', required=True, help='output Excel file name')
    args = parser.parse_args()
    data = read_data_from_file(args.file)
    workbook = create_workbook(data, args.output)
    workbook.close()

if __name__ == '__main__':
    main()
