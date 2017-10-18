import matplotlib.pyplot as plt

correction_time = (16,11,6,6,5,5,5,5,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
                   1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
student_category = (2,3,2,3,2,3,3,1,3,2,2,2,2,2,3,3,3,2,2,2,3,3,2,2,3,3,3,1,3,2,2,3,3,3,3,3,1,2,2,2,3,3,3,
                    3,1,3,3,2,2,2,2,2,3,3,3,3,1,3,3,2,2,3,3,3,3,1,3,3,2,2,1,3,3,1,3,2,3,3,3)

plt.scatter(correction_time, student_category)
plt.title("Classification of Student Corrections")
plt.xlabel('Time spend for corrections')
plt.ylabel('Category of students')
plt.show()
