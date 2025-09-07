import  random
from itertools import product

def guess_rank(c,n = 1):
    counts = 0
    for i in range(n):
        if type(c[i][0]) == int:
            counts += c[i][0]
        else:
            if c[i][0] == "Jack" or c[i][0] == "Queen" or c[i][0] == "King":
                counts += 10
            else:
                counts += 11
    return counts
def delete_card(card,n=0):
    if n == 0:
        card_all.remove(card[0])
    else:
        for i in range(n):
            card_all.remove(card[i])
    return 0
def Add(random_card,n = 1):
    counts = guess_rank(random_card,n)
    delete_card(random_card)
    return counts

card_suits = ["Spades","Clubs","Diamonds","Hearts"]
card_ranks = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

istrue = True
while istrue:
    card_all = []

    for x in product(card_ranks, card_suits):
        card_all.append(x)

    rnd1 = random.sample(card_all, k=2)
    player = Add(rnd1,2)
    rnd2 = random.sample(card_all, k=2)
    computer = Add(rnd2,2)

## ვნახოთ პირველი ორი კარტი
    print(f"თქვენი კარტებია: {rnd1}")
## ეს კომპიუტერის კარტები დასატესტად რო გვქონდეს
    # print(f"rnd2: {rnd2}")

    strs = input("Add Or Stop: ")
    while strs == "Add":
        rnd1 = random.sample(card_all, k=1)
        player += Add(rnd1)

        if computer < 17:
            rnd2 = random.sample(card_all, k=1)
            computer += Add(rnd2)

        strs = input("Add Or Stop: ")

## ეს პრინტი რო ვიცოდეთ ხოარ ვტყუვდებით
    print(player)
    print(computer)

    istrue = False
    if computer < player <= 21:
        print("თქვენ მოიგეთ")
    elif player < computer <= 21:
        print("თქვენ წააგეთ")
    elif player <= 21 < computer:
        print("თქვენ მოიგეთ")
    elif player == computer:
        istrue = True
        print("ფრე. დაიწყეთ თამაში თავიდან.\n")
    else:
        print("თქვენ წააგეთ")