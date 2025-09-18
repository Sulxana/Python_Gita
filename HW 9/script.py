import random
import string
from itertools import product
#1 შექმენი თამაში
# შექმენით Character კლასი (სახელი, სიცოცხლე, ძალა)
# გააკეთეთ მემკვიდრეები: Warrior, Mage, Archer
# გამოიყენეთ super() რომ მშობლის კონსტრუქტორი გამოიძახოთ
# თამაში: ორი გმირი ებრძვის ერთმანეთს (attack() მეთოდი).
# Warrior სჯობს Mage-ს , Mage სჯობს Archer-ს, Archer სჯობს Warrior-ს
# ტესტირების დროს სცადე სამივე ვარიანტი, ანუ როცა ერთმანეთზე გააკეთებინებ შეტევას 1 უნდა
# დამარცხდეს და 1მა გაიმარჯვოს, ეს უნდა გამოიტანო ტერმინალში. ზედმეტი ვალიდაციები და
# პირობის შეცვლა არაა საჭირო. რაც პირობაში წერია ამ მონახაზით გააკეთეთ თავისუფლად.
class Character:
    def __init__(self,name,life,strength):
        self.name = name
        self.life = life
        self.strength = strength

class Warrior(Character):
    name_w = "Warrior"
    def __init__(self, name, life, strength):
        super().__init__(name, life, strength)

class Mage(Character):
    name_m = "Mage"
    def __init__(self,name,life,strength):
        super().__init__(name, life, strength)

class Archer(Character):
    name_a = "Archer"
    def __init__(self,name,life,strength):
        super().__init__(name, life, strength)

def attack(x,y):
    if type(x) == Warrior and type(y) == Mage or type(x) == Mage and type(y) == Warrior:
        print("გაიმარჯვა Warrior-მა")
    elif type(x) == Archer and type(y) == Warrior or type(x) == Warrior and type(y) == Archer :
        print("გაიმარჯვა Archer-მა")
    elif type(x) == Mage and type(y) == Archer or type(x) == Archer and type(y) == Mage:
        print("გაიმარჯვა Mage-მა")


w = Warrior("vercxli",15,25)
m = Mage("oqro",20,50)
a = Archer("brinjao",30,12)

attack(a,m)
attack(w,m)
attack(w,a)

#2 პატარა პროგრამა მონსტრებზე
# თქვენი ვალია შექმნათ მონსტრების ქარხანა სადაც:
# შექმენით Monster კლასი.
# დაამატეთ classmethod create_from_level(level), რომელიც ქმნის მონსტრს სიძლიერის
# მიხედვით.
# სხვადასხვა level -> სხვადასხვა ტიპის მონსტრი.
# შექმენი მინიმუმ 10 მონსტრი რომლებსაც ექნებათ სახელები, სახელები არ უნდა იყოს ბოროტული :)
# (ეს მონსტრები ეხმარებიან ადამიანებს) “აქაც იგივე” არაა საჭირო ზედმეტი ვალიდაციები და პირობის
# ცვლილება. ამ მონახაზში იმუშავეთ თავისუფლად.
class Monster:
    def __init__(self,name,level):
        self.name = name
        self.level = level

    def __str__(self):
        return f"{self.name} {self.level}"

    def helping_humans(self):
        return "davexmareebito"

    @classmethod
    def create_from_level(cls,level):
        monsters = ["Snargle Fartclaw", "Wobbletooth the Hungry", "Blubberpuff Doomface", "Sir Slime-a-Lot",
                    "Chonkzilla", "Burpfang the Fearsome", "Grumbleflop the Sleeper", "Puddlebutt Creepster",
                    "Ticklefang McSpooky", "Boogersnort the Mighty"]
        return cls(f"{random.choice(monsters)}",level)

for i in range(1,11):
    m = Monster.create_from_level(i)
    print(m,m.helping_humans())

