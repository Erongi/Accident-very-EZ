import csv
import pygal
with open('data.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    cnt5, cnt6, cnt7, cnt8 = [], [], [], []
    for i in range(31):
        cnt5.append(0), cnt6.append(0), cnt7.append(0), cnt8.append(0)
    for row in csv_reader:
        if row[0][-2:] =="55":
            (cnt5[int(row[5])-1]) += 1
        elif row[0][-2:] =="56":
            (cnt6[int(row[5])-1]) += 1
        elif row[0][-2:] =="57":
            (cnt7[int(row[5])-1]) += 1
        elif row[0][-2:] =="58":
            (cnt8[int(row[5])-1]) += 1

    for _ in range(21):
        cnt5.pop(5), cnt6.pop(5), cnt7.pop(5), cnt8.pop(5)
    line_chart = pygal.Bar()
    line_chart.title = 'วันที่เกิดอุบัติเหตุในช่วงเทศกาล ปี 2555 - 2558'
    line_chart.x_labels = map(str, [1, 2, 3, 4, 5, 27, 28, 29, 30, 31])
    line_chart.add('ปี 2555', cnt5)
    line_chart.add('ปี 2556', cnt6)
    line_chart.add('ปี 2557', cnt7)
    line_chart.add('ปี 2558', cnt8)
    line_chart.render_to_file('day_2555-2558.svg')
    
