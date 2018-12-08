import csv
import pygal
with open('data.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    cnt1, cnt2, cnt3, cnt4 = [], [], [], []
    for i in range(31):
        cnt1.append(0), cnt2.append(0), cnt3.append(0), cnt4.append(0)
    for row in csv_reader:
        if row[0][-2:] == "51":
            (cnt1[int(row[5])-1]) += 1
        elif row[0][-2:] =="52":
            (cnt2[int(row[5])-1]) += 1
        elif row[0][-2:] =="53":
            (cnt3[int(row[5])-1]) += 1
        elif row[0][-2:] =="54":
            (cnt4[int(row[5])-1]) += 1

    for _ in range(21):
        cnt1.pop(5), cnt2.pop(5), cnt3.pop(5), cnt4.pop(5)
    line_chart = pygal.Bar()
    line_chart.title = 'วันที่เกิดอุบัติเหตุในช่วงเทศกาล ปี 2551 - 2554'
    line_chart.x_labels = map(str, [1, 2, 3, 4, 5, 27, 28, 29, 30, 31])
    line_chart.add('ปี 2551', cnt1)
    line_chart.add('ปี 2552', cnt2)
    line_chart.add('ปี 2553', cnt3)
    line_chart.add('ปี 2554', cnt4)
    line_chart.render_to_file('day_2551-2554.svg')