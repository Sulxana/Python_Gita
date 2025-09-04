from datetime import datetime, timedelta, date
from itertools import permutations, combinations
import  calendar,time,random
# 1 მოცემულია სიტყვა "ABCD". დაბეჭდე ყველა შესაძლო ვარიანტი და **დაითვალე** რამდენია სულ რაოდენობრივად (უნდა დააბრუნო რიცხვი)

word = "ABCD"
count = 0
for x in permutations(word):
    print(x)
    count+=1
print(count)

# 2 იპოვე მომდევნო კვირის პირველი სამშაბათი, საწყისი თარიღი არის დღევანდელი დღე (ხელით არ გაწეროთ თარიღი)
today = datetime.today()
for i in range(1,8):
    day = today + timedelta(days=i)
    if day.weekday() == 1:
        print(day)
        break

# 3 დაადგინე, არის თუ არა შეყვანილი წელი ნაკიანი, მომხმარებელს შემოჰყავს მხოლოდ წელი და ვეუბნებით არის თუ არა ნაკიანი
myinput = int(input("შეიყვანე წელი: "))

# ვარიანტი 1
mytuple = calendar.monthrange(myinput,2)
if mytuple[1] == 29:
    print("ნაკიანია")
else :
    print("არ არის ნაკიანი")

# ვარიანტი 2
mylist = calendar.month(myinput,2,5).split()
if mylist[-1] == "29":
    print("ნაკიანია")
else :
    print("არ არის ნაკიანი")

# 4 დაითვალე რამდენი კვირაა დარჩენილი ახალ წლამდე, საწყისი თარიღი არის დღევანდელი დღე (ხელით არ გაწეროთ თარიღი)
today = datetime.today()
newyear = datetime(today.year+1,1,1)
remain = (newyear - today).days // 7
if (newyear - today).days % 7 != 0:
    remain +=1

print(remain)

# 5 შექმენი ყველა 3-ელემენტიანი კომბინაცია სიიდან \[1,2,3,4,5] (itertools-ის გამოყენებით)
mylist = [1,2,3,4,5]
for x in combinations(mylist,3):
    print(x)

# 6 მიიღე ყველა კომბინაცია "XYZ"-ის სიმბოლოებით სიგრძე 1-დან 3-მდე
# მაგალითი: X, Y, Z, XY, XZ, YZ, XYZ უნდა მივიღოთ მსგავსი შედეგი.
strs = "XYZ"
mylist = []
for i in range(1,4):
    for x in combinations(strs,i):
        mylist.append("".join(x))
print(", ".join(mylist))