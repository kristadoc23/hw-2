def print_name(name):
    print("The name is",name)

print_name("krista")

import math
def ninety(a, b, c):
    d = 360 - (a+b+c)
    return d
    
def miles_per_hour(miles, hours, minutes, seconds):
    total_hours = (hours + minutes/60 + seconds/3600)
    total_miles = (miles/total_hours)
    return total_miles

name = input("What is your name?\n")
if name == "Chris":
    print("Hello Chris")
else:
    print("Goodbye")


def convert_temperature(temp, units):
    if units == "celsius":
        new_temp = (temp * 9/5) + 32
    else:
        new_temp = (temp - 32) * 5/9
    return new_temp

def calculate_grade(score):
    if score >= 90:
        print("A")
    elif 80 <= score < 90:
        print("B")
    elif 70 <= score <80:
        print("C")
    elif 60 <= score <70:
        print("D")
    else:
        print("F")
    
