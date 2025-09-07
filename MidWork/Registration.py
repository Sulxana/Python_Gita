import string

mydict = {
    "ელ-ფოსტა" : "mevargiorgi@gmail.com",
    "სახელი" : "",
    "ზედმეტსახელი" : "giusha007",
    "პაროლი" : "password123"
}
s = string.punctuation

while True:
    strs = input("შეიყვანეთ მომხმარებლის სახელი: ")
    if not strs.isascii():
        print("შემოყვანილია სხვა ენა. შეიყვანეთ მხოლოდ ლათინური პატარა რეგისტრის ასოები")

    elif strs.isalpha() and strs.lower()==strs:
        break

    elif strs.isnumeric() :
        print("შემოყვანილია რიცხვითი მნიშვნელობა, შემოიტანეთ მხოლოდ string პატარა რეგისტრში!!!")

    elif strs.isalpha() and strs.upper() == strs:
        print("შემოყვანილია ლათინური დიდი ასოები")

    elif not strs.lower() == strs:
        num = False
        punct = False
        for x in strs:
            if x.isnumeric():
                num = True
            elif s.find(x)!=-1:
                punct = True

        if num and not punct:
            print("შემოყვანილია ლათინური დიდი და პატარა ასოები და რიცხვები")
        elif punct and not num:
            print("შემოყვანილია ლათინური დიდი და პატარა ასოები და სიმბოლოები")
        elif num and punct:
            print("შემოყვანილია ლათინური დიდი და პატარა ასოები, რიცხვები და სიმბოლოები")
        else:
            print("შემოყვანილია ლათინური დიდი და პატარა ასოები")

    else:
        print("შემოყვანილია სიმბოლოები, შემოიტანეთ მხოლოდ string პატარა რეგისტრში!!!")
mydict["სახელი"] = strs
print(mydict)