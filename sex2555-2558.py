import csv
import pygal
with open('data.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    cnt5, cnt6, cnt7, cnt8 = [], [], [], []
    for i in range(2):
        cnt5.append(0), cnt6.append(0), cnt7.append(0), cnt8.append(0)
    for row in csv_reader:
        if row[0][-2:] == "55":
            if row[7] == "ชาย":
                cnt5[0] += 1
            if row[7] == "หญิง":
                cnt5[1] += 1
        elif row[0][-2:] == "56":
            if row[7] == "ชาย":
                cnt6[0] += 1
            if row[7] == "หญิง":
                cnt6[1] += 1
        elif row[0][-2:] == "57":
            if row[7] == "ชาย":
                cnt7[0] += 1
            if row[7] == "หญิง":
                cnt7[1] += 1
        elif row[0][-2:] == "58":
            if row[7] == "ชาย":
                cnt8[0] += 1
            if row[7] == "หญิง":
                cnt8[1] += 1
    line_chart = pygal.Bar()
    line_chart.title = 'เพศของบุคคลที่เกิดอุบัติเหุ ปี 2555 - 2558'
    line_chart.x_labels = map(str, ["ชาย", "หญิง"])
    line_chart.add('ปี 2555', cnt5)
    line_chart.add('ปี 2556', cnt6)
    line_chart.add('ปี 2557', cnt7)
    line_chart.add('ปี 2558', cnt8)
    line_chart.render_to_file('sex_2555-2558.svg')

