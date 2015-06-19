__author__ = 'Die Hu, mandihu@live.unc.edu, Onyen = mandihu'

# The main function.
def main():

    # Get the input file.
    input_file = get_input()

    # Get the output file.
    output_file = get_output()

    # Assign grades.
    assign_grade(input_file, output_file)


# The function of opening input file.
def get_input():

    # Default read_file as False to start loop.
    read_file = False

    # Continue until find the input file.
    while read_file == False:

        try:
            input_file_name = input("Please enter the name of the input data file: ")
            input_file = open(input_file_name, "r")
            read_file = True

        # Catch a file not found error.
        except FileNotFoundError:
            print("The file", input_file_name, "could not be opened.")
            read_file = False

    return input_file

# The function of opening output file.
def get_output():

    write_file = False

    while write_file == False:

        try:
            output_file_name = input("Please enter the name of the output data file: ")
            output_file = open(output_file_name, "w")
            read_file = False

        except FileNotFoundError:
            print("The file", output_file_name, "could not be opened.")
            read_file = False

    return output_file

# The function of reading and assigning grades.
def assign_grade(input, output):

    # Default read_line as True. Once the program catch an error when reading lines, set read_line
    # to False to prompt the message "Error occurred while determining letter grade. Aborting." in 
    # the final. 
    # Otherwise, prompt the message "All data was successfully processed and saved to the requested 
    # output file."
    read_line = True

    # Ask users whether they would like to curve grades or not.
    curve_grade = curve()

    # If users would like to curve grades, ask users to enter the score they want to be treated as 100.
    if curve_grade == "y":
        fake_100 = treat_as_100()

    # If users reject to curve grades, make no change to baseline, which means treat 100 as 100 obviously.
    else:
        fake_100 = 100

    # For each student, read his/her category, name, grade.
    for i in range(14):

            try:
                grad_or_undergrad = input.readline().rstrip("\n")

                 # Invalid category. Break the loop to stop processing any further data.
                if grad_or_undergrad != "GRAD" and grad_or_undergrad != "UNDERGRAD":
                    print("Unknown student category detected", "("+ grad_or_undergrad + "). ")
                    read_line = False
                    break

                input_name = input.readline().rstrip("\n")
                input_grade = int(input.readline().rstrip("\n"))

                # Invalid grade. Break the loop to stop processing any further data.
                if input_grade < 0 or input_grade > 100:
                    print("The grade of", input_name, "must be a positive integer. ")
                    read_line = False
                    break

            # Catch a value error and break the loop to stop processing any further data.
            except ValueError:
                print("The grade of", input_name, "should be a valid integer. ")
                read_line = False
                break

            else:

                # Curve the grade.
                # If fake_100 = 100, actually the grade is not curved at all.
                if fake_100 != 0:
                    ratio = 100 / fake_100
                    input_grade = input_grade * ratio

                # If users treat 0 as 100, then everyone can get H or A depending on their categories.
                else:
                    input_grade = 100

                # When the student's all data are valid, write the name into output file.
                output.write(input_name + "\n")

                # Assign grade according to the grade.
                grade_level(grad_or_undergrad, input_grade, output)

    # Whether all data are processed correctly.
    if read_line == True:
        print("All data was successfully processed and saved to the requested output file.")
    else:
        print("Error occurred while determining letter grade. Aborting.")
        
    # Close files.
    input.close()
    output.close()

# Assign letter grade.
def grade_level(grad_or_undergrad, input_grade, output):
    
    if grad_or_undergrad == "GRAD":
        if input_grade >= 95:
            return output.write("H" + "\n")
        elif input_grade >= 80 and input_grade <= 94:
            return output.write("P" + "\n")
        elif input_grade >= 70 and input_grade <= 79:
            return output.write("L" + "\n")
        else:
            return output.write("F" + "\n")
        
    elif grad_or_undergrad == "UNDERGRAD":
        if input_grade >= 90:
            return output.write("A" + "\n")
        elif input_grade >= 80 and input_grade <= 89:
            return output.write("B" + "\n")
        elif input_grade >= 70 and input_grade <= 79:
            return output.write("C" + "\n")
        elif input_grade >= 60 and input_grade <= 69:
            return output.write("D" + "\n")
        else:
            return output.write("F" + "\n")

# The function of asking users whether curve grades or not.
def curve():
    
    # Validation.
    curve = input("Would you like to curve the grades? (y/n) ")
    
    while curve != "y" and curve != "n":
        print(curve, "is not a choice.")
        curve = input("please enter \"y\" or \"n\": ")
        
    return curve

# The function of asking users to enter the score that they want to treat as 100.
def treat_as_100():

    # Default valid_input as False to start the loop.
    valid_input = False

    # Continue until users enter a valid integer.
    while valid_input == False:
        try:
            fake_score = int(input("Please enter the score that should map to a '100%' grade: "))
            valid_input = True
        except ValueError:
            print("The score should be a valid integer. ")
            valid_input = False
        else:
            if fake_score < 0:
                print("Please enter an integer between 0 to 100 (both exclusive): ")
                valid_input = False

    return fake_score

# Call the main function.
main()