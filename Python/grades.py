import sys

grades = {'Biology':80, 'Physics':88, 'Chemistry':98, 'Math':89, 'English':79, 'Music':67, 'History':68, 'Art':53, 'Economics':95, 'Psychology':88}

def ave_grade():
    key = sys.argv[1]
    del grades[key]
    average = sum(grades.values())/len(grades)
    return round(average, 2)

print(ave_grade())