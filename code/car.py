import csv
import pygal

pie_chart = pygal.Line(width=1200)
pie_chart.title = 'เวลาที่เกิดอุบัติเหตุ'
pie_chart.x_labels = map(str, ["24:01-02:00 น.", "02:01-04:00 น.", "04:01-06:00 น.", "06:01-08:00 น.",\
        "08:01-10:00 น.","10:01-12:00 น.", "12:01-14:00 น.", "14:01-16:00 น.","16:01-18:00 น.", "18:01-20:00 น.",\
        "20:01-22:00 น.","22:01-24:00 น."])
for i in range(51, 59):
    with open('data.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        cnt1 = []
        for j in range(12):
            cnt1.append(0)
        for row in csv_reader:
            if row[0][-2:] == str(i):
                if row[6] == "24:01-01:00 น." or row[6] == "01:01-02:00 น.":
                    cnt1[0] += 1
                if row[6] == "02:01-03:00 น." or row[6] == "03:01-04:00 น." :
                    cnt1[1] += 1
                if row[6] == "04:01-05:00 น." or row[6] == "05:01-06:00 น.":
                    cnt1[2] += 1
                if row[6] == "06:01-07:00 น." or row[6] == "07:01-08:00 น." :
                    cnt1[3] += 1
                if row[6] == "08:01-09:00 น." or row[6] == "09:01-10:00 น.":
                    cnt1[4] += 1
                if row[6] == "10:01-11:00 น." or row[6] == "11:01-12:00 น.":
                    cnt1[5] += 1
                if row[6] == "12:01-13:00 น." or row[6] == "13:01-14:00 น.":
                    cnt1[6] += 1
                if row[6] == "14:01-15:00 น." or row[6] == "15:01-16:00 น." :
                    cnt1[7] += 1
                if row[6] == "16:01-17:00 น." or row[6] == "17:01-18:00 น.":
                    cnt1[8] += 1
                if row[6] == "18:01-19:00 น." or row[6] == "19:01-20:00 น.":
                    cnt1[9] += 1
                if row[6] == "20:01-21:00 น." or row[6] == "21:01-22:00 น.":
                    cnt1[10] += 1
                if row[6] == "22:01-23:00 น." or row[6] == "23:01-24:00 น.":
                    cnt1[11] += 1
            elif row[0][-2:].isdigit():
                if (int(row[0][-2:]))>i:
                    break
        pie_chart.add('ปี 25' + str(i), cnt1)

pie_chart.render_to_file('time.svg')


