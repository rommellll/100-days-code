# *args Unlimited positional arguments
def add(*args):
    total = 0
    for n in args:
        total += n
    return total

print(add(1,2,3,4,5,6,7,8,9,10))


# **kwargs Unlimited keyword arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3,multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make", "Toyata")
        self.model = kw.get("model", "Veloz")
        self.seats = kw.get("seats", 5)

my_car = Car(make="Toyota")
print(my_car.model)