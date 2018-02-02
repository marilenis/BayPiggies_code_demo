#Add two numbers
#Use input to get a number from the user

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

#observe result of adding the two numbers
#the problem here is that input() returns a string
#and we want to add two numbers
#so we need to covert from string to integer to obtain the
#correct result
print("Number 1 plus Number 2 equals ", number1 + number2)
