"""
this program ment to manage a zoo
author : me
date 12/12
"""

from enum import Enum
import json


class Actions (Enum):
    ADD = 1
    PRINT = 2
    EXIT = 3

animals =[]
DATA_FILE ='data.json'

def menu():
        for action in Actions:
            print (f"{action.value} - {action.name}")
        
        return Actions( int( input("selection?")))

def print_animals():
    for animal in animals:
        print(f'Animal name {animal["name"] }age:{animal["age"]}')

def exit_program():
    with open(DATA_FILE, 'w') as f:
        json.dump(animals, f)
    exit()

def save_data():
    global animals
    try:
        with open(DATA_FILE,'r') as f:
            animals=json.load(f)
    except:
        print(" make sure the file exist")

def main():
    save_data()
    while(True):
        userSelection= menu()
        if userSelection == Actions.ADD: 
            animals.append({"name":input("animal name?"),"age":input("age")})
        elif userSelection == Actions.EXIT:
            exit_program()
        elif userSelection == Actions.PRINT:
            print_animals()
        else:
             print(" u idiot")


if __name__ == '__main__':
    main()