#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
digits = int(number)
if digits < 0:
    digit = -int(number[-1])
else:
    digit = int(number[-1])
if int(number[-1]) == 0:
    print("Last digit of {} is {} and is 0".format(number,digit))
elif int(number[-1]) > 5:
    print("Last digit of {} is {} and is greater than 5".format(number,digit))
elif int(number[-1]) < 6 and number[-1] != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number,digit))