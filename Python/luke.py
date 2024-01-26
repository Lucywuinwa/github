import sys

def printRelation(key):
    relations = {
        'Darth Vader':'father',
        'Leia':'sister',
        'Han':'brother in law',
        'R2D2':'droid',
        'Rey':'Padawan',
        'Tatooine':'homeworld',
    }

    if key == 'Darth Vader':
        print("No, I am your father")
    else:
        print("Luke, I am your %s"%(relations[key]))

printRelation(sys.argv[1])