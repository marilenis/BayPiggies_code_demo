#This example demonstrate the use of built in functions for lists
#No need to write additional code, it is already there for you!

num_input = 5
list_numbers = []

for num in range(num_input):
    number = int(input("Enter a number between 1 and 100: "))
    list_numbers.append(number)

#Built in functions
max_number = max(list_numbers)
print("The largest value entered is: ", max_number)
min_number = min(list_numbers)
print("The smallest value entered is: ", min_number)
sum_numbers = sum(list_numbers)
print("The sum of the numbers is: ", sum_numbers)

#Use of range() and list
numbers_in_range = list(range(num_input))
print("The numbers in range 0,",num_input, "are ", numbers_in_range)

#range() and list in a for loop
for index in range(num_input):
    print("list_numbers[",index,"]= ", list_numbers[index]) 








