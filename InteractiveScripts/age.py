import datetime, sys
#this imports the datetime module so we can get the current year
year = datetime.datetime.now().year
#this sets the year variable to the current year.
while True:
    #this is a forever loop.
    while True:
        birthyear = input("What year were you born?\n")
        try:
            birth = float(birthyear)
            #this attempts to convert it to a number
            #if it suceeds it will run this code
            break
        except ValueError:
            #if it fails, it will run this code
            print("Please enter a number.")
    if int(birthyear) > int(year):
        #this part make sure the birth year is greater than the current year.
        print("Incorrect Birth Year!\nThe current year is", year, "and you entered {}!".format(birthyear))
        #commas space apart different parts.
        #since the bracket is the first bracket, it is replaced by the first thing in the .format() part.
        #this is necessary so there isnt a space inbetween the birthyear and the exclamation mark.
    else:
        break
    #this breaks itself out of the loop.
age = int(year)-int(birthyear)
#this subtracts the year from the birthyear.
#the int() function is used to turn it from a string to a integer.
print("You are", age, "years old!")