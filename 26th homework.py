
import calendar    # Needed to present format

#initialize the year and the month variables

yr = 2023

mnth = 10

# printing the calendar

print(calendar.month(yr, mnth))




# Creating the whole year calender
import calendar
 
yy = 2023
 
print(calendar.calendar(yy))




# WRITING IN TURTLE

import turtle

turtle.color('deep pink')
style = ('Courier', 30, 'italic')
turtle.write('Hello!', font=style, align='center')
turtle.hideturtle()





# TO CREATE A CALENDER MONTH IN THE TURTLE CANVAS WITH PYTHON

from turtle import *
x=1
month = 1
const = 20
day = 1
speed(0)
monthname = ["","January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
weekdays = ["","S", "M", "T", "W", "TH", "F", "ST"]
start = [2, 5, 5, 1, 3, 6, 1, 4, 7, 2, 5, 7]



penup()
goto(-550, 300)
pendown()


for i in range(2):
    forward(const*7)
    right(90)
    forward(20)
    right(90)
setheading(90)
backward(const)
setheading(0)
forward(10)
write(monthname[month])
backward(10)

while(day < 8):
    for i in range (2):
        forward(const)
        right(90)
    forward(const-2)
    right(90)
    write(weekdays[day])
    setheading(180)
    forward(2)
    setheading(90)
    forward(const)
    setheading(0)
    forward(const)
    day += 1

backward(const*7)
right(90)
forward(const)
left(90)

if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    total = 31
elif (month == 4 or month == 6 or month == 9 or month == 11):
    total = 30
else:
     total = 28

#CALCULATING FIRST DAY OF ANY MONTH
century_digits = 2018 // 100
year_digits = 2018 % 100

value = year_digits + (year_digits // 4)

if century_digits == 18:
    value+=2
elif century_digits == 20:
    value+=6

if month ==1:
    value+=1
elif month == 2:
    value+=4
elif month == 3 or month == 1:
    value+= 4
elif month == 4 or month ==7:
    value+=0
elif month == 5:
    value += 2
elif month == 6:
    value += 5
elif month == 8:
    value += 3
elif month == 10:
    value+=1
elif month == 12 or month == 9:
    value+=6

day_of_week = (value + 1)% 7


if day_of_week == 0:
    starting_col = 7
else:
    starting_col = day_of_week
date = 1
for i in range(6):
    for j in range(7):
        for k in range(2):
            forward(const)
            right(90)
            forward(const)
            right(90)
            
        forward(const)
    setheading(270)
    forward(const)
    setheading(0)
    backward(const*7)

setheading(270)
penup()
forward(const)
pendown()
setheading(0)
month+=1




# CREATING A ROSE IN PYTHON TURTLE

from turtle import *
import turtle as tur

# Set initial position
tur.penup ()
tur.left (90)
tur.fd (200)
tur.pendown ()
tur.right (90)

# flower base
tur.fillcolor ("red")
tur.begin_fill ()
tur.circle (10,180)
tur.circle (25,110)
tur.left (50)
tur.circle (60,45)
tur.circle (20,170)
tur.right (24)
tur.fd (30)
tur.left (10)
tur.circle (30,110)
tur.fd (20)
tur.left (40)
tur.circle (90,70)
tur.circle (30,150)
tur.right (30)
tur.fd (15)
tur.circle (80,90)
tur.left (15)
tur.fd (45)
tur.right (165)
tur.fd (20)
tur.left (155)
tur.circle (150,80)
tur.left (50)
tur.circle (150,90)
tur.end_fill ()

# Petal 1
tur.left (150)
tur.circle (-90,70)
tur.left (20)
tur.circle (75,105)
tur.setheading (60)
tur.circle (80,98)
tur.circle (-90,40)

# Petal 2
tur.left (180)
tur.circle (90,40)
tur.circle (-80,98)
tur.setheading (-83)

# Leaves 1
tur.fd (30)
tur.left (90)
tur.fd (25)
tur.left (45)
tur.fillcolor ("green")
tur.begin_fill ()
tur.circle (-80,90)
tur.right (90)
tur.circle (-80,90)
tur.end_fill ()
tur.right (135)
tur.fd (60)
tur.left (180)
tur.fd (85)
tur.left (90)
tur.fd (80)

# Leaves 2
tur.right (90)
tur.right (45)
tur.fillcolor ("green")
tur.begin_fill ()
tur.circle (80,90)
tur.left (90)
tur.circle (80,90)
tur.end_fill ()
tur.left (135)
tur.fd (60)
tur.left (180)
tur.fd (60)
tur.right (90)
tur.circle (200,60)
tur.done()