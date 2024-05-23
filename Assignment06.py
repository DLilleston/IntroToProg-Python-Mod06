# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# Change Log: (Who, When, What)
#   Danielle Lilleston, 21  May 2024, Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

# Processing ----------------------------------------------------#
class FileProcessor:

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        file = None
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
        finally:
            if file and not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        file = None
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file. \n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message, error=e)
        finally:
            if file and not file.closed:
                file.close()

# Presentation ---------------------------------------------------#
"""
    A collection of presentation layer functions that manage user input and output.
    
    """
class IO:

    """ This function displays custom error messages to the user

          """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        print(message, end="\n\n")
        if error is not None:
            print("--Technical Error Message --")
            print(error, error.__doc__, type(error), sep='\n')

    """ This function displays the menu of choices to the user

           """
    @staticmethod
    def output_menu(menu: str):
        print()
        print(menu)
        print()

    """ This function gets a menu choice from the user

        """
    @staticmethod
    def input_menu_choice():
        choice = "0"
        try:
            choice = input("Enter your menu choice number:")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(message="Invalid Menu Choice", error=e)

        return choice

    """ This function displays the student names and course enrolled in to the user

            """
    @staticmethod
    def output_student_and_course_names(student_data: list):
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    """ This function gets the student's first name, last name, and course name from the user

            """
    @staticmethod
    def input_student_data(student_data: list):

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="Incorrect data type", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data

# Main part of the code----------------------------------------------------------------#

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:
    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4.")

print("Program Ended")