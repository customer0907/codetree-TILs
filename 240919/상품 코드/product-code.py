import sys

item_name, item_code = sys.stdin.readline().split()

class Item:
    def __init__(self, name='codetree', code='50'):
        self.name = name
        self.code = code

default_item = Item()
input_item = Item(item_name, item_code)

print(f"product {default_item.code} is {default_item.name}")
print(f"product {input_item.code} is {input_item.name}")