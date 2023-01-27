
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
    print(f"Students with 0-64: {students_with_0_64}\n")