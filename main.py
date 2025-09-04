## 7 თამაში უკუსვლაზე
# კომპიუტერი ირჩევს შემთხვევითობის პრინციპით რიცხვს 1-20 მდე,
# მოთამაშეს აქვს მხოლოდ 5 წამი რიცხვის გამოსაცნობად, თუ 5 წამში
# სწორ რიცხვს ვერ შეიყვანს, თამაში სრულდება და გამოდის ტექსტი "დრო ამოიწურა, თქვენ დამარცხდით".

x = random.randint(1,20)
print(x)
start = datetime.now().second
istrue = True
myinput = int(input("შეიყვანე რიცხვი სწრაფად: "))
while True:
    if datetime.now().second - start > 5:
        print("დრო ამოიწურა, თქვენ დამარცხდით")
        quit()
    if myinput == x:
        print("CORRECT!!!")
        break
    myinput = int(input("შეიყვანე რიცხვი სწრაფად: "))
