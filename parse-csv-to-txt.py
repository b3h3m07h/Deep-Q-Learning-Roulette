import csv

BLACK_NUM =   [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
RED_NUM = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

print(len(RED_NUM) == len (BLACK_NUM))

with open("wizard.csv", 'r') as csvfile:
    datareader = csv.reader(csvfile);
    for row in datareader:
        for r in row:
            if r != '':
                if int(r) == 0 or int(r) == 00:
                    print(r + ' Green')
                    continue
                if (int(r) in BLACK_NUM):
                    print(r + ' Black')
                else:
                    print(r + ' Red')