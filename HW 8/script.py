import gc
from dataclasses import dataclass
from gc import garbage


#1 ამოცანა 1
# შექმენი კლასი BankAccount, რომელსაც ექნება: დახურული ატრიბუტები: __balance, __owner.
# მეთოდი deposit(amount) – თანხის დამატება. მეთოდი withdraw(amount) – თანხის გამოტანა (არ უნდა გადავიდეს მინუსში).
# მეთოდი get_balance() – მხოლოდ წაკითხვისთვის. დაწერე კოდი ისე, რომ მომხმარებელს პირდაპირ __balance-ზე წვდომა არ ჰქონდეს.

class BankAcc:
    def __init__(self,balance,owner):
        self.__balance = balance
        self.__owner  = owner
        self.get_balance()

    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print('თქვენ გსურთ იმაზე მეტის გამოტანა ვიდრე ანგარიშზე გაქვთ')
    def get_balance(self):
        return self.__balance

me = BankAcc(1000,1)
me.deposit(50)
me.withdraw(1000)
me.get_balance()

#2 ამოცანა 2
# შექმენი კლასი ShoppingCart, რომელსაც ექნება:
# ატრიბუტი items (სიაში პროდუქტების რაოდენობა).
# __len__() დააბრუნებს პროდუქტების რაოდენობას.
# __eq__() ორი კალათის შედარება – აბრუნებს True, თუ რაოდენობა ტოლია.
# გააკეთე 2 კალათა და შეადარე.
# გააკეთე 3 კალათა და შეადარე.
# გააკეთე 4 კალათა და შეადარე.

class ShoppingCart:
    def __init__(self,items):
        self.__items = items

    def __len__(self):
        return len(self.__items)
    def __eq__(self, other):
        return self.__items == other.__items
#
first = ShoppingCart([5,9,12])
second = ShoppingCart([1,2,3])
third  = ShoppingCart([5,9,12])
forth = ShoppingCart([1,2,3])
mylist = [first,second,third,forth]

for i in range(4):
    for j in range(i+1,4):
        print(f"{i+1} == {j+1}?: {mylist[i]==mylist[j]}")
print(len(first))

#3 ამოცანა 3
# გამოიყენე @dataclass მოდული კლასის Book შესაქმნელად:
# ველები: title, author, year.
# დაამატე მეთოდი is_classic() → აბრუნებს True, თუ წელი < 1970.
# შექმენი რამდენიმე წიგნი და შეამოწმე ფუნქცია.

@dataclass
class Book:
    title:str
    author:str
    year:int

    def is_classic(self):
        if self.year < 1970:
            return True
        else:
            return False
book1 = Book("gio","gio",2006)
book2 = Book("Lion","Lion",1755)
print(book1.is_classic())
print(book2.is_classic())

#4 ამოცანა 4
# შექმენი კლასი Person, რომელსაც ექნება __del__() მეთოდი, რომელიც ბეჭდავს "Person removed" როცა ობიექტი წაიშლება.
# შექმენი ობიექტი, შემდეგ წაშალე del-ით და ნახე როგორ რეაგირებს garbage collector.
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Person removed")


grb  = gc.collect()
counts = gc.get_count()

p1 = Person("gio",19)
del p1

print(grb,gc.collect())
print(counts,gc.get_count())

#5 ამოცანა 5
# შექმენი კლასი Temperature, რომელსაც ექნება:
# დახურული ატრიბუტი __celsius.
# get და set property °C-სთვის.
# fahrenheit property (read-only), რომელიც აბრუნებს °F.
# შექმენი ობიექტი, შეცვალე °C და შეამოწმე °F ავტომატურად იცვლება თუ არა.

class Temperature:
    def __init__(self,celsius):
        self.__celsius = float(celsius)

    @property
    def see_temp(self):
        return f"{self.__celsius} Celsius"

    @see_temp.setter
    def see_temp(self,new):
        self.__celsius = float(new)

    @see_temp.getter
    def show_f(self):
        self.__celsius = (self.__celsius * 9/5) + 32
        return f"{self.__celsius} Fahrenheit"

temp = Temperature(30)
print(temp.see_temp)

temp.see_temp = 100
print(temp.see_temp)
print(temp.show_f)

#6 ამოცანა 6
# შექმენი კლასი CustomList, რომელიც:
# ინახავს ელემენტებს.
# __getitem__() – აბრუნებს ელემენტს ინდექსით.
# __setitem__() – ცვლის ელემენტს.
# __iter__() – Iterable უნდა იყოს.
# გამოიყენე for ციკლში შენი CustomList.

class CustomList:
    def __init__(self,items):
        self.__items = items

    def __getitem__(self, key):
        return self.__items[key]

    def __setitem__(self, key, value):
        self.__items[key] = value

    def __iter__(self):
        return iter(self.__items)

mylist = CustomList([1,2,3,4,5])

print(mylist.__getitem__(1))

mylist.__setitem__(1,15)

print(mylist.__getitem__(1))

for x in mylist:
    print(x,end=" ")

##7 ამოცანა 7
# შექმენი კლასი Refrigerator, რომელსაც ექნება:
# ატრიბუტი items (სია).
# __contains__() – აბრუნებს True, თუ პროდუქტი მაცივარშია ("milk" in fridge).
# __str__() – "Fridge with N items".
# __del__() – "Fridge unplugged!".
# დაამატე პროდუქტები, შეამოწმე "milk" in fridge, დაბეჭდე ობიექტი და ბოლოს წაშალე.

class Refrigerator:
    def __init__(self,items):
        self.__items = items

    def __contains__(self, item):
        return item in self.__items

    def __len__(self):
        return len(self.__items)

    def __str__(self):
        return f"Fridge with {len(self)} items"

    def __del__(self):
        print("Fridge Unplugged")

ref = Refrigerator(["milk","chocolate","egg"])
print(ref)
print(ref.__contains__("Milk".lower()))
del ref

#8 ამოცანა 8
# შექმენი კლასი FunnyCalculator, რომელსაც ექნება:
# __add__() – აბრუნებს "Why are you adding numbers? Just buy a calculator".
# __mul__() – აბრუნებს "Multiplication is too mainstream...".
# __truediv__() – თუ გაყოფ 0-ზე, ბეჭდავს "ZeroDivisionError? Nah, let’s just say infinity"
# __str__() – "I’m the funniest calculator in Python!".
# ცადე calc + 5, calc * 2, 10 / calc და ნახე რა მოხდება.

class FunnyCalculator:
    def __init__(self,numbers):
        self.__numbers = numbers

    def __add__(self, other):
        return "Why are you adding numbers? Just buy a calculator"
    def __mul__(self, other):
        return "Multiplication is too mainstream..."
    def __truediv__(self, other):
        if other.__numbers == 0:
            print("ZeroDivisionError? Nah, let’s just say infinity")

    def __str__(self):
        return "I’m the funniest calculator in Python!"
obj1 = FunnyCalculator(10)
obj2 = FunnyCalculator(0)

print(obj1 + obj2)
print(obj1 * obj2)
obj1.__truediv__(obj2)
print(obj1)

