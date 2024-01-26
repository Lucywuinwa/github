import sys


def print_gpa(grade1, grade2, grade3, grade4):
    grades = [grade1, grade2, grade3, grade4]
    gpa_dict = {
        "A": 4.0,
        "A-": 3.66,
        "B+": 3.33,
        "B": 3.0,
        "B-": 2.66,
        "C+": 2.33,
        "C": 2.0,
        "C-": 1.66,
        "D+": 1.33,
        "D": 1.00,
        "D-": 0.66,
        "F": 0.00,
    }

    total = 0
    for gpa in grades:
        total += gpa_dict[gpa.upper()]
    gpaa = total / len(grades)
    gpaa = round(gpaa, 2)
    print(f"My GPA is {gpaa:.2f}")


print_gpa(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
