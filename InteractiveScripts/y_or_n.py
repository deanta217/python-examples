answer = input("Do you like cupcakes (Y/N) \n")
if answer.upper() == "Y":
    # .upper() makes it uppercase
    print("Yes")
elif answer.upper() == "N":
    # elif is else and if combined
    print("No")
else:
    print("Answer Y or N")