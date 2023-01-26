import pandas

data_301 = pandas.read_csv("/home/eg/grades/301.csv")
data_302 = pandas.read_csv("/home/eg/grades/302.csv")
data_303 = pandas.read_csv("/home/eg/grades/303.csv")
data_304 = pandas.read_csv("/home/eg/grades/304.csv")

#select cloumn with MP2 grades
grades_301 = data_301["MP2"]
grades_302 = data_302["MP2"]
grades_303 = data_303["MP2"]
grades_304 = data_304["MP2"]

#calculate total number of students & number of students in certain ranges
def calculate(grades):
    total_students = 0
    students_with_90_100 = 0
    students_with_85_89 = 0
    students_with_80_84 = 0
    students_with_75_79 = 0
    students_with_70_74 = 0
    students_with_65_69 = 0
    students_with_0_64 = 0
    for grade in grades:
        total_students += 1
        if grade >= 90 and grade <= 100:
            students_with_90_100 += 1
        elif grade >= 85 and grade <= 89:
            students_with_85_89 += 1
        elif grade >= 80 and grade <= 84:
            students_with_80_84 += 1
        elif grade >= 75 and grade <= 79:
            students_with_75_79 += 1
        elif grade >= 70 and grade <= 74:
            students_with_70_74 += 1
        elif grade >= 65 and grade <= 69:
            students_with_65_69 += 1
        elif grade >= 0 and grade <= 64:
            students_with_0_64 += 1

    print(f"Total number of students: {total_students}")
    print(f"Students with 90-100: {students_with_90_100}")
    print(f"Students with 85-89: {students_with_85_89}")
    print(f"Students with 80-84: {students_with_80_84}")
    print(f"Students with 75-79: {students_with_75_79}")
    print(f"Students with 70-74: {students_with_70_74}")
    print(f"Students with 65-69: {students_with_65_69}")
    print(f"Students with 0-64: {students_with_0_64}")


print(f"##301 Grades##")
calculate(grades_301)
print(f"##302 Grades##")
calculate(grades_302)
print(f"##303 Grades##")
calculate(grades_303)
print(f"##304 Grades##")
calculate(grades_304)