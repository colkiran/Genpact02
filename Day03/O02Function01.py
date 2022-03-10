
def greet():
    print("Greetings Mr. Sachin, Welcome to Python Programming")

def greetGst(gstname):
    print(f"Greetings Mr. {gstname}, Welcome to the event....")

# city is default argument and gname is a non default argument
def greetGstCity(gname, city="Delhi"):
    print(f"Greetings Mr. {gname} from {city}, Welcome to the event.....")

greet()
greetGst("Rahul")
greetGstCity("Kholi")
greetGstCity("Yuvraj")
# parameters
greetGstCity("Ashwin", "Chennai")

# function can return values
# function can return more than one value
# return is the last of execution in a function

print("-" * 40)
def mutilplyMe(x, y):
    return x * y

print("The product of 10 and 20 is :", mutilplyMe(10, 20))

# recursive call
print("-" * 40)
def fun(x):
    if x > 0:
        print(f"Recursive call.....{x}")
    else:
        return 0
    fun(x-1)

res = fun(10)
print(f"res :{res}")

print("-" * 40)
def ArithematicCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

# x = 10, 20
res = ArithematicCalc(20, 8)
print(f"res :{res}")
print(type(res))

print("-" * 40)
# passing arguments to the function
# named arguments
def register(fname, lname, dob, conno, city, gender, eqlf):
    print(f"Name                    :{fname + ' ' + lname}")
    print(f"DOB                     :{dob}")
    print(f"Contact Number          :{conno}")
    print(f"City                    :{city}")
    print(f"Gender                  :{gender}")
    print(f"Education Qualification :{eqlf}")

register(eqlf="BE", city="Bangalore", gender="Male", conno='293482348',
         fname="Sachin", lname="Tendulkar", dob="25/05/1973")

print("-" * 40)
# variable length arguments
l = [1, 2, 3, 4, 5]
print(l)
print(*l)       # unpack

print("-" * 40)
def prodAll(*num):              # can accept more than one argument and store it in a tuple
    print(num, *num)
    prod = 1
    for n in num:
        prod *= n
    return prod

res = prodAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 40)

def extractDetails(**detail):
    print(detail)
    print(f"Name     :{detail['name']}")
    print(f"Score    :{detail['score']}")
    print(f"Opponent :{detail['opponent']}")
extractDetails(name="Rahul", score=65, opponent='SA')

print("-" * 40)

def admission(name, *tech, **marks):
    print(f"Name :{name}")
    print("Technologies Familiar :", tech)
    print("Academic Marks :", marks)

admission("Gibson", 'Java', 'J2EE', 'Spring', 'Hibernate', 'Angular', 'Python',
            Xth='89%', XIIth='85%', degree='78%', pg='87%')

print("-" * 40)

def fun():
    "This is a sample doc string"
    # this not a doc string
    print("Hello World")

fun()
print(fun.__doc__)                 # call the doc string

print("-" * 40)

def fun1(a, b):
    """
        This function fun1 takes two integer arguments and returns the sum of it

        sum(a, b) = fun1 (a, b)

        a and b are integer arguments
        the funtion returns an integer as a result
    """
    return a + b

print(fun1(30, 40))

print("-" * 40)

help(fun1)
