# wfp, 6/1/07, example 6
# wfp, 9/13/11, update names
# simple if

dividend_str = input("Give me an integer to divide: ")
divisor_str = input("Give me an integer to divide it by: ")

dividend_int = int(dividend_str)
divisor_int = int(divisor_str)

print("The result of the expression divisor_int==0 is: ", divisor_int==0)
if divisor_int == 0:
    print("Hey, your divisior is: ",divisor_int)
    print("You can't divide by 0")
    print("Run the program and enter a non-zero divisor")
    # this is harsh, exits the shell)
    exit(1)

print("The result of ",dividend_int,"/",divisor_int," is: ",dividend_int/divisor_int)
print("Thanks for running the program")

