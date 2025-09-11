import json
from email.contentmanager import raw_data_manager
# import requests

#1 SQL დავალება
# გამოიტანე ProductName, CategoryID, Unit, Price ცხრილი- “პროდუქტები
# სადაც ფასი მოთავსებული 18-სა და 25-ს შორის
# დაალაგე კლებადობით ფასის მიხედვით

# SELECT ProductName,CategoryID,Unit,Price FROM Products
# WHERE Price>18 AND Price < 25
# ORDER BY Price DESC

#2 SQL დავალება2
# გამოიტანე ყველა ველი, სადაც რაოდენობა ტოლია 15-ის ან 12-ის
# დაალაგე ზრდადობით
# ცხრილი - “OrderDetails”

# SELECT * FROM OrderDetails
# WHERE Quantity = 15 OR Quantity = 12
# ORDER BY Quantity ASC

#3 მოცემულია JSON მასივი:
# ამოიღე მხოლოდ ის პროდუქტები, რომელთა ფასი 100-ზე მეტია.
# data = '''
# [
#     {"id": 1, "price": 50},
#     {"id": 2, "price": 200},
#     {"id": 3, "price": 150}
# ]
# '''
# parsed = json.loads(data)
# iD = [d["id"] for d in parsed if int(d["price"]) > 100]
# print(iD)

# 4 მოცემულია რთული JSON:
# ამოიღე ყველა თანამშრომლის სახელი
# mydata = '''{
#     "company": {
#         "departments": [
#             {
#                 "name": "IT", "employees": [{"name": "Ana"}, {"name": "Beka"}]
#             },
#             {
#                 "name": "HR", "employees": [{"name": "Nino"}]
#             }
#         ]
#     }
# }'''
# parsed = json.loads(mydata)
# arr = parsed["company"]["departments"]
# name = [data["employees"] for data in arr]
# for data in name:
#     for i in range(len(data)):
#         print(data[i]["name"],end=" ")

#5 მოცემულია სტუდენტების სია:
# იპოვე სტუდენტი, რომელსაც აქვს საშუალო ქულის მიხედვით საუკეთესო შედეგი.
#
# mydata = """[
#     {"name": "Ana", "grades": [90, 80, 95]},
#     {"name": "Beka", "grades": [70, 85, 88]},
#     {"name": "Nino", "grades": [100, 95, 99]}
# ]"""
# parsed = json.loads(mydata)
# mx = 0
# counts = 0
# name = ""
# for student in parsed:
#     counts = sum(student["grades"]) / 3
#     if counts > mx:
#         mx = counts
#         name = student["name"]
# print(name)
#
#
#6 მოცემულია კომპანიების სია:
# იპოვე ყველა თანამშრომელი, რომლის ხელფასი მეტია 4000-ზე და დაბეჭდე
# მათი სახელები + კომპანიის სახელი.

# mydata = '''{
#     "companies": [
#         {
#             "name": "TechCorp",
#             "employees": [
#                 {"name": "Ana", "salary": 3000},
#                 {"name": "Beka", "salary": 4500}
#             ]
#         },
#         {
#             "name": "SoftPlus",
#             "employees": [
#                 {"name": "Nino", "salary": 5000},
#                 {"name": "Giorgi", "salary": 2500}
#             ]
#         }
#     ]
# }'''
# parsed = json.loads(mydata)
# arr = parsed["companies"]
#
# for comp in arr:
#     for emp in comp["employees"]:
#         if emp["salary"] > 4000:
#             print(emp["name"] + " company: " + comp["name"])
#
#7 გააგზავნე GET მოთხოვნა https://jsonplaceholder.typicode.com/users და
# დაბეჭდე პირველი მომხმარებლის სახელი.
# resp = requests.get("https://jsonplaceholder.typicode.com/users")
# resp = resp.json()
# print(resp[0]["name"])
#
#8 გააგზავნე POST მოთხოვნა https://jsonplaceholder.typicode.com/posts და
# შექმენი ახალი პოსტი შემდეგი მონაცემებით:
# newlist = {"title": "Test", "body": "Hello World", "userId": 5}
# resp = requests.post("https://jsonplaceholder.typicode.com/posts",json=newlist)
# print(resp.json())

#9 წამოიღე ყველა TODO task და დაბეჭდე მხოლოდ ის, სადაც "completed": False -
# https://jsonplaceholder.typicode.com/todos
# ბოლოს დათვალე რამდენი შეუსრულებელი ტასკია (რაოდენობაში)

# resp = requests.get("https://jsonplaceholder.typicode.com/todos")
# resp = resp.json()
# counts = 0
# for x in  resp:
#     if not x["completed"]:
#         print(x)
#         counts += 1
# print(counts)

# #10 ამოიღე ყველა პოსტი https://jsonplaceholder.typicode.com/posts, შემდეგ
# იპოვე ავტორის სახელი (users API-დან) და დაბეჭდე:
# "Post Title – Author Name"
# გამოიტანე მხოლოდ პირველი 5

# resp = requests.get("https://jsonplaceholder.typicode.com/posts")
# resp = resp.json()
# for x in resp:
#     print(f'Post Title – {x["title"]}')