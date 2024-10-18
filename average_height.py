print("Welcome to Average height calculator of students here\nCome to this machine and stand on it wait till machine tell you it's complete\nso let's get started  ")

print("Just come here and stand for some seconds or If you guys know your height just type it here ha ha ")


student_height = input("Enter the heights of students: ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)
total_student = len(student_height)
sum_height = sum(student_height)
average_height = round(sum_height / total_student)
print(f"The average height of the students is {average_height}")