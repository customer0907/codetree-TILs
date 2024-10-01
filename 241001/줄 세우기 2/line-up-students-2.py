import sys

n = int(input())

class Student():
    def __init__(self, height, weight, idx):
        self.height = height
        self.weight = weight
        self.idx = idx

students = []

for i in range(n):
    height, weight = map(int,sys.stdin.readline().split())
    students.append(Student(height,weight,i+1))

students.sort(key= lambda x: (x.height, -x.weight))

for i in range(n):
    print(f"{students[i].height} {students[i].weight} {students[i].idx}")