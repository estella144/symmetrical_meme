population = 275
original_population = 400
sus = 0

while True:
    proccess = input("do you want to change or view a variable? (c/v)")
    if proccess == "c":
        print ("In progress")
    elif proccess == "v":
        request = input("what do you want to find?")
        if request == "population":
            print (population)
            print("")
            print("")
            
        elif request == "original population":
            print (original_population)
            print("")
            print("")
        elif request == "sus":
            sus=(sus+1)
            print("You are X", sus, "sus ")
    elif proccess == "sus":
            sus=sus+1
            print ("You are X", sus, "sus ")
            
    else:
        print ("Invalid request")

