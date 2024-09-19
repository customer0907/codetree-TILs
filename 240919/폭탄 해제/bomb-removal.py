import sys

def_code, line_color, spe_sec = tuple(sys.stdin.readline().split())

class bomb_defused:
    def __init__(self,code,color,second):
        self.code = code
        self.color = color
        self.second = second

bomb = bomb_defused(def_code, line_color, spe_sec)

print(f"code : {bomb.code}\ncolor : {bomb.color}\nsecond : {bomb.second}")