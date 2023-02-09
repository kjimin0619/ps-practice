import sys

students = set()
allStudents = set(i for i in range(1,31))

for _ in range(28) : 
    i = int(sys.stdin.readline())
    students.add(i)
    
s = allStudents - students
s = sorted(s)
print(s[0])
print(s[1])
