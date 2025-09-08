import logging
import random
from itertools import permutations

logging.basicConfig(filename="game.log", level=logging.INFO, encoding="UTF-8")


# 1 შექმენი გენერატორი, რომელიც ტექსტის თითოეულ სიმბოლოს აბრუნებს.
def funct(x):
    for i in x:
        print(i)
        yield 1


Word = "CODE"
w = funct(Word)
for i in range(len(Word)):
    next(w)

#
# 2 დაწერე პროგრამა რომელშიც მომხმარებელი შემოიყვანს მხოლოდ ციფრებს, ლოგიკა
# უნდა იყოს შემდეგი: გვაქვს კონკრეტული ლისტი და მომხმარებელი უნდა მიწვდეს
# შემოყვანილი ციფრით რომელიმე ელემენტს, თუ ვერ მიწვდება პროგრამა შეცდომაზე არ
# უნდა გავიდეს.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
try:
    num = int(input("შეიყვანე ინდექსი: "))
    print(arr[num])
except:
    print("შეყვანილი ციფრი ცდება საზღვრებს")


# 3 ვერ გავაკეთე
def counter(func):
    def wrapper():
        func()
        print("S")

    return wrapper


@counter
def say():
    print("Hi")


say()
say()

# 4 მომხმარებელს უნდა დავუსვათ 5 მათემატიკური შეკითხვა, თითოეულზე სწორი
# პასუხი არის 10 ქულა ხოლო არასწორი 0 ქულა, მიღებული პასუხებიდან უნდა
# განვსაზღვროთ რამდენი ქულა აიღო მომხმარებელმა, შევქმნათ ლოფ ფაილი
# game.log და შევინახოთ ყველა ქულა. ბოლოს გამოვუტანოთ მიღებული შედეგი

#
question = ["რას უდრის 8 * 7? ", "რას უდრის 100-ის 30%? ", "რას უდრის 111 - 12? ", "რას უდრის 13 // 2? ",
            "რას უდრის 13 % 2? "]
answers = [56, 30, 99, 6, 1]
counts = 0
for i in range(5):
    q = int(input(question[i]))
    if q == answers[i]:
        counts += 10
        logging.info(f"შენ {i + 1} კითხვაზე პასუხით დააგროვე 10 ქულა.")
    else:
        logging.info(f"შენ {i + 1} კითხვაზე პასუხით დააგროვე 0 ქულა.")
logging.info(f"შენ სულ მოაგროვეთ {counts} ქულა")
print(f"შენ სულ მოაგროვეთ {counts} ქულა")

# 5 შექმენით ფაილი quiz.log, შექმენით გენერატორი რომელშიც შენახული იქნება
# 5 შეკითხვა და სათითაოდ დააბრუნებს, მომხმარებელმა უნდა უპასუხოს ყველა
# შეკითხვას და პასუხები შეინახეთ ლოგ ფაილში.
logging.basicConfig(filename="quiz.log", level=logging.INFO, encoding="UTF-8")


def funct(a):
    for x in a:
        yield x


question = ["რას უდრის 8 * 7? ", "რას უდრის 100-ის 30%? ",
            "რას უდრის 111 - 12? ", "რას უდრის 13 // 2? ", "რას უდრის 13 % 2? "]
trying = funct(question)
for i in range(5):
    strs = int(input(next(trying)))
    logging.info(f"თქვენი პასუხი კითხვაზე {question[i]} არის {strs}.")

# 6 შექმენი პროგრამა სადაც მომხმარებელი ეჯიბრება კომპიუტერს: ქვა/ბადე/
# მაკრატელის თამაშში, თამაში არის სამამდე, კომპიუტერი შემთხვევითობის
# პრინციპით ირჩევს ამ სამიდან 1-ს , ასევე ტერმინალში მომხმარებელი წერს ერთ-
# ერთს, ერთნაირის შემთხვევაში ფრეა და გრძელდება თამაში 3-მდე, ვინც პირველი
# მიაღწევს 3-ს გამოიტანე შეტყობინება .....-მ გაიმარჯვა, ყველა ნათამაშები ხელი
# უნდა შეინახოო ლოგირების ფაილში.

