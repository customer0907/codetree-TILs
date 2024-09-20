import sys

class Slowest:
    def __init__(self,name='',jibun='',area=''):
        self.name = name
        self.jibun = jibun
        self.area = area

n = int(input())
arr = [sys.stdin.readline().split() for _ in range(n)]
people = [Slowest(name, jibun, area) for name, jibun, area in arr]

target_idx = 0
for i, person in enumerate(people):
    if person.name > people[target_idx].name: # i번째 person name이 더 크면 (더 느리면) i
        target_idx = i

print(f"name {people[target_idx].name}\naddr {people[target_idx].jibun}\ncity {people[target_idx].area}")