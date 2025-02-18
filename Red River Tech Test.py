#Set Available Drinks here
availabledrinks = {"coffee", "chocolate", "lemon tea"}

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
if drinkselection.lower() == "coffee":
    print("Boiling water...")
    print("Brewing coffee grounds...")
    print("Pouring coffee...")
    print("Adding sugar...")
    print("Adding milk...")
    print("Ready!")
if drinkselection.lower() == "chocolate":
    print("Boiling water...")
    print("Adding chocolate powder to cup...")
    print("Pouring chocolate...")
    print("Ready!")
if drinkselection.lower() == "lemon tea":
    print("Boiling water...")
    print("Steeping water in tea...")
    print("Pouring tea...")
    print("Adding lemon...")
    print("Ready!")