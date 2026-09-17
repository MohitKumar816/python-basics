student = {
    "name": "Mohit",
    "age": "23",
    "course": "MCA",
}

print(student)

mobile = {}

print(mobile)

print(student["name"])
print(student["age"])
print(student["course"])

# get Method for accessing the values

print(student.get("name"))
print(student.get("age"))
print(student.get("course"))

print(student.get("city"))

#  print(student["city"])

student["city"] = "Delhi"

print(student)

student["age"] = "24"

print(student)

student.pop("city")

print(student)

student["city"] = "Delhi"

print(student)

student.popitem()

print(student)

student["city"] = "Delhi"

print(student)

del student["city"]

print(student)

