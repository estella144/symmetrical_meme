# This file created by ObsidianTurtle and improved by estella_144

import json

def main():
    c1 = input("do you want to change or view a variable? (c/v)")
    if c1 == "c":
        print("In progress")
        main()
    elif c1 == "v":
        find()
    else:
        print("Invalid request")
        main()

def load(filename):

    with open(filename, 'r') as f:
        return json.load(f)

def find():

    d = load("servdata/population.json")
    population = d["population"]
    original_population = d["original_population"]

    c1 = input("what do you want to find? (Or B to go back)")
    if c1 == "population":
        print(population)
        find()
    elif c1 == "original population":
        print(original_population)
        find()
    elif c1 == "b":
        main()
