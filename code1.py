from turtle import *
def malben(x, y, grade):
    penup()
    goto (x, y)
    pendown()
    forward(20)
    left(90)
    forward(grade)
    left(90)
    forward(20)
    left(90)
    forward(grade)
    left(90)
    penup()
    goto(x, y - 20)
    pendown()
    write(name)


    
x = -300
while True:
    name = input("Enter your name or quit to stop:")
    if name == "quit":
        print("You quit the program. Goodbye")
        break
    grade = input("Enter your grade:")
    try:
        grade = int(grade)
    except:
        print("Invalid grade. Please try again")
        continue
    if 0 < grade < 101:
        malben(x, 0, grade)
    else:
        print("Invalid grade. Please try again")
    x = x + 50
