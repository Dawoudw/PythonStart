option= input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if option=="stamps":
    print("Select Stamp ")

elif option=="envelope":
    print("Select Evnelop size")

elif option=="copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))

else:
    print("Thank you, please come again.")
    
