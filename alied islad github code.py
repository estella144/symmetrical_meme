population = 275
original_population = 400


while True:
    proccess = input("do you want to change or view a variable? (c/v)")
    if proccess == "c":
        print ("In progress")
    elif proccess == "v":
        request = input("what do you want to find?")
        if request == "population":
            print (population)
            #return to find menu
        elif request == "original population":
            print (original_population)
            #return to find menu
    else:
        print ("Invalid request")

