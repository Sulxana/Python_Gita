# ამოცანა 1
import string,random

# ვარიანტი 1 - ვეკითხები თითოეულ ნაბიჯზე მომხმარებელს სურს თუარა თვითონ მიიღოს მონაწილეობა.

length = int(input("რა სიგრძის პაროლის დაყენება გსურთ?: "))
language = input("რა ენაზე გსურთ პაროლის გენერირება? (ქართული/ინგლისური): ")
if language == "ქართული":
    print("ამ ეტაპზე მხოლოდ ლათინური ასოებით შეგვიძლია შევქმნათ პაროლი.")
Characters = input("აირჩიეთ ასოების ზომა: (დიდი და პატარა / პატარა / დიდი) ")
s = input("გსურთ თუარა სიმბოლოების გამოყენება? (კი/არა): ")
nums = input("გსურთ თუარა რიცხვების  გამოყენება? (კი/არა): ")

symbols = ["!","@","#","$","%","^","&","*","~"]
if Characters == "დიდი და პატარა":
    big_small = string.ascii_letters
elif Characters == "დიდი":
    big_small = string.ascii_uppercase
else :
    big_small = string.ascii_lowercase

if s == "კი":
    symbols = "".join(symbols)
    big_small+=symbols
    kitxva_1 = input("გსურთ ასოების და სიმბოლოების თქვენთითონ შემოტანა თუ ჩვენ დავაგენერიროთ?: (ჩემით/თქვენ)")
else:
    kitxva_1 = input("გსურთ ასოების თქვენთითონ შემოტანა თუ ჩვენ დავაგენერიროთ?: (ჩემით/თქვენ)")


list_asoebi = []

