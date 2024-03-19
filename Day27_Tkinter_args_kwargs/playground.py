#Unlimited args

def add(*args):
    int_sum = 0
    for n in args:
        int_sum+=n
    return int_sum

print(add(3,4,5,6))

#Key-word args

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *=kwargs["multiply"]
    print(n)

calculate(2, add=3,multiply=5)

class Car:
    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make = "Nissan", model = "GTR")
print(my_car.model)
print(my_car.make)