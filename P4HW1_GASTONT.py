#CTI110
#P4WH1
#GASTONT
#11/1/2022

#ASK THE USER FROR 6 GRADES FOR THE 6 MODULES.

grades = []
for grade in range(6):
    grade = int(input("Enter grade: "))
    grades.append(grade)

print("The grades are: ",grades)


print("Highest grade: ", max(grades))
print("Lowest grade: ", min(grades))

total = sum(grades)
count = len(grades)
average = total / count
print("Toal is: ", total)
print("Average is: ",average)
