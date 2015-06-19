__author__ = 'Die Hu, mandihu@live.unc.edu, Onyen = mandihu'



print("Compound Interest Calculator")

#Get investment parameters from user.
initial_investment = float(input("Please enter the initial amount of the investment: "))

rate_interest = float(input("Please enter the interest rate(e.g, \'.01\' for interest rate 1%): "))

years = float(input("Please enter the number of years investing: "))

compounding_number = int(input("Please enter the number of compoundings per year: "))

#Calculate the new balance after earning interest.
#The formula is P'=P(1+r/n)^(nt)
#P is the initial amount of the investment(initial_investment)
#r is the interest rate(rate_interest)
#n is the number of compoundings per year(compouding_number)
#t is the number of years of interest(years)
#P' is the new balance of the account after earning interest for t years(new_balance)
new_balance = initial_investment * ((1 + rate_interest / compounding_number) ** (years * compounding_number))

#Print calculating results.
print("Initial Investment: $", format(initial_investment, ",.2f"), sep = "")
print("Interest Earned:    $", format(new_balance - initial_investment, ",.2f"), sep = "")
print("Final Balance:      $", format(new_balance, ",.2f"), sep = "")

#Ask the user whether he wants to compare this with other investment options.
additional_set = input("Do you want to compare this with another investment option? y for Yes, n for No. ")

#If the user says yes, he should input y.
#Once the user inputs "y", the program will ask he to input another set of investment parameters.
if additional_set == "y":

#Get another set of investment parameters.
    initial_investment_add = float(input("Please enter the initial amount of the investment: "))

    rate_interest_add = float(input("Please enter the interest rate(e.g, \'.01\' for interest rate 1%): "))

    years_add = float(input("Please enter the number of years investing: "))

    compounding_number_add = int(input("Please enter the number of compoundings per year: "))

    new_balance_add = initial_investment_add * ((1 + rate_interest_add / compounding_number_add) \
                                        ** (years_add * compounding_number_add))

    #Pring calculating results.
    print("Initial Investment: $", format(initial_investment_add, ",.2f"), sep = "")
    print("Interest Earned:    $", format(new_balance_add - initial_investment_add, ",.2f"), sep = "")
    print("Final Balance:      $", format(new_balance_add, ",.2f"), sep = "")

    #Compare two sets of investment parameters.
    if (new_balance > new_balance_add):

        #If the new balance of second options is less than first one, the program will
        #tell the user "The first option will result in the largest final account balance."
        print("The first option will result in the largest final account balance.")

    elif (new_balance < new_balance_add):

        #If the new balance of second options is more than first one, the program will
        #tell the user "The second option will result in the largest final account balance."
        print("The second option will result in the largest final account balance.")

    else:
        #If the new balance of second options equals to first one, the program will
        #the user "The two options will result in the same final account balance."
        print("The two options will result in the same final account balance.")

    #Tell the user that the calculation is over.
    print("Your calculation is over!")

#If the user input n for not comparing first option with another option, the program will
#tell the user that the calculation is over.
else:
    print("Your calculation is over!")