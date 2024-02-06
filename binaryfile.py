
import datetime
import os
numberInput = input("Enter your number: ")
number = int(numberInput)
Binary = bin(number)
dateToday = datetime.datetime.now()

file = open("History.txt",'w')
file.write("number\n")
file.write(numberInput)
file.write(Binary)
file.write("\n")
file.write(f'{dateToday}')
print(os.system('ifconfig'))
file.close()
file = open("History.txt",'r')
print(file.read())