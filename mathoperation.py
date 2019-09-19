#This program is to review:
mathop = open('mathop.txt')
for line in mathop:
    print("This program will make this math operation: ", line)
number = int(input("Introduce a number:"))
firsttotal = (3 + number)/(number*5)
total = firsttotal**number
print(total)