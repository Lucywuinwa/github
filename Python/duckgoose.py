import sys
duck_goose = sys.argv[1:]

def remove_goose(var):
    new_list = [item for item in duck_goose if item != 'goose']
    return new_list

print(remove_goose(sys.argv[1]))