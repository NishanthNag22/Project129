import csv

dataSet1=[]
dataSet2=[]

with open('unit_converted_stars.csv','r') as f:
    csv_reader=csv.reader(f)

    for row in csv_reader:
        dataSet1.append(row)

with open('starsSorted.csv') as f:
    csv_reader=csv.reader(f)

    for row in csv_reader:
        dataSet2.append(row)

header1=dataSet1[0]
planet_data1=dataSet1[1:]

header2=dataSet2[0]
planet_data2=dataSet2[1:]

headers=header1+header2

planet_data=[]

for index,data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])

with open('finalData.csv','a+') as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)