temperture = 0
if temperture > 30:
    print("It's warm")
    print("Drink water")
print("it's Done")
if temperture > 20:
    print("It's nice")
elif temperture >10:
    print("It's cold")
    print("Wear warm cloths")
else:
    print ("It's cold storm")
    print("Stay at home")
print("Thanks for the advise and I am safe.")
#basic way 
age = 22
if age > 18:
    print("Eligible")
else:
    print("Not Eligible")
#intermedia way
age = 15
if age > 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)
#advance way
age = 25
message = "Eligible" if age > 18 else "Not Eligible" 
print(message)
# using And operator
high_income = True
good_cerdit = True
if high_income and good_cerdit:
    print("Eligible")
else:
    print("Not Eligible")
#using Or operator
high_income = True
good_cerdit = False
if high_income or good_cerdit:
    print("Eligible")
else:
    print("Not Eligible")
#using Not operator
student = True
if not student:
    print("Eligible")
else:
    print("Not Eligible")
#using complex cndition
high_income = True
good_cerdit = False
student = True
if (high_income or good_cerdit) and (not student):
    print("Eligible")
else:
    print("Not Eligible")
#chaining comparsion operator
if 18 <= age < 65: #instead of writing if age >= 18 and age < 65:
    print("Eligible")
#for Loop
for number in range(1, 10, 2):
    print("Roma", number, number * ".")
    successful = True
    for number in range(3):
        print("Attempt")
        if successful:
            print("successful")
            break
        else:
            print("Attempted 3 times and failed")
#nested loop
for x in range(5):
    for y in range(3):
        print(f"({x} , {y})")
#Exercise output should be
#2
#4
#6
#8
#we have 4 even numbers.
count = 0
for number in range(1,10):
    if (number%2)==0:
        print(number)
        count+=1
print(f"we have {count} even numbers.")

