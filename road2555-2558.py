import csv
import pygal
with open('data.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    cnt5, cnt6, cnt7, cnt8 = [], [], [], []
    for i in range(4):
        cnt5.append(0), cnt6.append(0), cnt7.append(0), cnt8.append(0)
    for row in csv_reader:
        if row[0][-2:] == "55":
            if row[9] == "ในเมือง":
                cnt5[0] += 1
            if row[9] == "ทางหลวง":
                cnt5[1] += 1
            if row[9] == "ชนบท":
                cnt5[2] += 1
            if row[9] == "ไม่ทราบ":
                cnt5[3] += 1
        elif row[0][-2:] == "56":
            if row[9] == "ในเมือง":
                cnt6[0] += 1
            if row[9] == "ทางหลวง":
                cnt6[1] += 1
            if row[9] == "ชนบท":
                cnt6[2] += 1
            if row[9] == "ไม่ทราบ":
                cnt6[3] += 1
        elif row[0][-2:] == "57":
            if row[9] == "ในเมือง":
                cnt7[0] += 1
            if row[9] == "ทางหลวง":
                cnt7[1] += 1
            if row[9] == "ชนบท":
                cnt7[2] += 1
            if row[9] == "ไม่ทราบ":
                cnt7[3] += 1
        elif row[0][-2:] == "58":
            if row[9] == "ในเมือง":
                cnt8[0] += 1
            if row[9] == "ทางหลวง":
                cnt8[1] += 1
            if row[9] == "ชนบท":
                cnt8[2] += 1
            if row[9] == "ไม่ทราบ":
                cnt8[3] += 1
    line_chart = pygal.Bar()
    line_chart.title = 'เส้นทางที่เกิดอุบัติเหตุ ปี 2555 - 2558'
    line_chart.x_labels = map(str, ["ในเมือง", "ทางหลวง", "ชนบท", "ไม่ทราบ"])
    line_chart.add('ปี 2555', cnt5)
    line_chart.add('ปี 2556', cnt6)
    line_chart.add('ปี 2557', cnt7)
    line_chart.add('ปี 2558', cnt8)
    line_chart.render_to_file('road_2555-2558.svg')

