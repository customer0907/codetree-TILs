import sys

class Identity:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name,height,weight

identity = []
for i in range(5):
    name, height, weight = tuple(sys.stdin.readline().split())
    identity.append(Identity(name, int(height), float(weight)))

identity.sort(key= lambda x: x.name)
print("name")
for i in range(5):
    print(f"{identity[i].name} {identity[i].height} {identity[i].weight}")

print("")

identity.sort(key= lambda x: -x.height)
print("height")
for i in range(5):
    print(f"{identity[i].name} {identity[i].height} {identity[i].weight}")