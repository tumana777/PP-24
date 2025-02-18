from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")

db = client["PP-24"]

students = db["students"]

# for student in students.find():
#     print(student)

# student = {"name": "Giorgi Petuashvili", "email": "test@gmail.com"}

# students.insert_one(student)

# student_list = [
#     {"name": "Ana", "age": 18},
#     {"name": "Niko", "age": 25},
#     {"name": "Dato", "age": 20},
#     {"name": "Leqso", "age": 23},
#     {"name": "Nino", "age": 28}
# ]
#
# students.insert_many(student_list)

# for student in students.find({"name": "Leqso"}):
#     print(student)

# for student in students.find({"age": {"$gt": 25}}):
#     print(student)

# for student in students.find({"age": {"$gte": 25}}):
#     print(student)

# for student in students.find({"age": {"$lte": 25}}):
#     print(student)

# for student in students.find({"$or": [{"age": {"$lt": 20}}, {"age": {"$gt": 25}}]}):
#     print(student)

# students.update_one({"name": "Leqso"}, {"$set": {"name": "Alex"}})

# students.update_many({"name": "Alex"}, {"$set": {"name": "Leqso"}})

# students.update_many({}, {"$set":{"name":"moswavle"}})

# students.delete_many({})