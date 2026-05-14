# students = ["Hermione", "Harry", "Ron"]

# # for student in students:
# #     print(student)

# for i in range(len(students)):
#     print(i+1, students[i])



# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherine"
# }

# for student in students:
#     print(student, students[student], sep=",")

students = [
     {"name":"Hermione", "house": "Gryffindor", "patronous": "otter"},
     {"name":"Harry", "house": "Gryffindor", "patronous": "stag"},
     {"name":"Ron", "house": "Gryffindor", "patronous": "jack russel terrier"},
     {"name":"Draco", "house": "Slytherine", "patronous": None},
     
]


for student in range(len(students)):
    print(student,*students[student].values())