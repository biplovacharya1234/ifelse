employee = {
    "name": "Biplov",
    "age": "25",
    "job_role": "Python developer"
}
print(employee.get("name"))
print(employee.get("dob", "6th april"))
# dictionary elements can be updated
employee["name"] = "Biplov Aharya"
print(employee.get("name"))


numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
output = ""
phone = input("Enter your phone number")
for character in phone:
    output += numbers.get(character) + " "
print(output)
