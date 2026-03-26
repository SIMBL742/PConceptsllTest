import csv

#creates the csv file with header and row structure
def grades_csv():
    #ask user for complete student count then covert string to int
    student_count = int(input("How many students in the class? "))

    #use with to create csv
    with open("grades.csv", "w") as file:
        #gives us permission to write manipulate file
        writer = csv.writer(file)

        #our header row
        writer.writerow(["First Name", " Last Name", " Exam 1", " Exam 2", " Exam 3"])

        #for loop responsible for gathering all student data
        for i in range(student_count):
            student_name = input("Student First Name: ")
            student_lname = input("Student Last Name: ")
            exam1_grade = int(input("Exam 1 Score: "))
            exam2_grade = int(input("Exam 2 Score: "))
            exam3_grade = int(input("Exam 3 Score: "))

            #creates row for each student
            student_row = [student_name, student_lname, exam1_grade, exam2_grade, exam3_grade]
            writer.writerow(student_row)

#reads and formats our creates csv
def read_grades_csv():

    #allows us to look into csv
    with open("grades.csv", "r") as file:
        reader = csv.reader(file)

        #for loop creates to iterate through each row and format correctly
        for row in reader:
            print(f"{row[0]:<20}{row[1]:<20}{row[2]:<20}{row[3]:<20}{row[4]:<20}")

#call our functions
grades_csv()
read_grades_csv()