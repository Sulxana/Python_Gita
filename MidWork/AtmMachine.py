import logging
logging.basicConfig(filename = "app.log",level=logging.INFO, encoding="utf-8")

def islari(c):
    if c.find("ლარი") != -1:
        indx = c.find("ლარი")
        c = int(c[0:indx])
        return c
    return 0

x = 1350
print()
print("გამარჯობა.",end=" ")
while True:
    strs = input("თქვენ შეგიძლიათ თანხის: გატანა, შემოტანა და ბალანსის ნახვა. აირჩიეთ ერთ-ერთი: ")
    if strs == "გატანა":
        num = input("რა თანხის გატანა გსურთ? ")
        if islari(num):
            num = islari(num)
            while num > x:
                q = input("თქვენ არ გაქვთ საკმარისი ბალანსი. გსურთ თავიდან ცდა?(კი/არა) ")
                if q == "კი":
                    num = input("რა თანხის შემოტანა გსურთ? ")
                    if islari(num):
                        num = islari(num)
                else:
                    break

            if num <= x:
                x -= num
                logging.info(f"თქვენ გაიტანეთ {num} ლარი")

        else:
            print("თქვენ შემოიტანეთ არასწორი ვალუტა")

    elif strs == "შემოტანა":
        num = input("რა თანხის შემოტანა გსურთ? ")
        if islari(num):
            num = islari(num)
            while num > 1000:
                q = input("თქვენ არ გაქვთ 1000 ლარზე მეტის შემოტანის შესაძლებლობა. გსურთ თავიდან ცდა?(კი/არა) ")
                if q == "კი":
                    num = input("რა თანხის შემოტანა გსურთ? ")
                    if islari(num):
                        num = islari(num)
                else:
                    break
            if num <= 1000:
                x += num
                logging.info(f"თქვენ შემოიტანეთ {num} ლარი")
        else:
            print("თქვენ შემოიტანეთ არასწორი ვალუტა")

    else:
        print(f"თქვენი ბალანსი შეადგენს {x} ლარს")