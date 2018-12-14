import csv
import pygal
with open('data.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    cnt1, cnt2, cnt3, cnt4, cnt5, cnt6, cnt7, cnt8 = [], [], [], [], [], [], [], []
    for i in range(31):
        cnt1.append(0), cnt2.append(0), cnt3.append(0), cnt4.append(0), cnt5.append(0),\
        cnt6.append(0), cnt7.append(0), cnt8.append(0)
    for row in csv_reader:
        if row[0][-2:] == "51":
            (cnt1[int(row[5])-1]) += 1
        elif row[0][-2:] =="52":
            (cnt2[int(row[5])-1]) += 1
        elif row[0][-2:] =="53":
            (cnt3[int(row[5])-1]) += 1
        elif row[0][-2:] =="54":
            (cnt4[int(row[5])-1]) += 1
        elif row[0][-2:] =="55":
            (cnt5[int(row[5])-1]) += 1
        elif row[0][-2:] =="56":
            (cnt6[int(row[5])-1]) += 1
        elif row[0][-2:] =="57":
            (cnt7[int(row[5])-1]) += 1
        elif row[0][-2:] =="58":
            (cnt8[int(row[5])-1]) += 1
    for _ in range(21):
        cnt1.pop(5), cnt2.pop(5), cnt3.pop(5), cnt4.pop(5), cnt5.pop(5),\
        cnt6.pop(5), cnt7.pop(5), cnt8.pop(5)
    from pygal.style import Style
    custom_style = Style(colors=( '#A0522D','#FF0000', '#FF4500', '#FFA500',\
    '#FFFF33', '#CCFF00', '#66FF66', '#66FFFF'))
    line_chart = pygal.StackedBar(style=custom_style)
    line_chart.title = 'วันที่เกิดอุบัติเหตุในช่วงเทศกาล'
    line_chart.x_labels = map(str, [1, 2, 3, 4, 5, 27, 28, 29, 30, 31])
    line_chart.add('ปี 2551', cnt1)
    line_chart.add('ปี 2552', cnt2)
    line_chart.add('ปี 2553', cnt3)
    line_chart.add('ปี 2554', cnt4)
    line_chart.add('ปี 2555', cnt5)
    line_chart.add('ปี 2556', cnt6)
    line_chart.add('ปี 2557', cnt7)
    line_chart.add('ปี 2558', cnt8)
    line_chart.render_to_file('day.svg')