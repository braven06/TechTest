#Set Available Drinks here
availabledrinks = ["coffee", "chocolate", "lemon tea"]
#Create list of common ways to say "yes"
yeslist = ["yes", "y", "yea", "yeah", "ok", "okay", "sure"]
#Create list of common ways to say "no"
nolist = ["no", "n", "nope"]

#loop allowing for multiple users
while True:
    #Present user drinks and allow for selection
    print("Welcome to the hot drinks machine!")
    print("Please select your drink below: ")
    for i in availabledrinks:
        print(i.capitalize())
        
    drinkselection = input("> ")

    #Handle invalid input
    while drinkselection.lower() not in availabledrinks:
        print("invalid drink!")
        drinkselection = input("> ")

    #Make drinks
    if drinkselection.lower() == availabledrinks[0]:
        #coffee
        print("Boiling water...")
        print("Brewing coffee grounds...")
        print("Pouring coffee...")
        #ask for sugar
        print("Would you like sugar?")
        sugardecision = input("> ")
        #handle invalid input
        while sugardecision.lower() not in (yeslist + nolist):
            print("Invalid input!")
            sugardecision = input("> ")
        if sugardecision.lower() in yeslist:
            print("Adding sugar...")

        #ask for milk
        print("Would you like milk?")
        milkdecision = input("> ")
        #handle invalid input
        while milkdecision.lower() not in (yeslist + nolist):
            print("Invalid input!")
            milkdecision = input("> ")
        if milkdecision.lower() in yeslist:
            print("Adding milk...")

        print("Ready!")
    if drinkselection.lower() == availabledrinks[1]:
        #chocolate
        print("Boiling water...")
        print("Adding chocolate powder to cup...")
        print("Pouring chocolate...")
        print("Ready!")
    if drinkselection.lower() == availabledrinks[2]:
        #lemon tea
        print("Boiling water...")
        print("Steeping water in tea...")
        print("Pouring tea...")
        print("Adding lemon...")
        print("Ready!")
    #new line so that the text for the new user looks neat!
    print("")
