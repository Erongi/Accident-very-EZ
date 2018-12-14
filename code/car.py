import csv
import pygal

line_chart = pygal.StackedLine(fill=True, width=1200)
line_chart.title = 'ประเภทของรถที่เกิดอุบัติเหตุ'
line_chart.x_labels = map(str, ["รถบรรทุก", "รถเก๋ง/แท็กซี่", "ปิคอัพ", "รถตู้","รถโดยสาร 4 ล้อ",\
"จักรยานยนต์", "สามล้อเครื่อง", "สามล้อถีบ", "รถจักรยาน", "ไม่มี/ล้มเอง", "ไม่ทราบ", "อื่นๆ"])
for i in range(51, 59):
    with open('data.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        cnt1 = []
        for j in range(12):
            cnt1.append(0)
        for row in csv_reader:
            if row[0][-2:] == str(i):
                if row[11] == "รถบรรทุก" :
                    cnt1[0] += 1
                if row[11] == "รถเก๋ง/แท็กซี่" :
                    cnt1[1] += 1
                if row[11] == "ปิคอัพ" :
                    cnt1[2] += 1
                if row[11] == "รถตู้" :
                    cnt1[3] += 1
                if row[11] == "รถโดยสาร 4 ล้อ" :
                    cnt1[4] += 1
                if row[11] == "จักรยานยนต์" :
                    cnt1[5] += 1
                if row[11] == "สามล้อเครื่อง" :
                    cnt1[6] += 1
                if row[11] == "สามล้อถีบ" :
                    cnt1[7] += 1
                if row[11] == "รถจักรยาน" :
                    cnt1[8] += 1
                if row[11] == "ไม่มี/ล้อเอง" :
                    cnt1[9] += 1
                if row[11] == "ไม่ทราบ" :
                    cnt1[10] += 1
                if row[11] == "อื่นๆ" :
                    cnt1[11] += 1
            elif row[0][-2:].isdigit():
                if (int(row[0][-2:]))>i:
                    break
        line_chart.add('ปี 25' + str(i), cnt1)
line_chart.render_to_file('car.svg')

