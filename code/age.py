import csv
import pygal

pie_chart = pygal.Line()
pie_chart.title = 'อายุของผู้เกิดอุบัติเหตุ'
pie_chart.x_labels = map(str, ["91 - 100 ปี", "81 - 90 ปี", "71 - 80 ปี",\
    "61 - 70 ปี", "51 - 60 ปี", "41 - 50 ปี", "31 - 40 ปี", "21 - 30 ปี", "11 - 20 ปี", "0 - 10 ปี"])
for i in range(51, 59):
    with open('data.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        cnt1 = []
        for j in range(10):
            cnt1.append(0)
        for row in csv_reader:
            if row[0][-2:] == str(i):
                if 91 <= int(row[8]) <= 100 :
                    cnt1[0] += 1
                if 81 <= int(row[8]) <= 90 :
                    cnt1[1] += 1
                if 71 <= int(row[8]) <= 80 :
                    cnt1[2] += 1
                if 61 <= int(row[8]) <= 70 :
                    cnt1[3] += 1
                if 51 <= int(row[8]) <= 60 :
                    cnt1[4] += 1
                if 41 <= int(row[8]) <= 50 :
                    cnt1[5] += 1
                if 31 <= int(row[8]) <= 40 :
                    cnt1[6] += 1
                if 21 <= int(row[8]) <= 30 :
                    cnt1[7] += 1
                if 11 < int(row[8]) <= 20 :
                    cnt1[8] += 1
                if 0 <= int(row[8]) <= 10 :
                    cnt1[9] += 1
            elif row[0][-2:].isdigit():
                if (int(row[0][-2:]))>i:
                    break
        pie_chart.add('ปี 25' + str(i), cnt1)

pie_chart.render_to_file('age.svg')

