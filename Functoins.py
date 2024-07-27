#basic function
def greet():
    print("hello Roma")
    print("how are you")
    print("what do you do")
#arguments
def greet(first_name, last_name):
    print(f"hello {first_name} {last_name}")
    print("how are you")
    print("what do you do")
greet("Roma","Irshad")
#two types of function
#perform a task
#return a value
def get_greeting(name):
    return f"hello {name}"
message = get_greeting("Roma Irshad")
print(message)
#keyword permeter 
def increment(number,by):
    return number + by
print(increment(5,by = 2))
#print(increment(5,2)) same
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *=number
    return total
print(multiply(2,3,4,6))
def save_user(**user):
    print(user)
save_user(id = 1, name = "Roma", age = 21)
#scope
message = "a" #global variable
def greet(name):
    message = "b" # local variable
greet("Mosh")
print(message)
message = "a" #global variable
def greet(name):
    global message
    message = "b" # local variable
greet("Mosh")
print(message)
#exercise
def fizz_buzz(input):
    if (input%3)==0 and (input%5)==0:
        return "Fizz Buzz"
    elif (input%3)==0:
        return "Fizz"
    elif (input%5)==0:
        return "Buzz"
    else:
        return input

print(fizz_buzz(5))