##3 მარტივი კაზინო თამაში
# შექმენით SlotMachine კლასი.
# გამოიყენეთ staticmethod შემთხვევითი სიმბოლოების დასაგენერირებლად.
# გამოიყენეთ classmethod from_difficulty(level) -> უფრო რთული დონის სლოტები
# მოთამაშე მოიგებს თუ სამივე სიმბოლო დაემთხვევა.
# აუცილებლად გატესტეთ, სცადეთ რამოდენიმე ვარიანტის გაშვება.
num = string.digits
class SlotMachine:

    @staticmethod
    def make_random():
        return random.sample(num, k=3)

    @classmethod
    def from_difficulty(cls,level):
        new = string.digits
        if level == 1:
            new += string.ascii_lowercase
            return random.sample(new, k=3)
        elif level == 2:
            new += string.ascii_letters
            return random.sample(new, k=3)
        else:
            new += string.ascii_letters + string.punctuation
            return random.sample(new, k=3)

q = input("აირჩევ ლეველს? კი/არა ")
lucky = SlotMachine.make_random()
if q == "კი":
    n = int(input("აირჩიე სირთულის ლეველი (1/2/3): "))
    lucky = SlotMachine.from_difficulty(n)

print(lucky)
counts = 0
for i in range(3):
    x = input("შეიყვანე სიმბოლო: ")
    if lucky.count(x) >= 1:
        counts += 1
    else:
        break
if counts == 3:
    print("მოიგე")
else:
    print("წააგე")

#4 გმირის ქულების სისტემა
# შექმენით Hero კლასი.
# private health, private score.
# staticmethod random_event() -> შემთხვევითი მოვლენა (ქულა ემატება ან ჯანმრთელობა
# აკლდება).
# classmethod from_name(cls, name) -> ქმნის გმირს სახელით.
# მემკვიდრე SuperHero -> დამატებითი ძალა.
# super() გამოიძახეთ მშობლის კონსტრუქტორისთვის.
# თამაში გრძელდება სანამ გმირის health > 0.
class Hero:
    def __init__(self,name,health = 100,score = 0):
        self.name = name
        self.__health = health
        self.__score = score

    @property
    def get_health(self):
        return self.__health

    @get_health.setter
    def get_health(self,heal):
        self.__health -= heal

    @property
    def get_score(self):
        return self.__score

    @get_score.setter
    def get_score(self, sc):
        self.__score += sc

    @staticmethod
    def random_event(herou):
        n = [1,2]
        if random.choice(n) == 1:
            herou.get_score = 5
        else:
            herou.get_health  = 10

    @classmethod
    def from_name(cls, name):
        return cls(name)

class SuperHero(Hero):
    def __init__(self, name, health = 100,score = 10):
        super().__init__(name,health,score)

h = Hero.from_name("Giusha")
s = SuperHero.from_name("dzlieri")

#ვნახოთ რომ ნამდვილად უფრო ძლიერია
print(h.get_score,s.get_score)

while h.get_health > 0:
    Hero.random_event(h)
    print(f"score = {h.get_score}; health = {h.get_health}")

#5 პროგრამა კარტზე
# Card კლასი (rank, suit).
# Deck კლასი -> private cards list.
# classmethod create_standard_deck() აბრუნებს სტანდარტულ 52 კარტიან დასტას.
# staticmethod shuffle(cards) აურევს კარტებს.
# მოთამაშე იღებს 5 კარტს და ამოწმებს, აქვს თუ არა “მარტივი კომბინაცია” (მაგ: ორი ერთნაირი)
class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} {self.suit}"

class Deck:
    def __init__(self, ranks, suits):
        self.rank = ranks
        self.suit = suits
        self.__cards = [Card(r, s) for r, s in product(ranks, suits)]

    def get_cards(self):
        return  self.__cards

    @classmethod
    def create_standard_deck(cls):
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        return cls(ranks, suits)

    @staticmethod
    def shuffle(x):
        s = random.sample(Deck.get_cards(x),k=52)
        return s

deck = Deck([1,"J", "Q"], ["Hearts", "Clubs",])
print(f"ჩემი შედგენილი: {deck.get_cards()}")

whole = Deck.create_standard_deck()
print(f"მთლიანი დასტა: {whole.get_cards()}")

whole = Deck.shuffle(whole)
print(f"აჩეხილი დასტა: {whole}\n")

mylist = []
for i in range(5):
    if mylist.count(whole[i].rank):
        print("აქვს მარტივი კომბინაცია")
    mylist.append(whole[i].rank)
print(mylist)