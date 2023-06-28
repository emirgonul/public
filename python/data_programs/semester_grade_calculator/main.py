#Mrs. Kilic's grade statistics script
import pandas
from grade_calculate import *

user_input = input("Which Marking Period do you want to calculate?:\n")
sections = []
sections = input("Enter Section Numbers To Calculate:\n").split()
marking_period = f"MP{user_input}"

for section in sections:
    #create dataFrame with section's csv file
    data = pandas.read_csv(f"/home/eg/grades/{section}.csv")
    #select the column with marking periods
    grades_data = data[marking_period]
    #print entered sections name and statistics
    print(f"\n#{section} Grades")
    calculate(grades_data)