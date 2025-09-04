import random
from datetime import datetime
from itertools import permutations
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