if nums == "კი":
    kitxva_2 = input("გსურთ რიცხვების თქვენთითონ შემოტანა თუ ჩვენ დავაგენერიროთ?: (ჩემით/თქვენ) ")

    if kitxva_1 == "ჩემით" and kitxva_2 == "ჩემით":
        for i in range(length):
            c = input("შეიყვანე ასო, სიმბოლო ან ციფრი: ")
            list_asoebi.append(c)

    elif kitxva_1 == "ჩემით" and kitxva_2 == "თქვენ":
        for i in range(length//2+1):
            c = input("შეიყვანე ასო ან სიმბოლო: ")
            list_asoebi.append(c)
            if i % 2 == 0:
                list_asoebi.append(str(random.randint(0, 9)))

    elif kitxva_1 == "თქვენ" and kitxva_2 == "ჩემით":
        for i in range(length//2+1):
            c = input("შეიყვანე ციფრი: ")
            list_asoebi.append(c)
            if i % 2 == 0:
                list_asoebi.append("".join(random.sample(big_small,k=1)))

    else:
        big_small+=string.digits
        list_asoebi.append("".join(random.sample(big_small,k=length)))

else:
    if kitxva_1 == "ჩემით":
        for i in range(length):
            c = input("შეიყვანე ასო ან სიმბოლო: ")
            list_asoebi.append(c)
    else:
        list_asoebi = "".join(random.sample(big_small,k=length))
final = "".join(list_asoebi)
print(final)

# ვარიანტი 2 - მომხმარებელს შემოაქ character-ები და ვაგენერირებთ რანდომ პაროლს

length = int(input("რა სიგრძის პაროლის დაყენება გსურთ?: "))
mylist = []
i = 0
characters = string.ascii_letters+string.digits+string.punctuation
while i < length:
    char = input("შეიყვანე ნებისმიერი ასო ლათინურ ენაზე, სიმბოლო ან ციფრი: ")
    if not characters.count(char):
        print("შეიყვანე მხოლოდ ლათინური ასოები")
        continue
    mylist.append(char)
    i+=1
strs = "".join(random.sample(mylist,k=length))
print(strs)

# ამოცანა 2

pswd = input("შეიყვანეთ პაროლი: ")
count = 0
# სიგრძის მიხედვით ვწერ ქულას
if len(pswd) >= 15:
    count+=2
elif len(pswd)>=8:
    count+=1

mylist = list(pswd)
num = 0
up = 0
punct = 0
for i in range(len(pswd)):
    if string.digits.count(mylist[i]):
        num+=1
    elif string.ascii_uppercase.count(mylist[i]):
        up+=1
    elif string.punctuation.count(mylist[i]):
        punct+=1

# ციფრების რაოდენობით ვწერ ქულას
if num>=4:
    count+=2
elif num>0:
    count+=1

# დიდი ასოების რაოდენობით ვწერ ქულას
if up >=3:
    count+=2
elif up > 0:
    count+=1

# სიმბოლოების რაოდენობით ვწერ ქულას
if punct >=2:
    count+=2
elif punct >0:
    count+=1

# განმეორებადი ასოების რაოდენობით ვწერ ქულას
st = set(mylist)
if len(mylist)-len(st) <= 4:
    count+=2
elif len(mylist)-len(st) <= 6:
    count+=1

if count >= 8:
    print("Strong")
elif count >= 5:
    print("Medium")
else: print("Weak")

# ამოცანა 3

def funct(x):
    a = 0
    b = 1
    ln = 2
    while ln != x:
        a, b = b, a + b
        ln += 1
    return b

Characters = string.punctuation
num = input("შემოიყვანე რიცხვი: ")
while not num.isnumeric():
    if num.isalpha():
        print("შენ შემოიყვანე ასოები. შემოიყვანე მხოლოდ რიცხვი!!!")
    elif Characters.count(num):
        print("შენ შემოიყვანე სიმბოლო. შემოიყვანე მხოლოდ რიცხვი!!!")
    else:
        print("შენ შემოიყვანე არასწორი მნიშვნელობა. შემოიყვანე მხოლოდ რიცხვი!!!")
    num = input("შემოიყვანე რიცხვი: ")

num = int(num)
print(funct(num))

# ამოცანა 4
strs = input("შემოიყვანე სიტყვა/რიცხვი: ")
r_str = strs[::-1]
if strs == r_str:
    print(True)
else:
    pass

# ამოცანა 5
strs = input("შემოიყვანე სიტყვა: ")
while strs.count(" ")!=0:
    strs = input("შემოიყვანე მხოლოდ ერთი სიტყვა: ")

mylist = list(strs)
for i in range(5):
    new = "".join(random.sample(mylist,k=len(mylist)))
    print(new)

# ამოცანა 6
st = set()
while True:
    strs = input("შემოიყვანე რიცხვი:")
    newlist = strs.split()

    for i in range(len(newlist)):
        st.add(int(newlist[i]))

    mylist = list(st)
    mylist = sorted(mylist)

    r_mylist = mylist.copy()
    r_mylist.reverse()

    rand_mylist = random.sample(mylist,k=len(mylist))
    q = input("როგორ გსურთ რომ დავასორტიროთ? (კლებადობით/ზრდადობით/რანდომად): ")

    if q == "ზრდადობით":
        print(st)
    elif q == "კლებადობით":
        print(r_mylist)
    else:
        print(rand_mylist)

# ამოცანა 7

strs = input("შეიყვანე ტექსტი: ")
mylist = []
for s in strs:
    if s.isalpha() or s.isspace():
        mylist.append(s)
print("".join(mylist))

# ზუსტად იგივე ლოგიკაა უბრალოდ თავიდან ესე გავაკეთე ლისტებად შემოვიტანე და მერე მივხვდები რო პირდაპირ შემეძლო

strs = list(input("შეიყვანე ტექსტი: "))
mylist = []
for i in range(len(strs)):
    if strs[i].isalpha() or strs[i].isspace():
        mylist.append(strs[i])
print("".join(mylist))

# ამოცანა 8

strs = input("შემოიტანეთ სია: ")
mylist = strs.split()
mylist = [int(s) for s in mylist]

for i in range(len(mylist)-1):
    newlist = []
    for j in range(len(mylist)-1):
        newlist.append(mylist[j]+mylist[j+1])
    mylist = newlist
    print(newlist)

# ამოცანა 9

strs = input("შეიყვანე ტექსტი:").lower()
mylist = strs.split()
word = []
mx = 0

for s in mylist:
    total = mylist.count(s)

    if total > mx:
        mx = total
        while word:
            word.pop()
        word.append(s)

    elif total == mx and word.count(s)==0:
        word.append(s)
print(word)

# ამოცანა 10

strs = input("შეიყვანე წინადადება:")
mylist = strs.split()
mydict = {}
for s in mylist:
    mydict[s] = len(s)
print(mydict)

