import requests
import re
import pandas as pa
import matplotlib.pyplot as plt

link = 'https://raw.githubusercontent.com/bigdata-i523/hid233/master/experiment/classification/classification.txt'
d = requests.get(link).text

d = re.split('\n|, ', d)
pair = [i.split(' ') for i in d]
pair = pair[:-1]

correction_time = []
student_category = []

for i in pair: 
    correction_time.append(pa.to_numeric(i[0]))
    student_category.append(pa.to_numeric(i[1]))

plt.scatter(correction_time, student_category)
plt.title("Classification of Student Corrections")
plt.xlabel('Time spend for corrections')
plt.ylabel('Category of students')
plt.show()
