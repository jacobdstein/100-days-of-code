import math


def paint_calc(height, width, coverage):
    num_cans: int = math.ceil(height * width / coverage)

    return num_cans


height = int(input("Enter the height of the area you are painting: "))
width = int(input("Enter the width of the area you are painting: "))
coverage = int(input("Enter the coverage of one paint can: "))

print(f"You need {paint_calc(height, width, coverage)} cans to paint the area")
