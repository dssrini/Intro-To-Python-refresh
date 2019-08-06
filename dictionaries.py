students =["Bob", 12, "Rachel", 13, "Emily", 15]

students = {
    "Bob" : 12,
    "Rachel" : 13,
    "Emily" : 15
}
print students
print students["Bob"]
print students["Rachel"]

students["Rachel"] = 20
print students["Rachel"]

del students["Emily"]
print students
print len(students)