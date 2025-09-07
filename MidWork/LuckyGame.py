import logging
import  random
logging.basicConfig(filename = "app.log",level=logging.INFO, encoding="utf-8")
prize = 5000
numbers = list(range(1, 50))
while True:
    mylist = random.sample(numbers, k=6)
    counts = 0
    # ჩვენთვის რო ვიცოდეთ რანდომულად არჩეული რიცხვები
    print(mylist)

    for i in range(1, 7):
        num = int(input(f"შეიყვანე რიცხვი {i}: "))
        if mylist.count(num) > 0:
            counts += 1
            mylist.remove(num)
    if counts == 6:
        logging.info(f"მომხმარებელმა დაამთხვია {counts} რიცხვი და მოიგო {prize} ლარი.")
    elif counts == 5:
        logging.info(f"მომხმარებელმა დაამთხვია {counts} რიცხვი და მოიგო {prize * 60//100} ლარი.")
    elif counts == 4:
        logging.info(f"მომხმარებელმა დაამთხვია {counts} რიცხვი და მოიგო {prize * 40//100} ლარი.")
    elif counts == 3:
        logging.info(f"მომხმარებელმა დაამთხვია {counts} რიცხვი და მოიგო {prize * 20//100} ლარი.")
    else:
        logging.info(f"მომხმარებელმა დაამთხვია {counts}. რიცხვი სამწუხაროდ თქვენ ვერ მოიგეთ.")
    print()