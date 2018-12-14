import csv
import pygal
with open('data.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    cnt1, cnt2, cnt3, cnt4, cnt5, cnt6, cnt7, cnt8 = [], [], [], [] , [], [], [], []
    for i in range(4):
        cnt1.append(0), cnt2.append(0), cnt3.append(0), cnt4.append(0), cnt5.append(0),\
        cnt6.append(0), cnt7.append(0), cnt8.append(0)
    for row in csv_reader:
        if row[0][-2:] == "51":
            if row[9] == "ในเมือง":
                cnt1[0] += 1
            if row[9] == "ทางหลวง":
                cnt1[1] += 1
            if row[9] == "ชนบท":
                cnt1[2] += 1
            if row[9] == "ไม่ทราบ":
                cnt1[3] += 1
        elif row[0][-2:] == "52":
            if row[9] == "ในเมือง":
                cnt2[0] += 1
            if row[9] == "ทางหลวง":
                cnt2[1] += 1
            if row[9] == "ชนบท":
                cnt2[2] += 1
            if row[9] == "ไม่ทราบ":
                cnt2[3] += 1
        elif row[0][-2:] == "53":
            if row[9] == "ในเมือง":
                cnt3[0] += 1
            if row[9] == "ทางหลวง":
                cnt3[1] += 1
            if row[9] == "ชนบท":
                cnt3[2] += 1
            if row[9] == "ไม่ทราบ":
                cnt3[3] += 1
        elif row[0][-2:] == "54":
            if row[9] == "ในเมือง":
                cnt4[0] += 1
            if row[9] == "ทางหลวง":
                cnt4[1] += 1
            if row[9] == "ชนบท":
                cnt4[2] += 1
            if row[9] == "ไม่ทราบ":
                cnt4[3] += 1
        elif row[0][-2:] == "55":
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
    from pygal.style import Style
    custom_style = Style(colors=( '#191970', '#000099','#9400D3', '#3366CC',\
    '#8A2BE2', '#FF99CC','#FA8072', '#FF6347'))
    line_chart = pygal.Bar(style=custom_style)
    line_chart.title = 'เส้นทางที่เกิดอุบัติเหตุ'
    line_chart.x_labels = map(str, ["ในเมือง", "ทางหลวง", "ชนบท", "ไม่ทราบ"])
    line_chart.add('ปี 2551', cnt1)
    line_chart.add('ปี 2552', cnt2)
    line_chart.add('ปี 2553', cnt3)
    line_chart.add('ปี 2554', cnt4)
    line_chart.add('ปี 2555', cnt5)
    line_chart.add('ปี 2556', cnt6)
    line_chart.add('ปี 2557', cnt7)
    line_chart.add('ปี 2558', cnt8)
    line_chart.render_to_file('road.svg')

