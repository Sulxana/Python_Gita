books = ["To Kill a Mockingbird/Harper Lee 1960","Pride and Prejudice/Jane Austen 1813",
         "Atomic Habits/James Clear 2018", "Mindset/Dr Carol Dweck 2017", "Start With Why/Simon Sinek 2011",
         "The Gifts of Imperfection/Brene Brown 2022","Big Magic/Elizabeth Gilbert 2016",
         "Feel Good Productivity/Ali Abdaal 2022", "How to be a Stoic/Massimo Pigliucci 2017",
         "Think and Grow Rich/Napoleon Hill 1937"]

print("გამარჯობა მოგესალმებით მინი ბიბლიოთეკაში.",end=" ")
while True:
    length = len(books)
    print("თქვენ შეგიძლიათ: 1) ნახოთ წიგნების სია "
          "2) მოძებნოთ წიგნი სათაურით 3) დაამატოთ სასურველი წიგნი სიაში")
    num = int(input("გთხოვთ შეიყვანოთ ციფრი, რათა დავაკმაყოფილოთ თქვენი მოთხოვნა: "))
    print()
    if num == 1:
        print(f"ამჟამად ბიბლიოთეკაში გვაქვს {length} წიგნი:")
        for index, x in enumerate(books, 1):
            indx = x.rfind(" ")
            print(f"{index}. {x[0:indx]}")
        print()
    elif num == 2:
        str = input("გთხოვთ შეიყვანოთ სასურველი წიგნის სათაური: ")
        for i in range(length):
            if books[i].__contains__(str):
                requested = books[i]
                print(f"თქვენი დასერჩილი წიგნია: {requested}.", end=" ")
                q = input("გსურთ წიგნის ბიბლიოთეკიდან გატანა წასაკითხად?(კი/არა) ")
                print()
                if q == "კი":
                    books.pop(i)
                    length -=1
                    print(f"წიგნი {requested} ბიბლიოთეკიდან გატანილია. \n")
                else:
                    print("კარგით დავბრუნდეთ ბიბლიოთეკაში.\n")
                break
    else:
        add = input("შეიყვანეთ სასურველი წიგნი: (სათაური/ავტორი და წელი) ")
        indx = add.rfind(" ")
        books.append(add)
        length +=1
        print(f"თქვენი წიგნი {add[0:indx]} დამატებულია ბიბლიოთეკაში \n")