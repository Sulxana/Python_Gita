import random
import string

from setuptools.unicode_utils import try_encode

# ამოცანა 1
c = input("შემოიყვანე ასო: ")
# ვარიანტი 1
mytuple = ("ა","ე","ი","ო","უ")
if mytuple.count(c):
    print(f"{c} არის ხმოვანი")
else:
    print(f"{c} არის თანხმოვანი")
# ვარიანტი 2
if c=="ა" or c=="ე"or c=="ი"or c=="ო"or c=="უ":
    print(f"{c} არის ხმოვანი")
else:
    print(f"{c} არის თანხმოვანი")
#
# ამოცანა 2
a = 10
for _ in range(10):
    print(a)
    a-=1
#
# ამოცანა 3
lst = [random.randint(1,20) for _ in range(10)]
print(lst)
count = 0
for i in range(10):
    a = lst[i]
    index = i
    for j in range(10):
        if a < lst[j]:
            a = lst[j]
            index = j
    count+=1
    print(f"{count} უდიდესი რიცხვი: {a}; ინდექსი: {index}")
    lst[index] = -1
    if count==3:break
#
#          ციკლის გარეშეც მომაფიქრდა მაგრამ ციკლი უფრო მოქნილია
print(f"უდიდესი რიცხვი: {max(lst)}; ინდექსი: {lst.index(max(lst))}")
x = lst.index(max(lst))
lst.remove(max(lst))
lst.insert(x,-1)
print(f"უდიდესი რიცხვი: {max(lst)}; ინდექსი: {lst.index(max(lst))}")
x = lst.index(max(lst))
lst.remove(max(lst))
lst.insert(x,-1)
print(f"უდიდესი რიცხვი: {max(lst)}; ინდექსი: {lst.index(max(lst))}")
#
# ამოცანა 4
w = int(input("შეიყვანე სიგანე: "))
h = int(input("შეიყვანე სიმაღლე: "))
for i in range(h):
    for j in range(w):
        print("#",end=" ")
    print("\n")

# ამოცანა 5
# max და min იმიტო გამოვიყენე რო იქნებ მომხმარებელმა პირიქით შემოიტანოს დიდი და პატარა რიცხვები
def funct(x,y):
    print(x+y)
    print(max(x,y)-min(x,y))
    print(x*y)
    print(max(x,y)/min(x,y))
    print(max(x, y) // min(x, y))
    print(max(x, y) % min(x, y))
#
a = int(input("შეიყვანე პირველი რიცხვი: "))
b = int(input("შეიყვანე მეორე რიცხვი: "))
funct(a,b)
#
# ამოცანა 6
def Pr(x,y):
    for i in range(y):
        for j in range(x):
            print("#",end=" ")
        print("\n")

w = int(input("შეიყვანე სიგანე: "))
h = int(input("შეიყვანე სიმაღლე: "))
Pr(w,h)
#
# ამოცანა 7
def Count(s,c):
    print(f'Character "{c}" in given string: {s.count(c)} times')

str = input("შეიყვანე ტექსტი: ")
c = input("შეიყვანე ასო: ")
Count(str,c)

# ამოცანა 8
def funct(s):
    print(f'სიტყვების რაოდენობა წინადადებაში შეადგენს {s.count(" ") + 1}-ს')
str = input("შეიყვანე ტექსტი: ")
funct(str)
#
# ამოცანა 9
# რანდომული სიტყვების გენერირება
word = string.ascii_letters
x = "".join(random.sample(word,10))

count = 0
while True:
    guess = input("შეიყვანეთ სწორი სიტყვა: ")
    if guess == x:
        print("გილოცავ!!!")
        break
    elif guess == "exit":
        break
    elif count==10:
        print("თქვენ დამარცხდით")
        break
    else:
        print("არასწორია კიდევ ცადეთ")
    count+=1
#
# ამოცანა 10
# თუ ერთიც შეეშლება გაგრძელებას ცდების აღარ აქვს და ავტომატურად უნდა გამოიტანოს დამარცხება.
trying = ["მარჯვენა","მარცხენა"]
x = random.choice(trying)
##print(x) - ჩვენ რო გავიგოთ რომელია
count = 0
while True:
    guess = input("შეიყვანე სიტყვა: ")
    if guess != x :
        print("დამარცხება")
        break
    elif guess == "exit":break
    count += 1
    if count==5:
            print("გამარჯვება")
            break

