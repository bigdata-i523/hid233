import matplotlib.pyplot as plt
a = (16,11,6,6,5,5,5,5,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,
2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0)
plt.hist(a, bins=35)
plt.xticks(a)
plt.title("Histogram of Student Corrections")
plt.xlabel('number of students')
plt.ylabel('time spend for corrections')
plt.show()