player = 0
computer = 0
trying = ["ქვა", "ბადე", "მაკრატელი"]

while True:
    if player == 3:
        logging.info("გაიმარჯვე შენ")
        break
    if computer == 3:
        logging.info("გაიმარჯვა კომპიუტერმა")
        break

    p = input("აირჩიე ქვა/ბადე/მაკრატელი: ")
    c = random.sample(trying, k=1)
    c = "".join(c)

    if p == c:
        logging.info("ფრეა")
        continue
    if p == "ქვა" and c == "მაკრატელი":
        player += 1
        logging.info(f"ანგარიში: {player} - {computer}")
    elif p == "ქვა" and c == "ბადე":
        computer += 1
        logging.info(f"ანგარიში: {player} - {computer}")
    elif p == "ბადე" and c == "მაკრატელი":
        player += 1
        logging.info(f"ანგარიში: {player} - {computer}")
    elif p == "ბადე" and c == "ქვა":
        player += 1
        logging.info(f"ანგარიში: {player} - {computer}")
    elif p == "მაკრატელი" and c == "ქვა":
        computer += 1
        logging.info(f"ანგარიში: {player} - {computer}")
    elif p == "მაკრატელი" and c == "ბადე":
        computer += 1
        logging.info(f"ანგარიში: {player} - {computer}")
#
#
# 7 პროგრამა კამათელზე - გვყავს ორი მომხმარებელი Gamer 1 & Gamer 2,
# თითოეულს უნდა გავაგორებინოთ კამათელი თითო თითოჯერ, თუ ფრეა ვიმეორებთ,
# სხვა შემთხვევაში მოგებულ მოთამაშეს უნდა ვკითხოთ კიდევ 1 შანსს მისცემს თუ
# არა წაგებულს და კიდევ გააგორებს თუ არა, თუ უარია ვამთავრებთ, თუ თანახმაა
# იგივე ლოგიკა უნდა გაგრძელდეს სანამ უარს არ იტყვის ერთ-ერთი.

Gamer1 = 0
Gamer2 = 0
mylist = list(range(1, 7))
while True:
    guess1 = random.sample(mylist, k=1)
    guess2 = random.sample(mylist, k=1)
    print(guess1, guess2, end=" ")
    print()
    if guess1 > guess2:
        strs = input("მოიგო პირველმა. მისცემ კიდევ 1 შანს მეორე მოთამაშეს? (კი/არა) ")
    elif guess1 < guess2:
        strs = input("მოიგო მეორემ. მისცემ კიდევ 1 შანს პირველ მოთამაშეს? (კი/არა) ")
    else:
        print("ფრეა")
        continue
    if strs == "არა":
        break

# 8 შექმენი პროგრამა სადაც გექნება გადაცემული 10 სიტყვა ლისტში და ლოგიკა
# არის შემდეგი, ამ სიტყვებიდან 2 ცალს ირჩევ შემთხვევითობის პრინციპით და
# თითოეული სიტყვიდან უნდა ამოაკლო 2 ასო და მომხმარებელს აჩვენო მსგავსი
# ფორმით და უთხრა რომ გამოიცნოს სიტყვა და ჩაწეროს სრულად, თუ გამოიცნო
# “გამარჯვება” თუ ვერ გამოიცნო ვერცერთი სიტყვა “დამარცხდი”, ერთის
# გამოცნობის შემთხვევაში “50%”

mylist = ["Lantern", "horizon", "marble", "whisper", "falcon", "meadow", "compass", "drift", "puzzle", "thunder"]
newlist = random.sample(mylist, k=2)
counts = 0
for i in range(2):
    word1 = newlist[i]
    word2 = list(newlist[i])
    for _ in range(2):
        c = random.randint(0, len(word2) - 1)
        word2[c] = "_"
    strs = "".join(word2)

    guess = input(f"guess the character {strs}: ")
    if word1 == guess:
        counts += 1

if counts == 2:
    print("გამარჯვება")
elif counts == 1:
    print("50%")
else:
    print("დამარცხება")