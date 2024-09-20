import sys

n = int(input())

class Meteo:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

arr = []

for i in range(n):
    arr.append(sys.stdin.readline().split())

meteo = [Meteo(date,day,weather) for date,day,weather in arr]

meteo.sort(key=lambda x:x.date)

for i, line in enumerate(meteo):
    if line.weather == 'Rain':
        print(f"{line.date} {line.day} {line.weather}")
        break