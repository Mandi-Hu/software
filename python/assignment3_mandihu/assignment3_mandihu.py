__author__ = 'Die Hu, mandihu@live.unc.edu, Onyen = mandihu'

epsilon = 0.0001

# Ask users whether they want calculate single square root or a range of values.
single_or_range = input \
    ("Enter \'single\' or \'range\' to solve for a single square root or a range of values, respectively: ")

# If users enter words other than "single" or "range", ask users enter again
# until they enter "single" or "range".
while (single_or_range != "single" and single_or_range != "range"):
    print(single_or_range, "is NOT a choice.")
    single_or_range = input("Please enter \'single\' or \'range\': ")

# If users enter "single", ask them to enter a positive integer,
# and then calculate square root of this integer.
if (single_or_range == "single"):

   n = int(input("Eneter a positive integer value: "))

   # If users enter a negative integer or 0, ask they to enter again
   # until the integer they enter is positive.
   while n <= 0:
       n = int(input("The integer must be positive, please enter again: "))

   # Assign what users enter to estimated value.
   guess = n

   # Divide the integer n by estimate value guess, and
   # compare the result of that division to the current estimate guess.
   underguess = n / guess
   while abs(guess -  underguess) >= epsilon:

       # If the difference is greater than the epsilon value,
       # set estimated value guess to the average of the division and old estimate guess
       guess = (guess + underguess) / 2
       underguess = n / guess

   print("Value\tSquare Root")
   print(n,format(guess, "11.3f"),sep="\t\t")

# If users enter "range", ask them to provide a range of value by enter the start value and end value.
elif (single_or_range == "range"):
    start = int(input("Enter a positive integer value to start your range: "))

    # Make sure that the start value is positive.
    while start <=0:
        print("The start integer must be positive.")
        start = int(input("Enter a positive integer value again to start your range: "))


    end = int(input("Enter a positive integer value to end your range: "))

    # Make sure that the end value is positive and greater than start value.
    while end <=0 or end <= start:
        print("The end integer must be positive and greater than start value. ")
        end = int(input("Enter a positive integer value again to end your range: "))

    print("Value\tSquare Root")

    # Calculate square root of each number in the range.
    n = start
    for n in range(start, end+1):
        guess = n
        underguess =  n / guess
        while abs(guess - underguess) >= epsilon:
            guess = (guess + underguess) / 2
            underguess =  n / guess
        print(n,format(guess,"11.3f"),sep="\t\t")

