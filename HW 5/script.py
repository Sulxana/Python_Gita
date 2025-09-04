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

## 7 თამაში უკუსვლაზე
# კომპიუტერი ირჩევს შემთხვევითობის პრინციპით რიცხვს 1-20 მდე,
# მოთამაშეს აქვს მხოლოდ 5 წამი რიცხვის გამოსაცნობად, თუ 5 წამში
# სწორ რიცხვს ვერ შეიყვანს, თამაში სრულდება და გამოდის ტექსტი "დრო ამოიწურა, თქვენ დამარცხდით".

# myinput = 0
x = random.randint(1,20)
print(x)
start = datetime.now().second
t = start+5
istrue = True
while datetime.now().second<=t:
    if datetime.now().second<=t:
        myinput = int(input("Sheiyv: "))
        if myinput == x:
            print("CORRECT!!!")
            istrue = False
            break

if istrue:
    print("დრო ამოიწურა, თქვენ დამარცხდით")

## 8 ორი მოთამაშე იწყებს "გარბენს". უნდა შეამოწმო რომელი დაასრულებს ნაკლებ დროში
start = timedelta(seconds=0)
player1 = start + timedelta(seconds=random.randint(5,20))
player2 = start + timedelta(seconds=random.randint(5,20))

#შესამოწმებლად
# print(player1,player2)

if player1>player2:
    print("player2")
else:print("player1")

## 9 იღბლიანი დაბადების დღე მოთამაშემ უნდა შეიყვანოს დაბადების თარიღი და თამაში დაითვლის
#რამდენი დღეა დარჩენილი შემდეგ დაბადების დღემდე
birthday = input("შეიყვანეთ თქვენი დაბადების დღე:(D/M/Y) ")
birthday = datetime.strptime(birthday,"%d/%m/%Y")
today = datetime.today()

if today.month>birthday.month:
    birthday = datetime(today.year+1,birthday.month,birthday.day)
else:
    birthday = datetime(today.year, birthday.month, birthday.day)

print((birthday-today).days + 1)

###10 საცავი - ჯუნიორ ჰაკერი :)თამაში არის შემდეგი - გვაქვს სეიფი რომელსაც აქვს ციფრები 1-6 მდე
# პაროლი არ ვიცით, ყოველ დღე კომპიუტერი აგენერირებს ახალ პაროლს (შემთხვევითობის პრინციპით)
# პაროლი არის 4 ციფრიანი. ჩვენი მიზანია დავწეროთ ისეთი კოდი რომელიც შეამოწმებს ვარიანტებს და
# როცა მოხდება კომპიუტერის მიერ დაგენერირებული პაროლის დამთხვევა უნდა გამოვიტანოთ შეტყობინება "პაროლი სწორია
# , საცავი გახსნილია", აუცილებელი პირობაა გამოვიტანოთ ყველა ჩვენს მიერ ნაცადი პაროლი სანამ მივალთ სწორ ვარიანტამდე.

mylist = [1,2,3,4,5]
pswd = random.sample(mylist,k=4)
for x in permutations(mylist,4):
    if list(x) == pswd:
        print(f"პაროლი {x} სწორია, საცავი გახსნილია")
        break
    else:
        print(x)
