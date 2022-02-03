
'''
    csv 모듈로 파일 읽기
'''

import csv



with open('test.csv', 'r', newline='') as file:
    # reader(파일객체, delimiter(구분기호), quotechar(문자열기호))
    csv_reader = csv.reader(file, delimiter=',', quotechar='"')
    for line in csv_reader:
        print(line)

